from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import banco
from app import seguranca
from app import entidades

router = APIRouter()

@router.get("/users/{username}/notes", dependencies=[Depends(seguranca.get_current_user)], response_model=list[entidades.Note])
async def get_user_notes(username: str, db: Session = Depends(banco.get_db)):
    try: 
        user_dao = banco.UserDAO(db)
        notas_dao = banco.NoteDAO(db)
        
        user = user_dao.get_user(username)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        notas = notas_dao.get_all_notes()
        return notas
    except Exception as ex:
      raise HTTPException(status_code=500, detail=f"Internal server error. {str(ex)}")