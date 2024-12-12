from flask import Flask

from rotas.cadastro import home_route


app = Flask(__name__)

app.register_blueprint(home_route)

app.run(debug=True)

