import re
import unicodedata

#fromは省略を定義
from bs4 import BeautifulSoup

# zipは一時的に配列を結合して扱うための関数
# dict配列を辞書方を作成
# str.maketransは文字列変換を行うための辞書を作成する
translation_table = str.maketrans(dict(zip('()!', ' () ! ')))

# テキストからいらないゴミを取り除いている
def cleanse(text):
    # unicodedata.normalizeは、文字を正規化
    # 上で作成した辞書を用いて実際に変換を行う
    text = unicodedata.normalize('NFKC', text).translate(translation_table)
    # re.sub()では第一引数に正規表現パターン、第二引数に置換先文字列、第三引数に処理対象の文字列を指定する。
    text = re.sub(r'\s+', '', text)
    return text

def scrape(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # stripは引数を削除する（空白含む）
    # not in は指定した配列に引数の内容がない時にTrue
    if len(block.text.strip()) > 0 and \
            block.text.strip()[-1] not in ['。', '！']:
        block.append('<__EOS__>')
    
    # joinは引数（配列）を連結する
    text = '\n'.join([cleanse(block.text.strip())])

        # soup.find_allはタグの取得
    for block in soup.find_all(['p','h1','h2','h3','h4'])
        if len(block.text.strip()) > 0])
    
    title = cleanse(soup.title.text.replace('- Wikipedia', ''))
    
    return text,title
