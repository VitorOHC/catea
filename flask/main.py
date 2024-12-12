from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def ola_mundo():
    return "Oii tudo bem?"

@app.route('/cadastro', methods=['POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        # Aqui você pode adicionar a lógica para salvar os dados em um banco de dados, por exemplo
        print(f"Cadastro realizado! Nome: {nome}, Email: {email}")
        return redirect(url_for('index'))  # Redireciona de volta para o formulário após o cadastro

if __name__ == '__main__':
app.run(debug=True)

