from flask import Blueprint, session, redirect
from flask import url_for, flash, render_template
import requests
from app import utilidades

notas_bp = Blueprint('notas', __name__)

@notas_bp.route('/notas')
def my_notas():
    if "username" not in session:
        return redirect(url_for("auth.login"))

    try:
        # Retrieve user information from FastAPI app using token
        access_token = session["access_token"] 
        headers = {"Authorization": f"Bearer {access_token}"}
        usuario_logado = session['username']
        url_router = f"{utilidades.API_URL}/users/{usuario_logado}"
        response = requests.get(url_router, headers=headers)
    
        if response.status_code == 200:
            user_data = response.json()            
            url_route_mynotas = f"{utilidades.API_URL}/users/{usuario_logado}/notes"
            response_mynotas = requests.get(url_route_mynotas, headers=headers)

            if response_mynotas.status_code == 200:
                user_data_notas = response_mynotas.json()
            return render_template("notas/lista_notas.html", user=user_data, usuario = usuario_logado, notas=user_data_notas,
                profilePic=session['profile_image_url'], titulo="Dashboard", funcionalidade='Listar Notas')

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