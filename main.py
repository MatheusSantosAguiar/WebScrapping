from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.imdb.com/chart/top").text
soup = BeautifulSoup(html, 'html5lib')
todos_filmes = soup.find_all('tr')


def extrai_nome_filmes():
    for filme in todos_filmes:
        filme_nome = filme('td', {'class': 'titleColumn'})
    for filme_dois in filme_nome:
        filme_nome1 = filme_dois.find('a').text
    return filme_nome1

def extrai_nota_filmes():
    for filme in todos_filmes:
        filme_nota = filme('td', {'class': 'ratingColumn imdbRating'})
    for importa_nota in filme_nota:
        filme_nota1 = importa_nota.find('strong').text

    return filme_nota1

def extrai_data_filmes():
    for filme in todos_filmes:
        filme_ano = filme('td', {'class': 'titleColumn'})
    for importa_ano in filme_ano:
        filme_ano1 = importa_ano.find('span').text

    return filme_ano1



if __name__ == '__main__':

    nomefilmes = extrai_nome_filmes()
    datafilmes = extrai_data_filmes()
    notafilmes = extrai_nota_filmes()

    with open("Top 250 Filme.txt", 'w') as file:
        for filme in todos_filmes:

            for filme_dois in filme('td', {'class': 'titleColumn'}):
                file.write(" Nome:" + filme_dois.find('a').text + "\n")

            for importa_ano in filme('td', {'class': 'titleColumn'}):
                file.write(" Ano:" + importa_ano.find('span').text+ "\n")

            for importa_nota in filme('td', {'class': 'ratingColumn imdbRating'}):
                file.write(" Nota:" + importa_nota.find('strong').text+ "\n")