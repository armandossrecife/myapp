from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
from app import utilidades
from app import banco
from app import seguranca
import mimetypes
import os
from app import entidades

router = APIRouter()

@router.get("/users/{user_id}/profile", dependencies=[Depends(seguranca.get_current_user)])
async def get_user_profile(user_id: int, db: Session = Depends(banco.get_db)):
    try: 
      user_dao = banco.UserDAO(db)
      user = user_dao.get_user_by_id(user_id)
      if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

      image_profile_name = user_dao.get_image_profile_for_user(user.id) 
      image_url = f"{utilidades.API_URL}/users/{user_id}/profile/{image_profile_name}"
      image_default = f"{utilidades.API_URL}/users/{user.username}/profile/default.png"
      content = {
          "message": "User image profile",
          "id": user.id,
          "username": user.username,
          "email": user.email,
          "profile_image_url": image_url if image_profile_name else image_default  # Include image URL if available
      }
      return content
    except Exception as ex:
      raise HTTPException(status_code=500, detail=f"Internal server error. {str(ex)}")

@router.post("/users/{user_id}/picture", dependencies=[Depends(seguranca.get_current_user)])
async def upload_image_prolife(user_id:int, image: UploadFile = File(...), db: Session = Depends(banco.get_db)):
    user_dao = banco.UserDAO(db)
    user = user_dao.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    extension = os.path.splitext(image.filename)[1].lower()
    if extension not in utilidades.ALLOWED_EXTENSIONS:
        return HTTPException(status_code=400, detail=f"Unsupported file extension. Allowed extensions: {', '.join(utilidades.ALLOWED_EXTENSIONS)}")

    try: 
      # Create 'profile' folder if it doesn't exist
      os.makedirs(utilidades.IMAGES_PATH_PROFILE, exist_ok=True)
      filepath = os.path.join(utilidades.IMAGES_PATH_PROFILE, image.filename)
      filename = image.filename

      # Save the image file
      contents = await image.read()
      with open(filepath, "wb") as f:
        f.write(contents)
        image_url = f"{utilidades.API_URL}/users/{user.username}/profile/{image.filename}"
      user_dao.add_profile_image_to_user(user.id, filename)
      
      content = {"message": f"Imagem do profile atualizada com sucesso!: {image.filename}", 
          "filename":image.filename,
          "id": user.id,
          "username": user.username,
          "email": user.email,
          "profile_image_url": image_url if image.filename else None  # Include image URL if available
          }
      return content

    except Exception as ex:
      raise HTTPException(status_code=500, detail=f"Internal server error. {str(ex)}")

@router.post("/users/{user_id}/password", dependencies=[Depends(seguranca.get_current_user)])
async def update_password(user_id: int, user_password: entidades.UserPassword, db: Session = Depends(banco.get_db)):
    user_dao = banco.UserDAO(db)
    user = user_dao.get_user_by_id(user_id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found - from update password")

    try: 
      # confirma o password passado nos dados no formulario
      if user_password.password == user_password.confirm_password:     
        # faz a logica que atuliza o password no banco
        user_dao.update_password_user(user_id, user_password.password)
        content = {"message": f"Password atualizado com sucesso!", 
              "id": user.id,
              "username": user.username,
              "email": user.email
          }
        return content
      else:
        return {"message":"Password inválido!"}
    except Exception as ex:
      raise HTTPException(status_code=500, detail=f"Internal server error. {str(ex)}")

@router.get("/users/{user_id}/profile/{filename}")
async def show_image_profile(filename: str, user_id: int, db: Session = Depends(banco.get_db)):
    user_dao = banco.UserDAO(db)
    user = user_dao.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    try:      
        # TODO: melhorar o sanitized_filename para nao quebrar a referencia do arquivo quando tiver espaco em branco ou caracteres especiais      
        sanitized_filename = utilidades.validate_filename(filename)
        filepath = os.path.join(utilidades.IMAGES_PATH_PROFILE, sanitized_filename)
        content_type = mimetypes.guess_type(filepath)[0]
        return FileResponse(filepath, media_type=content_type)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail="Image not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error. {str(e)}")