from lib.db import Conexao
from math import sqrt
import pymongo



# Dados do Mongo
con = Conexao()
dadosMongo = con.lista_livros()

ratingsItens = {}
ratingsUsuarios = {}

for dados in dadosMongo:
	for k, v in dados.items():
		ratingsItens[k] = v
print(ratingsItens)


# Dados estaticos - Apenas para testes
ratings = {'Ana': 
		{'Um dia': 2.5, 
		 'Rapido e Devagar': 3.5,
		 'Amanhecer': 3.0, 
		 'Orgulho e Preconceito': 3.5, 
		 'O Hobbit': 2.5,
		 'O Código da Vinci': 3.0},
	 
	  'Marcos': 
		{'Um dia': 3.0, 
		 'Rapido e Devagar': 3.5, 
		 'Amanhecer': 1.5, 
		 'Orgulho e Preconceito': 5.0, 
		 'O Código da Vinci': 3.0, 
		 'O Hobbit': 3.5}, 

	  'Pedro': 
	    {'Um dia': 2.5, 
		 'Rapido e Devagar': 3.0,
		 'Orgulho e Preconceito': 3.5, 
		 'O Código da Vinci': 4.0},
			 
	  'Claudia': 
		{'Rapido e Devagar': 3.5, 
		 'Amanhecer': 3.0,
		 'O Código da Vinci': 4.5, 
		 'Orgulho e Preconceito': 4.0, 
		 'O Hobbit': 2.5},
				 
	  'Adriano': 
		{'Um dia': 3.0, 
		 'Rapido e Devagar': 4.0, 
		 'Amanhecer': 2.0, 
		 'Orgulho e Preconceito': 3.0, 
		 'O Código da Vinci': 3.0,
		 'O Hobbit': 2.0}, 

	  'Janaina': 
	     {'Um dia': 3.0, 
	      'Rapido e Devagar': 4.0,
	      'O Código da Vinci': 3.0, 
	      'Orgulho e Preconceito': 5.0, 
	      'O Hobbit': 3.5},
			  
	  'Adriano': 
	    {'Rapido e Devagar':4.5,
             'O Hobbit':1.0,
	     'Orgulho e Preconceito':4.0},
    'Luana':
              {'Harry Potter e a Criança Amaldiçoada':4.0}
}

# Distancia euclidiana
def euclidiana(base, book1, book2):
    si = {} # Criando um dicionário vazio para armazenar as similaridades

    # Listar todos os usuarios do book 1
    for item in base[book1]:

        # Verificar se os usuarios do book 1 viram o book 2
        if item in base[book2]:
            si[item] = 1 # Atribui o valor 1 a nossa lista de similaridades

    if len(si) == 0:
        return 0

    # Retorna a nota
    soma = sum([pow(base[book1][item] - base[book2][item], 2)

    # A mesma comparação feita em cima, se o usuario viu o book1 e o book2
    for item in base[book1] if item in base[book2]])
    return 1/(1+sqrt(soma)) # Retorna o calculo da porcentagem de similaridade entre os 2 books

def getSimilares(base, book):
    # Compara a similaridade do book com todos os outros
    similaridade = [(euclidiana(base, book, outro), outro)
                    for outro in base if outro != book]
    similaridade.reverse() # Ordena decrescente
    return similaridade[0:30] # 30 primeiros registros

# Função Itens similares
def calculaItensSimilares(base=ratingsItens):
    result = {}
    for i in base:
        notas = getSimilares(base,  i)
        result[i] = notas
    return result
    print()

# Salva os dados na variavel
itensSimilares = calculaItensSimilares(ratingsItens)

# Função recomendar
def getRecomendacoesItens(baseUsuario=ratings, similaridadeItens=itensSimilares, id=0):
    notasUsuario = baseUsuario[id]
    notas = {}
    totalSimilaridades = {}
    
    for (item, nota) in notasUsuario.items():
        for (similaridade, i2) in similaridadeItens[item]:
            if i2 in notasUsuario: continue
            notas.setdefault(i2, 0)
            notas[i2] += similaridade * nota
            totalSimilaridades.setdefault(i2, 0)
            totalSimilaridades[i2] += similaridade
    rankings = [(score/totalSimilaridades[item], item) for item, score in notas.items()]
    rankings.sort()
    rankings.reverse()
    return dict(rankings).values()
