from flask import Blueprint, session, redirect
from flask import url_for, flash, render_template
import requests
from app import utilidades
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/jobs/grafico')
def my_jobs_graphic():
    if "username" not in session:
        return redirect(url_for("auth.login"))

    try:
        # Retrieve user information from FastAPI app using token
        headers = {"Authorization": f"Bearer {session['access_token']}"}
        url_router = f"{utilidades.API_URL}/users/{session['user_id']}"
        response = requests.get(url_router, headers=headers)
    
        if response.status_code == 200:
            user_data = response.json()            
            url_route_myjobs = f"{utilidades.API_URL}/users/{session['user_id']}/jobs"
            response_myjobs = requests.get(url_route_myjobs, headers=headers)

            if response_myjobs.status_code == 200:
                user_data_jobs = response_myjobs.json()
                df = pd.DataFrame(user_data_jobs)
                fig = px.timeline(df, x_start="start", x_end="finish", y="task")
                fig.update_yaxes(autorange="reversed")
                return render_template('jobs/grafico_jobs.html', graphJSON=fig.to_json(), 
                            user=user_data, usuario = session['username'], tarefas=user_data_jobs,
                            profilePic=session['profile_image_url'], titulo="Dashboard", 
                            funcionalidade='Gráfico de Trabalhos (Jobs)')
            else:
                error_message = f"Failed to retrieve jobs graphic - {response.status_code}"
                return render_template("error.html", message=error_message)
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


@jobs_bp.route('/jobs')
def my_jobs():
    if "username" not in session:
        return redirect(url_for("auth.login"))

    try:
        # Retrieve user information from FastAPI app using token
        headers = {"Authorization": f"Bearer {session['access_token']}"}
        url_router = f"{utilidades.API_URL}/users/{session['user_id']}"
        response = requests.get(url_router, headers=headers)
    
        if response.status_code == 200:
            user_data = response.json()            
            url_route_myjobs = f"{utilidades.API_URL}/users/{session['user_id']}/jobs"
            response_myjobs = requests.get(url_route_myjobs, headers=headers)

            if response_myjobs.status_code == 200:
                user_data_jobs = response_myjobs.json()
            return render_template("jobs/lista_jobs.html", user=user_data, usuario = session['username'], jobs=user_data_jobs,
                profilePic=session['profile_image_url'], titulo="Dashboard", funcionalidade='Listar Trabalhos')

        else:
            # Handle error retrieving user information
            error_message = f"Failed to retrieve user information in jobs - {response.status_code}"
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