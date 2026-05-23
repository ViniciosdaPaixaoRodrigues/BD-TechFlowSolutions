from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

usuarios = [{"nome": "jorge", "email": "jorge@example.com", "senha": "Senha123"}]

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
                return redirect(url_for("perfil", email=email))
            
        return "Email ou senha inválidos!"
    
    return render_template("login.html")

@app.route("/usuarios")
def listar_usuarios():
    return render_template("usuarios.html", lista_usuarios=usuarios)

@app.route("/perfil/<email>")
def perfil(email):
    # Busca o usuário na lista pelo e-mail
    usuario_encontrado = next((u for u in usuarios if u['email'] == email), None)

    if usuario_encontrado:
        return render_template('perfil.html', usuario=usuario_encontrado)
    return "Usuário não encontrado", 404

@app.route('/editar_perfil/<email_original>', methods=['POST'])
def editar_perfil(email_original):
    # Pega os novos dados do formulário
    novo_nome = request.form.get('name')
    novo_email = request.form.get('email')
    nova_senha = request.form.get('password')

    # Busca o usuário e atualiza seus dados
    for usuario in usuarios:
        if usuario['email'] == email_original:
            usuario['nome'] = novo_nome
            usuario['email'] = novo_email
            usuario['senha'] = nova_senha
            # Após editar, vai para a lista de usuários para ver a mudança
            return redirect(url_for('listar_usuarios'))
            
    return "Erro ao atualizar perfil", 400

@app.route('/deletar_perfil/<email>', methods=['POST'])
def deletar_perfil(email):
    global usuarios
    # Filtra a lista removendo o usuário com o e-mail correspondente
    usuarios = [u for u in usuarios if u['email'] != email]
    
    # Após deletar, volta para a home
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)