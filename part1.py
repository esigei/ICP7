
import urllib.request
import bs4 as bs
url='https://en.wikipedia.org/wiki/Python_(programming_language)'
#request to parse
source = urllib.request.urlopen(url).read()
#parsing through the web links/html
soup = bs.BeautifulSoup(source,'html.parser')
print(soup.text)

