import json
import os
from bs4 import BeautifulSoup
import requests
import time
from tqdm import tqdm

UPLOAD_DIRECTORY = "uploads"

ALLOWED_EXTENSIONS = {'jpeg','jpg', 'png', 'mp4', 'mp3'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower()            

def get_media_type(extension):
  media_types = {
      "jpeg": "image/jpeg",
      "jpg": "image/jpeg",
      "png": "image/png",
      "mp4": "video/mp4",
      "mp3": "audio/mp3"
  }
  return media_types.get(extension.lower())

def salva_json_em_arquivo(my_json, nome_arquivo, path_json):
    try:
        filename = f"{nome_arquivo}.json"
        file = f"{path_json}/{filename}"
        with open(file, 'w') as f:
            json.dump(my_json, f)
    except Exception as ex:
        raise ValueError(str(ex))

def cria_pasta(path_folder):
    if not os.path.exists(path_folder):
        os.makedirs(path_folder)

# Faz a decodificacao do conteudo para o encoding correto
# Exemplo: codificacao UTF-8: https://pt.wikipedia.org/wiki/UTF-8
def decodifica_conteudo(conteudo):
  try:
      conteudo_str = conteudo.decode('utf-8')
  except UnicodeDecodeError as e:
      try:
        conteudo_str = conteudo.decode('latin-1')
      except UnicodeDecodeError as e:
        try:
          conteudo_str = conteudo.decode('ISO-8859-1')
        except UnicodeDecodeError as e:
          print(f"UnicodeDecodeError: {e}")
          conteudo_str = None

  return conteudo_str

def extract_links_from_html(content):
    soup = BeautifulSoup(content, 'html.parser')

    # Find all <a> tags with an 'href' attribute
    links = soup.find_all('a', href=True)

    # Print the URLs
    for link in links:
        print(link['href'])

    return links

def faz_alguma_coisa(tempo):
    time.sleep(tempo)

def minha_tarefa(total_seconds):
    # Como o tqdm atualiza com base em iterações
    # podemos criar um loop com atrasos de um segundo
    with tqdm(total=total_seconds, desc="Simulando um progresso", unit="s") as pbar:
        for _ in range(total_seconds):
            faz_alguma_coisa(tempo=1)
            pbar.update(1)  # Atualiza a barra de progresso em 1 segundo.