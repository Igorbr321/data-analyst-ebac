'''Para visualizar os dados, vamos utilizar o pacote seaborn na versão 0.13.2. A documentação completa por ser encontrada neste https://seaborn.pydata.org/.
Todas as bibliotecas necessárias já estão instaladas. O arquivo /data/df_coke.csv contém o resultado da Parte 1 deste exercício, com os dados já filtrados e convertidos para o tipo float.
Crie um gráfico de linha (sns.lineplot()) que demonstre a visualização da abertura das ações (coluna 'open') ao longo do tempo.
Obs: para visualizar seu gráfico, utilize o comando plt.show().'''

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df_coke = pd.read_csv('/data/df_coke.csv', index_col=0)

fig, axs = plt.subplots(1, figsize=(8, 8))

# Insira se código na linha abaixo. Veja a dica para resolver esse exercício
plot = sns.lineplot(x="date", y="open", data=df_coke)
_ = plot.set_xticklabels(labels=df_coke['date'], rotation=90)

plot.tick_params(axis='x', labelrotation = 45)

plt.show()

