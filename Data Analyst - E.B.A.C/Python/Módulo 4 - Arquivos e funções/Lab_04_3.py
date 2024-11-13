'''Complete a função para extração os valores de valor_venda e que retorne uma lista com os valores.
A função deve ter como parâmetros nome_arquivo, indice_coluna, tipo_dado.
O parâmetro tipo_dado deve aceitar como argumento os valores "str" ou "int".'''

import os

def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int, tipo_dado: str):
	coluna = []
	
	# leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'.
    # O caminho para o arquivo deve começar com '../../data/'
	with open(file= nome_arquivo, mode='r', encoding='utf8') as arquivo:
		linha = arquivo.readline()
		linha = arquivo.readline()
	# extraia a coluna do arquivo utilizando o parametro 'indice_coluna'
		while linha:
			linha_sep = linha.split(sep=',')
			coluna_sel = linha_sep[indice_coluna]

			if tipo_dado == 'str':
				coluna.append(str(coluna_sel))
			elif tipo_dado == 'int':
				coluna.append(int(coluna_sel))

			linha = arquivo.readline()
			
	# use a estrutura de decisão if/elif/else para fazer a conversão do tipo de dados utilizando o parametro 'tipo_dado'
	return coluna

valor_manutencao = extrai_coluna_csv(nome_arquivo='carros.csv', indice_coluna=2, tipo_dado= 'str')
print(valor_manutencao)
