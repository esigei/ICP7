import nltk
from nltk.stem import PorterStemmer
filetext=open('input.txt','r',encoding='utf-8')
text=filetext.read()
#creating instances of tokens
wordtokens=nltk.word_tokenize(text)#word tokens
stemmer=PorterStemmer()
print("STEMMED WORDS:")
for w in wordtokens:
    print(w)
    print(stemmer.stem(w))