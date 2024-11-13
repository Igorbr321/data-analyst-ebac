'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada.

Lembre-se de que você já conhece o nível intermediário da linguagem de programação Python, além de conhecer como automatizar dados por meio da programação funcional e programação orientada a objetos. '''


class Tabuada:
    def __init__(self, numero: int):
        self.numero = numero

    def apresentar(self):
        for i in range(1, 11):
            mult = i * self.numero
            print('{} x {} = {}'.format(self.numero, i, mult))


# Armazena a váriavel que o usuário digita
num = int(input('Digite o número da tabuada desejada: '))

# Armazenando a variável num dentro da class
tabuada = Tabuada(num)

# Utilizando a variável tabuada e chamando a função apresentar da class Tabuada, para fazer as multiplicações
tabuada.apresentar()
