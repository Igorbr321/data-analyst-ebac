'''Aplique a função map na lista de emprestimos para extrair os valores da chave valor_emprestimos na variável valor_emprestimos_map.
Ainda na função map, faça também a conversão de str para float.
Tranforme valor_emprestimos_map em lista e armazene na variável valor_emprestimos_lista.
Imprima a variável valor_emprestimos_lista.'''

emprestimos = []
with open(file='credito.csv', mode='r', encoding='utf8') as fp:
    fp.readline() # cabeçalho
    linha = fp.readline()
    while linha:
        linha_emprestimo = {}
        linha_elementos = linha.strip().split(sep=',')
        if len(linha_elementos) == 4:  # Verifica se a linha tem o número correto de elementos
            linha_emprestimo['id_vendedor'] = linha_elementos[0]
            linha_emprestimo['valor_emprestimos'] = linha_elementos[1]
            linha_emprestimo['quantidade_emprestimos'] = linha_elementos[2]
            linha_emprestimo['data'] = linha_elementos[3]
            emprestimos.append(linha_emprestimo)
        linha = fp.readline()

# Convertendo valores dos empréstimos para float e criando uma lista
valor_emprestimos_map = map(lambda x: float(x['valor_emprestimos']), emprestimos)
valor_emprestimos_lista = list(valor_emprestimos_map)

print(valor_emprestimos_lista)




