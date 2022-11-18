from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.imdb.com/chart/top").text
soup = BeautifulSoup(html, 'html5lib')

all_todosfilmes = soup.find_all('tr')


for filme in all_todosfilmes:

    importantfilme = filme('td', {'class': 'titleColumn'})
    for importantsdf in importantfilme:
        importantnome = importantsdf.find('a').text

    importnota = filme('td', {'class': 'ratingColumn imdbRating'})
    for importawd in importnota:
        importnota2 = importawd.find('strong').text
        print("Filme: " + importantnome, "Nota: " + importnota2)