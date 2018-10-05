
from nltk import wordpunct_tokenize,pos_tag,ne_chunk
filetext=open('input.txt','r',encoding='utf-8')
text=filetext.read()
print(ne_chunk(pos_tag(wordpunct_tokenize(text))))