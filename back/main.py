from fastapi import FastAPI, File, UploadFile, HTTPException
from app import banco
from app import entidades
from app.routes import auth, users, profile, tarefas, jobs
import uvicorn
import uuid
from fastapi.responses import FileResponse
import utilidades
import os

app = FastAPI()

# Call the create_tables function outside your application code (e.g., in a separate script)
banco.create_tables()

# Cria um usuario default
my_user = entidades.User(id=0, username="armando", email="armando@ufpi.edu.br", password="armando")

db = banco.get_db()
user_dao = banco.UserDAO(db)
user_dao.create_user(my_user)
print(f"Usuário {my_user.username} criado com sucesso!")

# Include das rotas da aplicacao
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(profile.router)
app.include_router(tarefas.router)
app.include_router(jobs.router)

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
    return {"filename": file.filename}

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
  uvicorn.run(app, host="0.0.0.0", port=8000)