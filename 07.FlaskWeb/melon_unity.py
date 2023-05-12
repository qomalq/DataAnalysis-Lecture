import requests
from bs4 import BeautifulSoup

def melon():
    url = 'https://www.melon.com/chart/'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text, 'html.parser')
    trs = soup.select('#lst50')
    line = []
    for tr in trs:
        rank = tr.select_one('.wrap.t_center').get_text().split('\n')
        img= 'https:' + tr.select_one('td > div > a> img')['src']
        title = tr.select_one('.ellipsis.rank01>span>a').get_text().split('\n')
        artist = tr.select_one('.ellipsis.rank02>span>a').get_text()
        song = tr.select_one('.ellipsis.rank03>a').get_text().split('\n')
        line.append({'순위':rank,'albumImage':img, '곡명':title,'가수':artist,'앨범':song})

    return line