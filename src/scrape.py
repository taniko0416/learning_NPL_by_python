import re
import unicodedata

#fromは省略を定義
from bs4 import BeautifulSoup

#dict配列を辞書方を作成
translation_table = str.maketrans(dict(zip('()!', ' () !')))

def cleanse(text):
    text = unicodedata.normalize('NFKC', text).translate(translation_table)
    text = re.sub(r'\s+', '', text)
    return text

def scrape(html):
    soup = BeautifulSoup(html, 'html.parser')
    if len(block.text.strip()) > 0 and \
            block.text.strip()[-1] not in ['。', '！']:
        block.append('<__EOS__>')
    text = '\n'.join([cleanse(block.text.strip())])
        for block in soup.find_all(['p','h1','h2','h3','h4'])
        if len(block.text.strip()) > 0])
    
    title = cleanse(soup.title.text.replace('- Wikipedia', ''))
    return text,title
