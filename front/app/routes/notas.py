from flask import Blueprint, session, redirect
from flask import url_for, flash, render_template, request
import requests
from app import utilidades

notas_bp = Blueprint('notas', __name__)

@notas_bp.route('/notas')
def my_notas():
    if "username" not in session:
        return redirect(url_for("auth.login"))

    try:
        # Retrieve user information from FastAPI app using token
        headers = {"Authorization": f"Bearer {session['access_token']}"}
        url_router = f"{utilidades.API_URL}/users/{session['user_id']}"
        response = requests.get(url_router, headers=headers)
    
        if response.status_code == 200:
            user_data = response.json()            
            url_route_mynotas = f"{utilidades.API_URL}/users/{session['user_id']}/notes"
            response_mynotas = requests.get(url_route_mynotas, headers=headers)

            if response_mynotas.status_code == 200:
                user_data_notas = response_mynotas.json()
            return render_template("notas/lista_notas.html", user=user_data, usuario = session['username'], notas=user_data_notas,
                profilePic=session['profile_image_url'], titulo="Dashboard", funcionalidade='Listar Notas')

        else:
            # Handle error retrieving user information
            error_message = f"Failed to retrieve user information in notes - {response.status_code}"
            return render_template("error.html", message=error_message)

    except requests.exceptions.MissingSchema:
        error_message = f"URL {url_router} inválida"
    except requests.exceptions.ConnectionError:
        error_message = "Erro de conexão"
    except IOError: 
        error_message = "Erro de IO"    
    except Exception as ex:
        error_message = f"Erro: {str(ex)}"
    flash(error_message, category='danger')

    return render_template("auth/login.html", error_message=error_message)

@notas_bp.route('/notas/nova', methods=['GET', 'POST'])
def nova_nota():
    if "username" not in session:
        return redirect(url_for("auth.login"))

    # Retrieve user information from FastAPI app using token
    headers = {"Authorization": f"Bearer {session['access_token']}"}
    url_router = f"{utilidades.API_URL}/users/{session['user_id']}"
    response = requests.get(url_router, headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()           

        if request.method == "POST":
            descricao_nota = request.form["descricao"]  
            note_data = {'description': descricao_nota, 'username': session['username']}
            
            url_route_new_note = f"{utilidades.API_URL}/users/{session['user_id']}/notes"                
            response_new_note = requests.post(url_route_new_note, headers=headers, json=note_data)

            if response_new_note.status_code == 201:
                user_data_new_data = response_new_note.json()
                flash(user_data_new_data["message"], 'success')
                return redirect(url_for("notas.my_notas"))
            else:
                # Handle error retrieving user information
                error_message = f"Failed to post new note - {response_new_note.status_code}"
                print(error_message)
                return render_template("error.html", message=error_message)
    
    return render_template("notas/nova_nota.html", user=user_data, usuario = session['username'], 
            profilePic=session['profile_image_url'], titulo="Dashboard", funcionalidade='Nova Nota')

@notas_bp.route('/notas/<int:id>', methods=['GET'])
def edita_nota(id):
    if "username" not in session:
        return redirect(url_for("auth.login"))

    try:
        # Retrieve user information from FastAPI app using token
        headers = {"Authorization": f"Bearer {session['access_token']}"}
        url_router = f"{utilidades.API_URL}/users/{session['user_id']}"
        response = requests.get(url_router, headers=headers)
    
        if response.status_code == 200:
            user_data = response.json()            
            url_route_edit_note = f"{utilidades.API_URL}/users/{session['user_id']}/notes/{id}"
            response_edit_note = requests.get(url_route_edit_note, headers=headers)

            if response_edit_note.status_code == 200:
                user_data_notas = response_edit_note.json()
                print(user_data_notas)
            return render_template("notas/edita_nota.html", user=user_data, usuario = session['username'], nota_selecionada=user_data_notas,
                profilePic=session['profile_image_url'], titulo="Dashboard", funcionalidade='Editar Nota')

        else:
            # Handle error retrieving user information
            error_message = f"Failed to retrieve user information - {response.status_code}"
            return render_template("error.html", message=error_message)

    except requests.exceptions.MissingSchema:
        error_message = f"URL {url_router} inválida"
    except requests.exceptions.ConnectionError:
        error_message = "Erro de conexão"
    except IOError: 
        error_message = "Erro de IO"    
    except Exception as ex:
        error_message = f"Erro: {str(ex)}"
    flash(error_message, category='danger')

    return render_template("auth/login.html", error_message=error_message)

@notas_bp.route('/notas/<int:id>', methods=['POST'])
def salva_nota(id):
    if "username" not in session:
        return redirect(url_for("auth.login"))

    try:
        # Retrieve user information from FastAPI app using token
        headers = {"Authorization": f"Bearer {session['access_token']}"}
        descricao_nota = request.form["descricao"]
        note_data = {'description': descricao_nota, 'username': session['username']}    

        url_route_save_note = f"{utilidades.API_URL}/users/{session['user_id']}/notes/{id}"
        response_save_note = requests.post(url_route_save_note, headers=headers, json=note_data)

        if response_save_note.status_code == 200:
            user_data_notas = response_save_note.json()
            flash(user_data_notas["message"], 'success')
            return redirect(url_for("notas.my_notas"))
        else:
            # Handle error retrieving user information
            error_message = f"Failed to save note - {response_save_note.status_code}"
            return render_template("error.html", message=error_message)

    except requests.exceptions.MissingSchema:
        error_message = f"URL {url_route_save_note} inválida"
    except requests.exceptions.ConnectionError:
        error_message = "Erro de conexão"
    except IOError: 
        error_message = "Erro de IO"    
    except Exception as ex:
        error_message = f"Erro: ao salvar nota {str(ex)}"
    flash(error_message, category='danger')

    return render_template("auth/login.html", error_message=error_message)    

@notas_bp.route('/notas/<int:id>/delete', methods=['POST'])
def exclui_nota(id):
    if "username" not in session:
        return redirect(url_for("auth.login"))

    try:
        # Retrieve user information from FastAPI app using token         
        headers = {"Authorization": f"Bearer {session['access_token']}"}
        url_route_delete_note = f"{utilidades.API_URL}/users/{session['user_id']}/notes/{id}/delete"
        response_delete_note = requests.post(url_route_delete_note, headers=headers)

        if response_delete_note.status_code == 200:
            user_data_notas = response_delete_note.json()
            flash(user_data_notas["message"], 'success')
            return redirect(url_for("notas.my_notas"))
        else:
            # Handle error retrieving user information
            error_message = f"Failed to delete note - {response_delete_note.status_code}"
            return render_template("error.html", message=error_message)

    except requests.exceptions.MissingSchema:
        error_message = f"URL {url_route_delete_note} inválida"
    except requests.exceptions.ConnectionError:
        error_message = "Erro de conexão"
    except IOError: 
        error_message = "Erro de IO"    
    except Exception as ex:
        error_message = f"Erro: ao salvar nota {str(ex)}"
    flash(error_message, category='danger')

    return render_template("auth/login.html", error_message=error_message)    