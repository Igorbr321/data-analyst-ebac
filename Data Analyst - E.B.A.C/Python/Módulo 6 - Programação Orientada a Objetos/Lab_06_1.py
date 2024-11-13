'''Crie a classe ArquivoTexto. Ela deve conter os seguintes atributos:
self.arquivo: Atributo do tipo str com o nome do arquivo;
self.conteudo: Atributo do tipo list onde cada elemento é uma linha do arquivo;
A classe também deve conter o seguinte método:
self.extrair_conteudo: Método que realiza a leitura do arquivo e retorna o conteúdo.
self.extrair_linha: Método que recebe como parâmetro o número da linha e retorna a linha do conteúdo. Considere a primeira linha como número 1.'''

class ArquivoTexto(object):
	def __init__(self, arquivo: str):
		self.arquivo = arquivo
		self.conteudo = self.extrair_conteudo()
		
	def extrair_conteudo(self):
		# Para acessar o arquivo você deve utilizar o caminho: "/data/"
		conteudo = None
		with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
			conteudo = arquivo.readlines()
		return conteudo	

	def extrair_linha(self, numero_linha: int):
		while True:
			try:
				return self.conteudo[numero_linha - 1].strip()
			except IndexError:	
				return 'Número de linha fora do intervalo.'
					
			

musica = ArquivoTexto('musica.txt')
print(musica.conteudo)
