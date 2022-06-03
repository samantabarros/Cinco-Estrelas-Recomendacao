from flask import Flask, render_template, json, request
from lib import recomendacao
from datetime import datetime
from lib.db import Conexao

app = Flask(__name__)

_usuario = 'User-ID'

@app.route('/')
def main():
	return render_template('index.html')

@app.context_processor
def recomenda():
	return dict(lista_livros=recomendacao.getRecomendacoesItens(usuario= _usuario))

@app.context_processor
def retorna_dados():
	_data = str(datetime.today().year)
	return dict(data=_data, usuario =_usuario)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

