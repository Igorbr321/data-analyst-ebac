'''Extraia os valores da coluna "valor_venda" e armazena em uma lista na variável valor_venda.
Siga os passos apresentados pelas linhas de comentários no editor de código.
Imprima a variável valor_venda utilizando a função print()'''

valor_venda = []

with open(file='carros.csv', mode='r', encoding='utf8') as arquivo:
	linha = arquivo.readline()
	linha = arquivo.readline()
	while linha:
		linha_sep = linha.split(sep=',')
		valor_vendas = linha_sep[1] 
		valor_venda.append(valor_vendas)
		linha = arquivo.readline()

	print(valor_venda)