import urllib.request
import cchardet
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC'
    with urllib.request.urlopen(url) as res:
        byte = res.read()
        #文字コードの変更
        html = byte.decode(cchardet.detect(byte)['encoding'])
        #解析できるように
        soup = BeautifulSoup(html,'html.parser')
        
        title = soup.head.title
        
        print('[title]:', title.text, '\n')
        
        for block in soup.find_all(['p','h1','h2','h3','h4']):
            print('[block]:', block.text)
            