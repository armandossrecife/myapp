from flask import Blueprint, session, redirect
from flask import url_for, flash, render_template
import requests
from app import utilidades

tarefas_bp = Blueprint('tarefas', __name__)

@tarefas_bp.route('/tasks')
def my_tasks():
    if "username" not in session:
        return redirect(url_for("auth.login"))

    try:
        # Retrieve user information from FastAPI app using token
        headers = {"Authorization": f"Bearer {session['access_token']}"}
        url_router = f"{utilidades.API_URL}/users/{session['user_id']}"
        response = requests.get(url_router, headers=headers)
    
        if response.status_code == 200:
            user_data = response.json()            
            url_route_mytasks = f"{utilidades.API_URL}/users/{session['user_id']}/tasks"
            response_mytasks = requests.get(url_route_mytasks, headers=headers)

            if response_mytasks.status_code == 200:
                user_data_tasks = response_mytasks.json()
            return render_template("tarefas/lista_tarefas.html", user=user_data, usuario = session['username'], tarefas=user_data_tasks,
                profilePic=session['profile_image_url'], titulo="Dashboard", funcionalidade='Listar Tarefas')

        else:
            # Handle error retrieving user information
            error_message = f"Failed to retrieve user information in tasks - {response.status_code}"
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