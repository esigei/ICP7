import nltk
from nltk.stem import WordNetLemmatizer
filetext=open('input.txt','r',encoding='utf-8')
text=filetext.read()
#creating instances of tokens
wordtokens=nltk.word_tokenize(text)#word tokens
lemma=WordNetLemmatizer()#creating an instance of lemmatizer
for w in wordtokens:
    print(w)
    print(lemma.lemmatize(w,'v'))#acts on verbs