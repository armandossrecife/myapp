from pydantic import BaseModel
from datetime import datetime
from datetime import date

class TarefaDTO(BaseModel):
    descricao: str
    data_expiracao: datetime
    prioridade: int
    data_conclusao: datetime | None = None
    concluida: bool = False

class JobDTO(BaseModel):
    task: str
    start: date | None = None
    finish: date | None = None