'''Aplique a função filter na lista de valor_emprestimos_lista para filtrar apenas os valores maiores que zero (os valores negativas são erros na base de dados). Atribua o resulta a variável valor_emprestimos_filtrado.
Transforme o resultado numa lista e armazene em valor_emprestimos_filtrado_lista.
Imprima a variável valor_emprestimos_filtrado_lista.'''

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

valor_emprestimos_lista = list(map(lambda x: float(x['valor_emprestimos']), emprestimos))

# Escreva seu código abaixo

valor_emprestimos_filtrado = filter(lambda x: x > 0, valor_emprestimos_lista)

valor_emprestimos_filtrado_lista = list(valor_emprestimos_filtrado)

print(valor_emprestimos_filtrado_lista)
print(valor_emprestimos_filtrado)
