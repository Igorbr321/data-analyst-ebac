'''Crie uma lista chamada filmes com o nome dos 10 primeiros filmes mais bem avaliados no site no IMDB utilizando a seguinte estrutura: filmes = [...]
Simule a movimentação do ranking. Para isso, utilize os métodos insert e pop para trocar a posição do primeiro e do segundo filme da lista.'''

# Corrigido
filmes = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "The Godfather Part II", "12 Angry Men", "Schindler's List", "The Lord of the Rings: The Return of the King", "Pulp Fiction", "The Lord of the Rings: The Fellowship of the Ring", "The Good, the Bad and the Ugly"]

filmes.pop(0)
filmes.insert(1, 'The Shawshank Redemption')

print(filmes)