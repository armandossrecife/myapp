import unittest
import requests
import models
from datetime import datetime

class TestGetWelcome(unittest.TestCase):
    def test_get_request(self):
        recurso = "http://localhost:8000/index"
        my_request = requests.get(recurso)

        # Assertions to verify the response
        self.assertEqual(my_request.status_code, 200)  # Check for a successful response
        self.assertIn("Bem vindo ao FastAPI", my_request.text)  # Replace with the expected content
        self.assertEqual(my_request.url, recurso)  # Verify the correct URL
        self.assertIn("Content-Type", my_request.headers)  # Check for a content type header

class TestGetWho(unittest.TestCase):
    def test_get_request(self):
        recurso = "http://localhost:8000/hi/armando"
        my_request = requests.get(recurso)

        # Assertions to verify the response
        self.assertEqual(my_request.status_code, 200)  # Check for a successful response
        self.assertIn("Olá armando, seja bem vindo ao FastAPI", my_request.text)  # Replace with the expected content
        self.assertEqual(my_request.url, recurso)  # Verify the correct URL
        self.assertIn("Content-Type", my_request.headers)  # Check for a content type header

class TestGetDados(unittest.TestCase):
    def test_get_request(self):
        recurso = "http://localhost:8000/dados?nome=armando&telefone=86994693558"
        my_request = requests.get(recurso)

        # Assertions to verify the response
        self.assertEqual(my_request.status_code, 200)  # Check for a successful response
        self.assertEqual(my_request.url, recurso)  # Verify the correct URL
        self.assertIn("Content-Type", my_request.headers)  # Check for a content type header
        retorno = my_request.json()
        self.assertEqual("armando", retorno['nome'])
        self.assertEqual("86994693558", retorno['telefone'])

class TestGetDados2(unittest.TestCase):
    def test_get_request(self):
        recurso = "http://localhost:8000/dados"
        parametros = {'nome':"armando", 'telefone':"86994693558"}
        my_request = requests.get(recurso, params=parametros)

        # Assertions to verify the response
        self.assertEqual(my_request.status_code, 200)  # Check for a successful response
        self.assertIn("Content-Type", my_request.headers)  # Check for a content type header
        retorno = my_request.json()
        self.assertEqual("armando", retorno['nome'])
        self.assertEqual("86994693558", retorno['telefone'])

class TestPostInformacoes(unittest.TestCase):
    def test_post_request(self):
        recurso = "http://localhost:8000/informacoes"
        parametros = {"dados":
                {'nome':"armando", 'telefone':"86994693558", 'cidade':"Teresina", 'estado':"PI"}
            }
        my_request = requests.post(recurso, json=parametros)

        # Assertions to verify the response
        self.assertEqual(my_request.status_code, 200)  # Check for a successful response
        self.assertIn("Content-Type", my_request.headers)  # Check for a content type header
        retorno = my_request.json()
        self.assertEqual("armando", retorno['nome'])
        self.assertEqual("86994693558", retorno['telefone'])
        self.assertEqual("Teresina", retorno['cidade'])
        self.assertEqual("PI", retorno['estado'])

class TestGetConfiguracao(unittest.TestCase):
    def test_get_request(self):
        recurso = "http://localhost:8000/configuracao"
        my_request = requests.get(recurso)

        # Assertions to verify the response
        self.assertEqual(my_request.status_code, 200)  # Check for a successful response
        self.assertIn("Content-Type", my_request.headers)  # Check for a content type header
        retorno = my_request.json()
        print(retorno)

class TestPostNewTag(unittest.TestCase):
    def test_post_request(self):
        recurso = "http://localhost:8000/tags"
        nova_tag = models.TagIn(tag="Nova tag de testes")
        nova_tag_json = {"tag_in":
                            {
                                "tag":nova_tag.tag
                            }
                        }
        my_request = requests.post(recurso, json=nova_tag_json)

        # Assertions to verify the response
        self.assertEqual(my_request.status_code, 200)  # Check for a successful response
        self.assertIn("Content-Type", my_request.headers)  # Check for a content type header
        retorno = my_request.json()
        print(retorno)

class TestGetTags(unittest.TestCase):
    def test_get_request(self):
        recurso = "http://localhost:8000/tags"
        my_request = requests.get(recurso)

        # Assertions to verify the response
        self.assertEqual(my_request.status_code, 200)  # Check for a successful response
        self.assertEqual(my_request.url, recurso)  # Verify the correct URL
        self.assertIn("Content-Type", my_request.headers)  # Check for a content type header
        retorno = my_request.json()
        print(retorno)

if __name__ == "__main__":
    unittest.main()