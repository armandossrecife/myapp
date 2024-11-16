from fastapi import FastAPI, Body, Header, UploadFile, File, HTTPException
import uvicorn
import models
from datetime import datetime
import utilidades
import uuid
import os
from fastapi.responses import FileResponse

app = FastAPI()

minhas_tags = []

@app.get('/index')
def welcome():
    return "Bem vindo ao FastAPI"

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