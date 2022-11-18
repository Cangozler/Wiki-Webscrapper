import requests
import bs4
search=input("What u searched ?")

res = requests.get('https://en.wikipedia.org/wiki/'+search)
soup = bs4.BeautifulSoup(res.text,'lxml')

links = soup.find_all('a', href=True)

for link in links:
    print(link['href'])