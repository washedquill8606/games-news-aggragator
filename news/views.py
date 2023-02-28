from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


#Levelup news
lu_r = requests.get("https://www.levelup.com/noticias")
lu_soup = BeautifulSoup(lu_r.content, 'html5lib')

lu_news = []
lu_as = []
lu_list = []
lu_dict = {}

#for texts
lu_headings = lu_soup.find_all('h4', {'class' : 'elementHeader'})

for lu_heading in lu_headings[:10]:
    lu_news.append(lu_heading.get_text(strip=True))

#for links

h4_links = [h4.a for h4 in lu_soup.find_all('h4', {'class' : 'elementHeader'})]
for h4_link in h4_links:
    href = h4_link.get('href')
    href_str = 'https://levelup.com' + href
    lu_as.append(href_str)
        # href_cpd = ""f"{href_str}""" (this is for passing the string with double quotes)

for x, y in zip(lu_news,lu_as):
    lu_list += [x,y]
    lu_dict = {
        'title' : x,
        'link' : y,
    }

#Eurogamer news
eu_r = requests.get("https://www.eurogamer.es/news")
eu_soup = BeautifulSoup(eu_r.content, 'html5lib')

eu_news = []
eu_as = []

#for texts

eu_headings = eu_soup.find_all('p', {'class':'title'})

for eu_heading in eu_headings[:10]:
    eu_news.append(eu_heading.get_text(strip=True))

#for links

h4eu_links = [h4.a for h4 in eu_soup.find_all('p', {'class' : 'title'})]
for h4eu_link in h4eu_links:
    eu_as.append(h4eu_link['href'])

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'lu_news' : lu_news,
        'lu_as' : lu_as,
        'lu_dict' : lu_dict,
        'eu_news' : eu_news,
        'eu_as' : eu_as,
    })