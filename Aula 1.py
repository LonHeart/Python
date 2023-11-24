import requests
from bs4 import BeautifulSoup

# Trazer o conteudo do site para o programa
# request vulgo pedir, vai solicitar via google as i
# informações da pesquisa/link.
link = "https://www.google.com/search?client=opera-gx&q=cotação+do+dolar"
# Headers explicação la embaixo
# É um dicionario python é como uma lista que armazena dados mas em formato
# key:value "nome":"ana" "idade":"25"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"
           }
requisicao = requests.get(link, headers=headers)

# se o response der [200] deu certo
#  print(requisicao)
# trazendo o codigo html por traz do request, todas as info da pagina
#  print(requisicao.text)

# html.parser(leitor de html), BeutifulSoup organiza o codigo e
# lê de maneira facilitada
site = BeautifulSoup(requisicao.text, "html.parser")
# traz o site bonito em html.
#  print(site.prettify()) 
#  print(site.title) titulo do site

# salve em variaveis o que desejas buscar
titulo = site.find("title")
# sempre utilize em find("TAG HTML") o tag da html em si
print(titulo)
# input generico, mas como pegar uma tag especifica?
pesquisa = site.find("textarea")
print(pesquisa)
# busca todas as tags com o input no site e armazena em uma lista
#  pesquisa_Tudo = site.find_all("textarea")
#  print(pesquisa_Tudo[0])
# O BeutifulSoup serve apenas para tratagem de dados, raspagem de dados
# ele traz os dados para o programa e os trata, em nenhum momento há
# interação do programa. Excelente em sites estáticos. e so funciona para
# eles. Sites dinamicos não é possivel, para isso será necessario outra
# ferramenta como o SELLENIUM.

# Alguns sites podem bloquear o processo de raspagem de dados.
# Uso necessario do class_ pois o class é do proprio python para criar
# busca de mais de um elemento é realizado dessa forma
#  pesquisa2 = site.find("textarea", class_="Tg7LZd")
#  print(pesquisa2)

print(pesquisa["value"])

# pegar um elemento chave especifico pós formatação do headers:
# o headers transformas os valores chaves como variaveis em uma lista,
# mas podem ser identificadas por suas caracteristicas especificas.

cotacao = site.find("span", class_="DFlfde SwHCTb")
print(cotacao["data-value"])

# pegar o texto contido dentro de uma tag

print(cotacao.get_text())




# Requisitar a versão do navegador para o google
# inspecionar elemento>network>qualquer_um>headers_la_embaixo>user-agent
# é necessario trazer a versão do navegador para que o codigo interprete
# as informações não como python mas como informações do proprio navegador
# html.