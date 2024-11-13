# Não corrigido
'''def valor_total_emprestimo(valor: float, quantidade: int) -> float:
	return valor * quantidade

emprestimos = []

with open(file='/data/credito.csv', mode='r', encoding='utf8') as fp:
	fp.readline() # cabeçalho
	linha = fp.readline()
	while linha:
		linha_emprestimo = {}
		linha_elementos = linha.strip().split(sep=',')
		linha_emprestimo['id_vendedor'] = linha_elementos[0]
		linha_emprestimo['valor_emprestimos'] = float(linha_elementos[1])
		linha_emprestimo['quantidade_emprestimos'] = int(linha_elementos[2])
		linha_emprestimo['data'] = linha_elementos[3]
		emprestimos.append(linha_emprestimo)
		linha = fp.readline()
	
emprestimos_total = []
for emprestimo in emprestimos:
	valor_total = valor_total_emprestimo(valor=emprestimo['valor_emprestimos'], quantidade=emprestimo['quantidade_emprestimos'])
	emprestimos_total.append({emprestimo['id_vendedor']: valor_total})
	
for emprestimo_total in emprestimos_total:
	print(emprestimo_total)'''


# Corrigido
def valor_total_emprestimo(valor: float, quantidade: int) -> float:
	return valor * quantidade

emprestimos = []

with open(file='/data/credito.csv', mode='r', encoding='utf8') as fp:
	fp.readline() # cabeçalho
	linha = fp.readline()

	while linha: 
		linha_emprestimo = {}
		linha_elementos = linha.strip().split(sep=',')
		linha_emprestimo['id_vendedor'] = linha_elementos[0]

		try:
			linha_emprestimo['valor_emprestimos'] = float(linha_elementos[1])
		except ValueError as e:
			error = e
			linha_emprestimo['valor_emprestimos'] = float(linha_elementos[1].replace('"', ''))

		linha_emprestimo['quantidade_emprestimos'] = int(linha_elementos[2])
		linha_emprestimo['data'] = linha_elementos[3]
		emprestimos.append(linha_emprestimo)
		linha = fp.readline()

emprestimos_total = []
for emprestimo in emprestimos:
	valor_total = valor_total_emprestimo(valor=emprestimo['valor_emprestimos'], quantidade=emprestimo['quantidade_emprestimos'])
	emprestimos_total.append({emprestimo['id_vendedor']: valor_total})
	
for emprestimo_total in emprestimos_total:
	print(emprestimo_total)