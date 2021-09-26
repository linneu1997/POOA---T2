#Classes relaconadas a extração de informação de arquivos HTML (parsing).
from bs4 import BeautifulSoup
import readhtml

#Classe base para extrair informações:
class extract:
	def news_title():
		return

#Classe que extrai informações da página da UOL:
class extract_UOL:
	#método que extrai os títulos das notícias:
	def news_title(self):
		pagina = readhtml.read_UOL()
		pagina.get_URL()
		#as noticias da UOL tem seus titulos pertencentes às classes "titulo color2", com as tags "h1" e "h2".
		self.lista_de_noticias = pagina.conteudo.find_all("h1", class_="titulo color2")
		self.lista_de_noticias.extend(pagina.conteudo.find_all("h2", class_="titulo color2"))
