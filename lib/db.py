from pymongo import MongoClient

class Conexao:
    def __init__(self):
        #self.conexao = MongoClient('mongodb://localhost:27017')
        self.conexao = MongoClient("localhost", 27017)
        #print(conexao.list_databases_names())


        # Banco recomendacao
        self.db = self.conexao.recomendacao

        # Colecao livros
        self.col_livros = self.db.db_livros

    # Documentos - Sem id
    def lista_livros(self):
        return self.col_livros.find({}, {"_id":0})
