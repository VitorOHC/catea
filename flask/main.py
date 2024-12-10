from flask import Flask

app = Flask(__name__)


@app.route("/")
def ola_mundo():
    return "Oii tudo bem?"

@app.route("/sobre")
def pagina_sobre():
    return """
        <b> CaTEA /b>: 

app.run(debug=True)

