from fastapi import FastAPI, Body, Header, UploadFile, File, HTTPException
import uvicorn
import models
from datetime import datetime
import utilidades
import uuid
import os
from fastapi.responses import FileResponse
from pydantic_settings import BaseSettings 
from functools import lru_cache
from fastapi.middleware.cors import CORSMiddleware
import httpx
import time
from jinja2 import Template
from fastapi import BackgroundTasks

origins = [
    "http://localhost", 
    "http://localhost:8080", 
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "https://yourdomain.com"
    ]

# Classe que permite manipular as configuracoes da aplicacao de forma integrada com o arquivo .env
class Settings(BaseSettings): 
    app_name: str = "MyFastAPI App" 
    admin_email: str = "armando@ufpi.edu.br"
    database_url: str = "sqlite:///my_db.db"
    secret_key: str = "minhachavesecreta"
    allowed_hosts: list = ["*", "localhost"] 
    debug: bool = False
    class Config: env_file = ".env"

# Guarda as informacoes de configuracao no cache da aplicacao
@lru_cache()
def get_settings(): 
    return Settings()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],
)

# Faz a verificacao de cada requisicao da aplicacao
@app.middleware("http")
async def validate_host(request, call_next):
    settings = get_settings()
    host = request.headers.get("host", "").split(":")[0]
    print(f"Host: {host}")
    print(settings.allowed_hosts)
    if settings.debug or host in settings.allowed_hosts:
        return await call_next(request)
    raise HTTPException(status_code=400, detail="Invalid host")

minhas_tags = []

@app.get('/index')
def welcome():
    settings = get_settings()
    mensagem = "Bem vindo ao FastAPI"
    return {
        "mensagem": mensagem,
        "app_name": settings.app_name,
        "admin_email":settings.admin_email,
        "debug_mode":settings.debug        
    }

@app.get('/google/{pesquisa}')
async def get_google_search(pesquisa:str):
    t1 = time.time()
    async with httpx.AsyncClient() as client:
        URL=f"https://www.google.com/search?q={pesquisa}"
        response = await client.get(URL)
        conteudo = response.content
        conteudo_decodificado = utilidades.decodifica_conteudo(conteudo)
        t2 = time.time()
        delta = t2-t1
        print(f"Tempo de resposta: {delta}")
        template = Template(conteudo_decodificado)
        html_output = template.render()
        my_links = utilidades.extract_links_from_html(html_output)
        print(my_links)
        qtd_links = len(my_links)
        return {
            "tempo":delta,
            "qtd_links":qtd_links
        }

def processa_tarefa(cpf:str):
    print(f"CPF: {cpf}")
    utilidades.minha_tarefa(total_seconds=5)

@app.get('/tarefa/{cpf}')
async def tarefa_demorada(cpf:str, background_tasks:BackgroundTasks):
    background_tasks.add_task(processa_tarefa, cpf)
    return {
        "mensagem": f"Tarefa do cpf {cpf} enviada para processamento"
    }

# Passa os dados no path da URL
@app.get('/hi/{who}')
def quem(who:str):    
    mensagem = f'Olá {who}, seja bem vindo ao FastAPI'
    return mensagem

# Passa os dados na querystring da URL
@app.get('/dados')
def dados_pessoa(nome: str, telefone: str):
    dados_pessoais = {'nome':nome, 'telefone':telefone}
    return dados_pessoais

# Passa os dados no corpo da mensagem (usando o Post)
@app.post('/informacoes')
def dados_no_corpo(dados:dict = Body(embed=True)):
    return dados

# Passa os dados no cabecalho da mensagem (usando o Post)
@app.get('/configuracao')
def dados_no_cabecalho(user_agent = Header()):
    return user_agent

@app.post('/tags')
def criar_tag(tag_in:models.TagIn = Body(embed=True)):
    nova_tag = models.Tag(tag=tag_in.tag, created=datetime.now(), secret="shhhh")
    minhas_tags.append(nova_tag)
    mensagem = f'Tag {nova_tag.tag} adicionada com sucesso!'
    return mensagem

@app.get('/tags')
def lista_tags():
    return "minhas listas ...."

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    extensao = utilidades.get_file_extension(file.filename)
    filename_uuid = str(uuid.uuid4())
    uploaded_file = filename_uuid + "." + extensao
    if utilidades.allowed_file(uploaded_file):
        file_location = f"{utilidades.UPLOAD_DIRECTORY}/{uploaded_file}"
        extensao = utilidades.get_file_extension(uploaded_file)
        file_type = utilidades.get_media_type(extensao)
        with open(file_location, "wb+") as file_object:
            file_object.write(await file.read())
    else:
        raise HTTPException(status_code=404, detail="Erro: Tipo de arquivo não permitido")
    return {"filename": file.filename, "type":file_type}

@app.get("/files")
def list_files():
    files = os.listdir(utilidades.UPLOAD_DIRECTORY)
    return {"files": files}

@app.get("/download/{file_name}")
def download_file(file_name: str):
    file_path = f"{utilidades.UPLOAD_DIRECTORY}/{file_name}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)

if __name__ == "__main__": 
    uvicorn.run(debug=True)