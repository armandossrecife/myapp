#!/bin/bash
echo "Executa a aplicação frontend principal"
flask --app main --debug run --host=0.0.0.0 --port=5000