import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import app
from src.users import usuarios

def teste_home():
    client = app.test_client()
    
    response = client.get("/")
    
    assert response.status_code == 200

def teste_cadastro():
    
    client = app.test_client()
    
    response = client.post(
        "/cadastro",
        data={
            "nome": "Teste",
            "email": "emailteste@example.com",
            "senha": "Senha123"
            }
        )
    
    assert response.status_code == 200
    
    assert b"Usu\xc3\xa1rio cadastrado com sucesso!" in response.data
    
    assert any(
        u["email"] == "emailteste@example.com"
        for u in usuarios
    )

def teste_login():
    client = app.test_client()
    
    response = client.post(
        "/login",
        data = {
            "email": "emailteste@example.com",
            "senha": "Senha123"
        },
        follow_redirects=True
    )
    
    assert response.status_code == 200
    
    assert b"Teste" in response.data