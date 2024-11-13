'''Complete a função para extração os valores de valor_venda e que retorne uma lista com os valores.
A função deve ter como parâmetros nome_arquivo e indice_coluna.'''


import os

def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int):
	coluna = []

	# leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'
	# O caminho para o arquivo deve começar com '../../data/'
	with open(file= nome_arquivo, mode='r', encoding='utf8') as arquivo:
		linha = arquivo.readline()
		linha = arquivo.readline()

	# extraia a coluna do arquivo utilizando o parametro 'indice_coluna'
		while linha:
			linha_sep = linha.split(sep=',')
			coluna_desejada = linha_sep[indice_coluna]
			coluna.append(coluna_desejada)
			linha = arquivo.readline()
	

	return coluna

valor_manutencao = extrai_coluna_csv(nome_arquivo='carros.csv', indice_coluna=2)
print(valor_manutencao)

