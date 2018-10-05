
import nltk
from nltk.stem import WordNetLemmatizer
filetext=open('input.txt','r',encoding='utf-8')
text=filetext.read()
#creating instances of tokens
wordtokens=nltk.word_tokenize(text)#word tokens
sentokens=nltk.sent_tokenize(text)#tokenize each sentence in text
print("Tokenized words: ")
#printing tokenized words in text
for w in wordtokens:
    print(w)
#printing tokenized sentences in text
print("Tokenized Sentences:")
for s in sentokens:
    print(s)
