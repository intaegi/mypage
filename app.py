import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://intaegi111:test@cluster0.lh44oge.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

URL = "https://www.billboard-japan.com/charts/detail?a=hot100"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#content2 > div > div.leftBox > table > tbody > tr')

for m in musics:
    rank = m.select_one('td > span').text
    title = m.select_one('p.musuc_title').text.strip()
    artist = m.select_one('p.artist_name').text.strip()
    print(rank, title, artist)