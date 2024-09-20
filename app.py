from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conteudo-extra')
def conteudo_extra():
    return "<p>Este é o conteúdo extra carregado dinamicamente com HTMX!</p>"

@app.route('/dica')
def dica():
    dicas = [
        "Mantenha-se positivo!",
        "Trabalhe duro e não desista!",
        "Aprenda algo novo todos os dias!",
        "A gratidão transforma o que temos em suficiente."
    ]
    return random.choice(dicas)

@app.route('/enviar-feedback', methods=['POST'])
def enviar_feedback():
    nome = request.form.get('nome')
    mensagem = request.form.get('mensagem')
    return f"<p>Obrigado, {nome}! Seu feedback foi enviado: {mensagem}</p>"

@app.route('/calcular-soma')
def calcular_soma():
    numero1 = request.args.get('numero1', 0)
    numero2 = request.args.get('numero2', 0)
    
    # Converta os valores para inteiros e calcule a soma
    soma = int(numero1) + int(numero2)
    return f"<p>A soma é: {soma}</p>"


if __name__ == '__main__':
    app.run(debug=True)
