from fastapi import FastAPI, Body, Header
import uvicorn
import models
from datetime import datetime

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
    return minhas_tags

if __name__ == "__main__": 
    uvicorn.run(debug=True)