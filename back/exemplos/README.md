# Testes automáticos

Este diretório de exemplo tem dois arquivos críticos: 
- teste.py é a aplicação que executa a API de exemplo
- my_tc.py é a aplicação que faz os testes automáticos da API de exemplo

## Execute a aplicação teste.py

```bash
uvicorn teste:app --reload
```

## Execute a aplicação my_tc.py

```bash
python3 my_tc.py
```

Caso todos os testes passem, deverá aparecer o seguinte resultado

```bash
...[]
....Tag Nova tag de testes adicionada com sucesso!
.
----------------------------------------------------------------------
Ran 8 tests in 0.250s

OK
```