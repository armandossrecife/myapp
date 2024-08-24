from flask import Blueprint, request, session, redirect
from flask import url_for, flash, render_template
import requests
from app import utilidades
from app import dto
import json

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route("/dashboard")
def dashboard():
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
            url_route_profile = f"{utilidades.API_URL}/users/{usuario_logado}/profile"
            response_profile = requests.get(url_route_profile, headers=headers)

            if response_profile.status_code == 200:
                user_data_profile = response_profile.json()
                session['profile_image_url'] = user_data_profile['profile_image_url']
            return render_template("dashboard/starter.html", user=user_data, usuario = usuario_logado, 
                profilePic=session['profile_image_url'], titulo="Dashboard", funcionalidade='Main')

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

@dashboard_bp.route("/profile")
def show_profile():
    if "username" not in session:
        return redirect(url_for("auth.login"))

    try:
        access_token = session["access_token"] 
        headers = {"Authorization": f"Bearer {access_token}"}
        usuario_logado = session['username']
        url_router = f"{utilidades.API_URL}/users/{usuario_logado}"
        response = requests.get(url_router, headers=headers)
    
        if response.status_code == 200:
            user_data = response.json()            
            url_route_profile = f"{utilidades.API_URL}/users/{usuario_logado}/profile"
            response_profile = requests.get(url_route_profile, headers=headers)

            if response_profile.status_code == 200:
                user_data_profile = response_profile.json()
                session['profile_image_url'] = user_data_profile['profile_image_url']
                
                return render_template("dashboard/profile.html", user=user_data, usuario = usuario_logado, 
                profilePic=session['profile_image_url'], titulo="Dashboard", funcionalidade="Profile")

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

@dashboard_bp.route("/profile", methods=["POST"])
def update_profile_picture():
    if "username" not in session:
        return redirect(url_for("auth.login"))

    try:
        access_token = session["access_token"] 
        headers = {"Authorization": f"Bearer {access_token}"}
        usuario_logado = session['username']
        url_router_profile = f"{utilidades.API_URL}/users/{usuario_logado}/profile"

        if request.method == 'POST':
            image = request.files['profile_picture']
            response_profile = requests.post(url_router_profile, headers=headers, files={'image': (image.filename, image.read(), image.content_type)})
        
            if response_profile.status_code == 200:
                user_data = response_profile.json() 
                session['profile_image_url'] = user_data['profile_image_url']
                flash(user_data["message"], 'success')
                return redirect(url_for("dashboard.dashboard"))
            else:
                # Handle error retrieving user information
                error_message = f"Failed to retrieve user information - {response_profile.status_code}"
                return render_template("error.html", message=error_message)

    except requests.exceptions.MissingSchema:
        error_message = f"URL {url_router_profile} inválida"
    except requests.exceptions.ConnectionError:
        error_message = "Erro de conexão"
    except IOError: 
        error_message = "Erro de IO"    
    except Exception as ex:
        error_message = f"Erro: {str(ex)}"
    flash(error_message, category='danger')

    return render_template("auth/login.html", error_message=error_message)

@dashboard_bp.route("/password")
def show_page_password():
    if "username" not in session:
        return redirect(url_for("auth.login"))

    try:
        access_token = session["access_token"] 
        headers = {"Authorization": f"Bearer {access_token}"}
        usuario_logado = session['username']
        url_router = f"{utilidades.API_URL}/users/{usuario_logado}"
        response = requests.get(url_router, headers=headers)
    
        if response.status_code == 200:
            user_data = response.json()            
                
            return render_template("dashboard/profile_password.html", user=user_data, usuario = usuario_logado, 
                profilePic=session['profile_image_url'], titulo="Dashboard", funcionalidade="Password")

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

@dashboard_bp.route("/password", methods=["POST"])
def update_profile_password():
    if "username" not in session:
        return redirect(url_for("auth.login"))

    try:
        access_token = session["access_token"] 
        headers = {"Authorization": f"Bearer {access_token}"}
        usuario_logado = session['username']
        url_router_password = f"{utilidades.API_URL}/users/{usuario_logado}/password"

        password = request.form['password_profile']
        confirm_password = request.form['confirm_password_profile']
        user_password_data = {"username": usuario_logado, "password":password, "confirm_password":confirm_password}
        response_profile_password = requests.post(url_router_password, headers=headers, json=user_password_data)
        
        if response_profile_password.status_code == 200:
            user_data = response_profile_password.json() 
            flash(user_data["message"], 'success')
            return redirect(url_for("dashboard.dashboard"))
        else:
            # Handle error retrieving user information
            error_message = f"Failed to retrieve user information - {response_profile_password.status_code}"
            return render_template("error.html", message=error_message)
    except requests.exceptions.MissingSchema:
        error_message = f"URL {url_router_password} inválida"
    except requests.exceptions.ConnectionError:
        error_message = "Erro de conexão"
    except IOError: 
        error_message = "Erro de IO"    
    except Exception as ex:
        error_message = f"Erro: {str(ex)}"
    flash(error_message, category='danger')

    return render_template("auth/login.html", error_message=error_message)