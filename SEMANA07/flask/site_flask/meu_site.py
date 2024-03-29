from flask import Flask, render_template, request
from random import randint
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    variavel = "Game: Adivinheo número correto"

    if request.method == "GET":
        return render_template("index.html", variavel=variavel)
    
    else:
        numero = randint(0, 10)
        palpite = int(request.form.get("name"))

        if numero == palpite:
            return f"<h1>Parabéns! Você ganhou!</h1>"
        else:
            return f"Você perdeu!"
    

@app.route('/about')
def about():
    return '<p>About</p>'

@app.route('/<string:nome>')
def page_not_found(nome):
    variavel = f'<h1>Página: {nome.upper()} não encontrada.</h1>'
    return render_template("error.html", variavel=variavel)