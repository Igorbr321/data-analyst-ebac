# Não foi corrigido (pegar o valor do selic e do ano na string)
'''noticia = 'Selic vai a 2,75% e supera expectativas é a primeira alta em 6 anos.'''


# Corrigido
noticia = 'Selic vai a 2,75% e supera expectativas é a primeira alta em 6 anos.'
selic = noticia[12:16]
ano = noticia[61]

print(selic)
print(ano)
