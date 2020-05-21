import requests, bs4 
res = requests.get('https://howlongtobeat.com/game?id=57686')
res.raise_for_status()
timeSoup = bs4.BeautifulSoup(res.text, "html.parser")
# print(timeSoup)
elms = timeSoup.select('li.short.time_100')
print(elms)