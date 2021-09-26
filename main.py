import readhtml
import extractinfo
import csv

f = open('dump', 'w')
writer = csv.writer(f)
teste = extractinfo.extract_UOL()
teste.news_title()
lista_de_titulos = []
for noticia in teste.lista_de_noticias:
	titulo = noticia.contents[0]
	lista_de_titulos.append(titulo)
writer.writerows([lista_de_titulos])
