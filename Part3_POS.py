import nltk
filetext=open('input.txt','r')
text=filetext.read()
#creating instances of tokens
wordtokens=nltk.word_tokenize(text)#word tokens
posword=nltk.pos_tag(wordtokens)
print("POS TAGGED :\n",posword)
