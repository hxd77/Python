import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = 'https://www.xbqg777.com/49936'
    try:
        req = requests.get(url=target)
        req.encoding = 'utf-8'
        html = req.text
        bs = BeautifulSoup(html, 'lxml')
        chapters=bs.find('a',{'class':'chapter container'})
        #chapters=chapters.find_all('a')
        for chapter in chapters:
            print(chapter)
        texts = bs.find('article', id='article')
        #print(texts)
        #print(texts.text.strip().split('\xa0' * 4))
    except requests.exceptions.ConnectionError as e:
        print(f"连接错误: {e}")
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")