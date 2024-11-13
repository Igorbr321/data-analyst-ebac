'''Crie a classe `ArquivoCSV`. Ela deve extender (herdar) a classe ArquivoTexto para reaproveitar os seus atributos (self.arquivo e self.conteudo). Além disso, adicione o seguinte atributo:
self.colunas: Atributo do tipo `list` onde os elementos são os nome das colunas;
A classe também deve conter o seguinte método:
self.extrair_nome_colunas: Método que retorna o nome das colunas do arquivo.
extrair_coluna: Método que recebe como parâmetro o indice da coluna e retorna o valor em questão. Considere a primeira coluna como número 1.'''


import sys
sys.path.insert(0, '/data')
from Lab_06_2 import ArquivoTexto

class ArquivoCSV(ArquivoTexto):
    def __init__(self, arquivo: str):
        super().__init__(arquivo=arquivo)
        self.colunas = self.extrair_nome_colunas()

    def extrair_nome_colunas(self):
        if self.conteudo:
            return self.conteudo[0].strip().split(',')
        return []

    def extrair_coluna(self, indice_coluna: int):
        if not (1 <= indice_coluna <= len(self.colunas)):
            return 'Índice de coluna fora do intervalo.'

        coluna_index = indice_coluna - 1
        coluna_valores = [linha.strip().split(',')[coluna_index] for linha in self.conteudo[1:]]
        return coluna_valores