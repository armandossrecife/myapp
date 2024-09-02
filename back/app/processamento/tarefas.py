from datetime import datetime, timedelta
from app import dtos

class Tarefa:
    def __init__(self, descricao, data_expiracao, prioridade):
        self.descricao = descricao
        self.data_expiracao = data_expiracao
        self.prioridade = prioridade
        self.concluida = False
        self.data_conclusao = None

    def get_data_expiracao(self):
      return self.data_expiracao.strftime("%d/%m/%Y")

    def get_data_conclusao(self):
      return self.data_conclusao.strftime("%d/%m/%Y")

    def __str__(self):
      return f"Descrição: {self.descricao} - Data de Expiração: {self.get_data_expiracao()} - Prioridade: {self.prioridade}"

class RegistrosTarefaDTO:
    def __init__(self, lista_tarefas_dto):
        self.colunas = list(vars(lista_tarefas_dto[0]).keys())
        self.registros = self.cria_registros(lista_tarefas_dto)

    def cria_registros(self, lista_tarefas):
        registros = []
        for tarefa in lista_tarefas:
            registro = {coluna: getattr(tarefa, coluna) for coluna in self.colunas}
            registros.append(registro)
        return registros

def add_days(date:datetime, days):
    new_date = date + timedelta(days=days)
    return new_date

def criar_tarefa_dto(tarefa):
    tarefaDTO = dtos.TarefaDTO(
        descricao=tarefa['descricao'],
        data_expiracao=tarefa['data_expiracao'],
        prioridade=tarefa['prioridade'],
        data_conclusao=None,  # Inicializar com None para indicar não concluída
        concluida=False
    )
    return tarefaDTO

def criar_registros_tarefas_DTO(tarefas):
    registros = []
    for tarefa in tarefas:
        tarefa_DTO = criar_tarefa_dto(tarefa)
        registros.append(tarefa_DTO)
    return registros