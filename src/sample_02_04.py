import re
import unicodedata

text = 'CLEANS ing によりﾃｷｽﾄﾃﾞｰﾀを変換すると　トラブルが少なくなります。'
print('Before:', text)

translation_table = str.maketrans(dict(zip('()!', ' () !')))
#unicodedataのnormalize関数により各文字の表記を統一している
text = unicodedata.normalize('NFKC', text).translate(translation_table)
text = re.sub(r'\s+', '', text)
print('After:',text)

