from flask import Flask, render_template, request, send_from_directory
import requests
import os
import utilidades
from app.routes import auth
from app.routes import dashboard
from app.routes import tarefas

app = Flask(__name__)
app.secret_key = "my_secret_key"

BACKEND_IP = os.getenv('BACKEND_IP')
BACKEND_PORT = os.getenv('BACKEND_PORT')
FASTAPI_URL = "http://localhost:8000"

STATIC_PATH = os.path.join(app.root_path, 'static')

if BACKEND_IP and BACKEND_PORT:
    FASTAPI_URL = f"http://{BACKEND_IP}:{BACKEND_PORT}"
else:
    print("Você precisa definir o IP e porta do backend")

url_servico_upload = f'{FASTAPI_URL}/upload'
url_servico_files = f'{FASTAPI_URL}/files'
url_servico_download = f"{FASTAPI_URL}/download"

#Registra os Blueprints
app.register_blueprint(auth.auth_bp)
app.register_blueprint(dashboard.dashboard_bp)
app.register_blueprint(tarefas.tarefas_bp)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(STATIC_PATH, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Recursos Publicos

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        print(f"file.filename: {file.filename}")
        print(f"file.content_type: {file.content_type}")
        files = {'file': (file.filename, file.read(), file.content_type)}
        response = requests.post(url_servico_upload, files=files)
        if response.status_code == 200:
            return 'File uploaded successfully'
        else:
            return 'Error uploading file'
    return render_template('upload.html')

@app.route('/arquivos')
def list_files():
    response = requests.get(url_servico_files)
    if response.status_code == 200:
        files = response.json()['files']
        return render_template('list_files.html', files=files)
    else:
        return 'Error listing files'

@app.route('/download/<filename>')
def download_file(filename):
    url_servico_download_file = url_servico_download + '/'+ filename
    response = requests.get(url_servico_download_file, stream=True)
    if response.status_code == 200:
        extensao = utilidades.get_file_extension(filename)
        file_type = utilidades.get_media_type(extensao)
        # para imagem
        if file_type == "image/jpeg" or file_type == "image/jpg" or file_type=="image/png":
            return render_template('view_image.html', filename=filename, url_file=url_servico_download_file)
        # para video
        if file_type == "video/mp4":
            return render_template('view_video.html', filename=filename, url_file=url_servico_download_file) 
        # para audio
        if file_type == "audio/mp3":
            return render_template('view_audio.html', filename=filename, url_file=url_servico_download_file)
    else:
        return 'Error downloading file'

if __name__ == '__main__':
    app.run(debug=True)