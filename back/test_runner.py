import unittest
from app.testes.suite_tc_notesdao import NoteDAOTest
from app.testes.suite_tc_usersdao import UserDAOTest
from sqlalchemy import create_engine
from app import modelos
from app import banco
from HtmlTestRunner import HTMLTestRunner
import os
from datetime import datetime

RESULTADOS_SUITE_TESTES_USUARIOS = "resultados/crud_users_suite"
RESULTADOS_SUITE_TESTES_NOTAS = "resultados/crud_notes_suite"
PATH_LOCAL = os.getcwd()

def set_test_suite(testcase):
    loader = unittest.TestLoader()
    test_suite = loader.loadTestsFromTestCase(testcase)
    return test_suite

def clean_database():
    # Create database engine
    engine = create_engine(banco.DATABASE_URL)
    # Clean database
    modelos.Base.metadata.drop_all(engine)
    modelos.Base.metadata.create_all(bind=engine)

def perform_runner(dao_test, resultados):
    my_suite = set_test_suite(testcase=dao_test)
    my_runner = HTMLTestRunner(output=resultados, verbosity=2)
    my_runner.run(my_suite)
    return my_runner

t1 = datetime.now()

print("Executa a suite de testes de CRUD de Usuários")
print("Aguarde...")
runner_users = perform_runner(dao_test=UserDAOTest, resultados=RESULTADOS_SUITE_TESTES_USUARIOS)

print("Limpa o banco de dados")
clean_database()

print("Executa a suite de testes de CRUD de Notas de um usuário")
print("Aguarde...")
runner_notes = perform_runner(dao_test=NoteDAOTest, resultados=RESULTADOS_SUITE_TESTES_NOTAS)

t2 = datetime.now()

print(f"O resultado dos testes estão disponíveis em: ")
print(f"{PATH_LOCAL}/{RESULTADOS_SUITE_TESTES_NOTAS}")
print(f"{PATH_LOCAL}/{RESULTADOS_SUITE_TESTES_USUARIOS}")

print(f"Tempo total: {t2-t1}")