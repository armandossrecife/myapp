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

@router.get("/users/{username}/notes/{note_id}", dependencies=[Depends(seguranca.get_current_user)], response_model=entidades.Note)
async def get_note_by_id(username: str, note_id: str, db: Session = Depends(banco.get_db)):
    try: 
        user_dao = banco.UserDAO(db)
        notas_dao = banco.NoteDAO(db)
        
        user = user_dao.get_user(username)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        nota = notas_dao.get_note_by_id(int(note_id))
        if not nota: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
        
        return nota
    except Exception as ex:
      raise HTTPException(status_code=500, detail=f"Internal server error. {str(ex)}")

@router.post("/users/{username}/notes", dependencies=[Depends(seguranca.get_current_user)])
async def create_note(nova_nota: entidades.NewNote, db: Session = Depends(banco.get_db)):
    try:
        user_dao = banco.UserDAO(db)
        note_dao = banco.NoteDAO(db)

        user = user_dao.get_user(nova_nota.username)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found") 

        new_note = note_dao.create_note(user.id, nova_nota.description)
        content = {"message": f"Nova anotação cadastrada com sucesso!", 
              "id": user.id,
              "username": user.username,
              "email": user.email,
          }
        return content
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error creating note: {str(ex)}")

@router.post("/users/{username}/notes/{note_id}", dependencies=[Depends(seguranca.get_current_user)])
async def edit_note(note_id: str, nota_editada: entidades.NewNote, db: Session = Depends(banco.get_db)):
    try:
        user_dao = banco.UserDAO(db)
        note_dao = banco.NoteDAO(db)

        user = user_dao.get_user(nota_editada.username)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found") 

        nota_atualizada = note_dao.update_note(note_id=note_id, description=nota_editada.description)
        content = {"message": f"Nota salva com sucesso!", 
              "id": user.id,
              "username": user.username,
              "email": user.email,
          }
        return content
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error creating note: {str(ex)}")

@router.post("/users/{username}/notes/{note_id}/delete", dependencies=[Depends(seguranca.get_current_user)])
async def delete_note_by_id(username: str, note_id: str, db: Session = Depends(banco.get_db)):
    try: 
        user_dao = banco.UserDAO(db)
        notas_dao = banco.NoteDAO(db)
        
        user = user_dao.get_user(username)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        nota_deletada = notas_dao.delete_note(note_id)

        if nota_deletada:
            content = {"message": f"Nota excluída com sucesso!", 
              "id": user.id,
              "username": user.username,
              "email": user.email,
          }            
        else:
            content = {"message": f"Erro ao remover a nota!", 
              "id": user.id,
              "username": user.username,
              "email": user.email,
          }
        return content

    except Exception as ex:
      raise HTTPException(status_code=500, detail=f"Internal server error. {str(ex)}")