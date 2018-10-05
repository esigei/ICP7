import urllib.request
import bs4 as bs
#url declaration,variable to hold url link
url='https://en.wikipedia.org/wiki/Python_(programming_language)'
#request to parse
source = urllib.request.urlopen(url).read()
#parsing through the web links/html
soup = bs.BeautifulSoup(source,'html.parser')
print(soup.text)
#creating a file to save the text to
myfile=open('input.txt','w',encoding='utf-8')
#converting to the regular text
text=soup.text
#saving contents to the input.text file
myfile.write(text)