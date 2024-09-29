from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import banco
from app import seguranca
from app.processamento import tarefas as processamento_tarefas
from datetime import datetime

router = APIRouter()

@router.get("/users/{user_id}/tasks", dependencies=[Depends(seguranca.get_current_user)])
async def get_user_tasks(user_id: int, db: Session = Depends(banco.get_db)):
    try: 
        user_dao = banco.UserDAO(db)
        user = user_dao.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        # Criar as tarefas (exemplo com lista de dicionários)
        tarefas = [
            {"descricao": "Tarefa 1", "data_expiracao": processamento_tarefas.add_days(datetime.now(), 5), "prioridade": 1},
            {"descricao": "Tarefa 2", "data_expiracao": processamento_tarefas.add_days(datetime.now(), 10), "prioridade": 2},
            {"descricao": "Tarefa 3", "data_expiracao": processamento_tarefas.add_days(datetime.now(), 15), "prioridade": 3}
        ]

        # Criar os registros
        tarefas_DTO_exemplo = processamento_tarefas.criar_registros_tarefas_DTO(tarefas)
        return tarefas_DTO_exemplo
    except Exception as ex:
      raise HTTPException(status_code=500, detail=f"Internal server error. {str(ex)}")