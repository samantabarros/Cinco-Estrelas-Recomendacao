from pymongo import MongoClient

from collections import Counter


class Conexao:
    def __init__(self):
        self.conexao = MongoClient('mongodb://localhost:27017')
        #self.conexao = MongoClient("localhost", 27017)


        # Banco recomendacao
        self.db = self.conexao.recomendacao

        # Colecao livros
        self.col_livros = self.db.db_livros

    # Documentos - Sem id
    def lista_livros(self):
        return self.col_livros.find({}, {"Book-Title": "Classical Mythology"})

    