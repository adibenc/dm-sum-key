from bs4 import BeautifulSoup
from pprint import pprint
import re
import requests as req

def toBs4(fname):
    content = open(fname, "r").read()
    return BeautifulSoup(content, 'html.parser')

class AppBs():
    content = ""
    soup = None

    def __init__(self):
        pass
    
    def setSoup(self, s):
        self.soup = s

        return self

    def allLink(self):
        return self.soup.find_all('a')
        
    def allArticle(self):
        return self.soup.find_all('article')

def getSave(url, alias=None):
    r = req.get(url)
    print(r.text)

    fname = "x"
    f1 = open("{}-rawhtml.html".format(fname), "w").write(r.text)

    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.find_all('article')
    article = ""

    for a in articles:
        article += a

    f2 = open("{}-raw.txt".format(fname), "w").write(article)

    return

url = "https://tirto.id/pertanian-ramah-lingkungan-bYbv"
getSave(url, alias=None)

fname = "./dummy/site_tirto.id pertanian at DuckDuckGo.html"
# soup = toBs4(fname)

# print(soup)
# ass = soup.find_all('a', {"href": re.compile(".*https://tirto.*")})
# idx=30
# pprint(ass)
#  .find_all('a')

# print(ass[idx])
# print(ass[idx].__dict__)
# pprint(ass[idx].__dict__)

# appbs = AppBs()
# r1 = appbs.setSoup(soup).allLink([], "")
# print(r1)
# b4.findAll()
