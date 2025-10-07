# starter-code.py
"""
Código inicial para a tarefa de FastAPI
"""
from fastapi import FastAPI

app = FastAPI()

tasks = []

# Adicione os endpoints conforme solicitado no README.md

# Exemplo de endpoint para listar tarefas
@app.get("/tasks")
def list_tasks():
    return tasks

# Implemente os demais endpoints (POST, PUT, DELETE)
