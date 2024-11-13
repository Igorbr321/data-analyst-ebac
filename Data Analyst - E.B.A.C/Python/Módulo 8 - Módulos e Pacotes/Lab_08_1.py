'''Neste exercício vamos utilizar a base de dados de ações da bolsa de valores dos EUA, a Dow Jones. Para processar os dados, vamos utilizar o pacote `pandas`. A documentação completa por ser 
encontrada neste link.
Todas as bibliotecas já estão instaladas e o arquivo CSV já existe no caminho /data/dow_jones_index.csv
Para tratar os dados, você deve:
Filtrar os dados para utilizar apenas os dados da empresa Coca-cola (coluna stock com o valor KO).
Selecionar os valores de abertura, fechamento, máximo e mínimo das ações da empresa Coca-Cola.
Limpar as colunas, retirando o caractere $ e convertendo os valores de string para float.
Certifique-se que o Dataframe final esteja armazenado na variável df_coke
Obs: No Material de Apoio da aula existe um Jupyter Notebook com explicações e exemplos. Veja o material antes de resolver o exercício.'''


import pandas as pd

df = pd.read_csv('/data/dow_jones_index.csv')

# Crie um Dataframe filtrado, selecionando as linha do dataframe original df em que a coluna stock é igual a KO.
df_coke = df[df['stock'] == 'KO']

# Selecione apenas as colunas de data e valores de ações: ['date', 'open', 'high', 'low', 'close'].
df_coke = df_coke[['date', 'open', 'high', 'low', 'close']]

# Limpe as colunas com o método `apply`, que permite a aplicação de uma função anônima (`lambda`) qualquer. A função `lambda` deve remover o caracter `$` e fazer a conversão do tipo de `str` para `float`.
for col in ['open', 'high', 'low', 'close']:
  df_coke[col] = df_coke[col].apply(lambda value: float(value.split(sep='$')[-1]))

# print the types
print(df_coke.dtypes)

