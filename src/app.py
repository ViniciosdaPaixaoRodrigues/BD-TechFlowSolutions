from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

usuarios = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":

        dados = request.form

        usuario = {
            "nome": dados["nome"],
            "email": dados["email"],
            "senha": dados["senha"]
        }

        usuarios.append(usuario)

        return "Usuário cadastrado com sucesso!"

    return render_template("cadastro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
        email = request.form["email"]
        senha = request.form["senha"]
        
        for usuario in usuarios:
            
            if usuario["email"] == email and usuario["senha"] == senha:
                return f"Bem vindo, {usuario["nome"]}!"
            
        return "Email ou senha inválidos!"
    
    return render_template("login.html")

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(debug=True)