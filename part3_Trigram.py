import nltk
from nltk.util import ngrams
filetext=open('input.txt','r',encoding='utf-8')
text=filetext.read()
#creating instances of tokens
wordtokens=nltk.word_tokenize(text)#word tokens
trig = []
index = 2
while index < len(wordtokens) - 2:
    trig.append((wordtokens[index], wordtokens[index+1], wordtokens[index+2]))
    index += 2
#print (trig)
tri=nltk.ngrams(wordtokens,3)
print(*tri)