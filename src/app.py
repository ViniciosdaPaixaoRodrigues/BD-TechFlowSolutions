from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route("/")
def home():
    return "Sistema de Login e Cadastro funcionando!"

@app.route("/cadastro", methods=["POST"])
def cadastrar():
    dados = request.json

    usuario = {
        "nome": dados["nome"],
        "email": dados["email"],
        "senha": dados["senha"]
    }

    usuarios.append(usuario)

    return jsonify({
        "mensagem": "Usuário cadastrado com sucesso!"
    }), 201

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(debug=True)