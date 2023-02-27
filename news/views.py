from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


#Levelup news
lu_r = requests.get("https://www.levelup.com/noticias")
lu_soup = BeautifulSoup(lu_r.content, 'html5lib')

lu_news = []
lu_as = []
lu_headings = lu_soup.find_all('h4')

for tags in lu_headings:
    aTags = tags.find_all('a', {'class':'rC'})
    for aTag in aTags:
        href = aTag.get('href')
        if href is not None:
            href_str = 'https://levelup.com' + href
            # href_cpd = ""f"{href_str}""" (this is for passing the string with double quotes)
            lu_as.append(aTag.get_text(strip=True)) #href_str

for lu_heading in lu_headings[:10]:
    lu_news.append(lu_heading.get_text(strip=True))


#Eurogamer news
eu_r = requests.get("https://www.eurogamer.es/news")
eu_soup = BeautifulSoup(eu_r.content, 'html5lib')

eu_news = []
eu_headings = eu_soup.find_all('div', {'class':'summary'})

for eu_heading in eu_headings[:10]:
    eu_news.append(eu_heading.get_text(strip=True))

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'lu_news' : lu_news,
        'lu_as' : lu_as,
        'eu_news' : eu_news,
    })