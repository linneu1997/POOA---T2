import readhtml
import extractinfo
import csv

print("Deseja imprimir as noticias de qual pagina?")
escolha = int(input("1 - UOL  2 - outra\n"))

#salva os titulos das notícias da UOL em um arquivo CSV
if escolha == 1:
	#Os titulos são salvos no arquivo CSV "news_dump":
	file = open('news_dump', 'w')
	writer = csv.writer(file)
	#cria o objeto "manchetes" com o titulo das notícias do site da UOL:
	manchetes = extractinfo.extract_UOL()
	manchetes.news_title()
	for noticia in manchetes.lista_de_noticias:
		#mantém apenas o titulo da notícia:
		titulo = noticia.contents[0]
		#formata a lista de títulos e a salva em um arquivo CSV
		writer.writerows([[titulo]])

#demonstração de como o programa pode ser expandido para incluir mais páginas:
if escolha == 2:
	print("Novas páginas a serem adicionadas futuramente\n")
