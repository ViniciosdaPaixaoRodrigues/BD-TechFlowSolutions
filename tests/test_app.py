import sys
import os

# Necessário essa linha para que o sistema localize o arquivo de testes.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import app
from src.users import usuarios

def test_home():
    # Necessário para garantir que os testes não deem falso-positivo.
    usuarios.clear()

    print("\nTeste: Acessar página principal: ", end="")
    client = app.test_client()
    
    response = client.get("/")
    
    if response.status_code == 200:
        print("\033[32mSucesso\033[0m")
    else:
        print("\033[31mFracasso\033[0m\n")
    
    assert response.status_code == 200
    
def test_cadastro():
    # Necessário para garantir que os testes não deem falso-positivo.
    usuarios.clear()
    
    print("\nTentativa de Cadastro: Usuário 'Teste'.\nResultado: ", end="")
    
    client = app.test_client()
    
    response = client.post(
        "/cadastro",
        data={
            "nome": "Teste",
            "email": "emailteste@example.com",
            "senha": "Senha123"
            }
        )
    
    if response.status_code == 200:
        print("\033[32mSucesso\033[0m")
    else:
        print("\033[31mFracasso\n\033[0m")
    
    assert response.status_code == 200
    
    assert b"Usu\xc3\xa1rio cadastrado com sucesso!" in response.data
    
    assert any(
        u["email"] == "emailteste@example.com"
        for u in usuarios
    )

def test_login():
    
    print("\nTentativa de Login: Usuário 'Teste'.")
    
    client = app.test_client()
    
    response = client.post(
        "/login",
        data = {
            "email": "emailteste@example.com",
            "senha": "Senha123"
        },
        follow_redirects=True
    )
    
    if response.status_code == 200:
        print("\033[32mSucesso\033[0m")
    else:
        print("\033[31mFracasso\033[0m")
    
    assert response.status_code == 200
    
    assert b"Teste" in response.data
    
def test_loginInvalido():
    # Necessário para garantir que os testes não deem falso-positivo.
    
    print("\nTentativa de Login INVÁLIDA: Usuário 'Teste'.")
    
    client = app.test_client()
    
    response = client.post(
        "/login",
        data = {
            "email": "emailteste@example.com",
            "senha": "Senha13"
        },
        follow_redirects=True
    )
    
    if response.status_code == 401:
        print("\033[32mSucesso\033[0m")
    else:
        print("\033[31mFracasso\033[0m")
    
    assert response.status_code == 401
    
    assert b"Email ou senha inv\xc3\xa1lidos!" in response.data