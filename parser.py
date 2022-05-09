from bs4 import BeautifulSoup
from pprint import pprint
import re

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

fname = "./dummy/site_tirto.id pertanian at DuckDuckGo.html"
soup = toBs4(fname)

# print(soup)
ass = soup.find_all('a', {"href": re.compile(".*https://tirto.*")})
#  .find_all('a')

idx=30
pprint(ass)
# print(ass[idx])
# print(ass[idx].__dict__)
# pprint(ass[idx].__dict__)

# appbs = AppBs()
# r1 = appbs.setSoup(soup).allLink([], "")
# print(r1)
# b4.findAll()
