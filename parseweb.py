import requests, bs4, os
res = requests.get('https://medium.com/topic/programming')

#throws an Exception if 404 or smth
res.raise_for_status()

mediumFeed = bs4.BeautifulSoup(res.text, 'html.parser')

todayHeaders = mediumFeed.select('h3')
print('Today headers are:\n')

for header in todayHeaders:
    text = header.getText()
    print(text)

