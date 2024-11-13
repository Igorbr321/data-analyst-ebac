'''Complete a função para extrair as palavras de uma linha do arquivo txt em uma lista.
Siga os passos apresentados pelas linhas de comentários no editor de código.'''

import os

def extrai_linha_txt(nome_arquivo: str, numero_linha: int):

	palavras_linha = []

	# leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'. O caminho para o arquivo deve começar com "../../data/".
	with open(file= nome_arquivo, mode = 'r',
	encoding='utf8') as arquivo:
		linha = arquivo.readline()
		cont_linha = 1
	# extraia a linha do arquivo utilizando o parametro 'numero_linha'
		while linha:
			if cont_linha == numero_linha:
				palavras_linha = linha.split(' ')
				break
			linha = arquivo.readline()
			cont_linha += 1
			
	# quebre a linha em palavras com o comando split, note que o separador é um espaço ' '
		
	return palavras_linha

linha10 = extrai_linha_txt(nome_arquivo='musica.txt', numero_linha=5)
print(linha10)
