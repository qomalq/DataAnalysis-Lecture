import requests
from urllib.parse import quote
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm
from datetime import datetime

def gene():
    url = 'https://www.genie.co.kr/chart/top200'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text, 'html.parser')
    trs = soup.select('tr.list')
    now = datetime.now()
    ymd = now.strftime('%Y%m%d')    
    hh = now.strftime('%H')         
    lines = []
    base_url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=Y'
    for page in tqdm(range(1, 5)):
        url = f'{base_url}&ymd={ymd}&hh={hh}&pg={page}'
        result = requests.get(url, headers=header)
        soup = BeautifulSoup(result.text, 'html.parser')
        trs = soup.select('tr.list')
        for tr in trs:
            rank = tr.select_one('.number').get_text().split('\n')[0].strip()
            img = 'https:' + tr.select_one('.cover > img')['src']
            title = tr.select_one('.title.ellipsis').get_text().split('\n')[-1].strip()
            artist = tr.select_one('.artist.ellipsis').string.strip()
            album = tr.select_one('.albumtitle.ellipsis').text.strip()
            lines.append({'rank':rank, 'img':img, 'title':title, 'artist':artist, 'album':album})
    return lines