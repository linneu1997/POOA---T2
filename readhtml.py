import requests
from bs4 import BeautifulSoup

#classe abstrata base para realizar a leitura das URL:
class read_URL(object):
	def get_URL():
		return

#classe para ler a página da UOL:
class read_UOL(read_URL):
	def get_URL(self):
		url = 'https://www.uol.com.br/'
		pagina = requests.get(url)
		self.conteudo = BeautifulSoup(pagina.text, 'html.parser')
