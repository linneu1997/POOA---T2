from bs4 import BeautifulSoup
import readhtml

class extract:
	def news_title():
		return

class extract_UOL:
	def news_title(self):
		pagina = readhtml.read_UOL()
		pagina.get_URL()
		self.lista_de_noticias = pagina.conteudo.find_all("h1", class_="titulo color2")
		self.lista_de_noticias.extend(pagina.conteudo.find_all("h2", class_="titulo color2"))
		
