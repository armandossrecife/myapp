from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app import banco
from app import utilidades
from jose import JWTError, jwt
from datetime import datetime, timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def create_access_token(data: dict):
  to_encode = data.copy()
  expire = datetime.utcnow() + timedelta(minutes=utilidades.ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire.timestamp()})
  return jwt.encode(to_encode, utilidades.SECRET_KEY, algorithm=utilidades.ALGORITHM)

def verify_token(token: str, credentials_exception=None):
  try:
    payload = jwt.decode(token, utilidades.SECRET_KEY, algorithms=[utilidades.ALGORITHM])
    return payload["sub"]
  except JWTError:
    # raise credentials_exception
    raise ValueError('Erro de credencial!')
  except Exception as ex:
    raise ValueError(f'Erro ao verificar o token: {str(ex)}')

async def get_current_user(db: Session = Depends(banco.get_db), token: str = Depends(oauth2_scheme)):
  try: 
    username = verify_token(token)
    user_dao = banco.UserDAO(db)
    user = user_dao.get_user(username)
    if not user:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return user
  except Exception as ex:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid token: {str(ex)}")