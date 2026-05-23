from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

usuarios = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":

        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        
        # Verificar se o email já existe.
        for usuario in usuarios:
            if usuario["email"] == email:

                return "Este email já está cadastrado!"
        
        novo_usuario = {"nome": nome, "email": email, "senha": senha}
        usuarios.append(novo_usuario)

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

@app.route("/usuarios")
def listar_usuarios():
    return render_template("usuarios.html", lista_usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)