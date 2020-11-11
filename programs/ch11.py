from urllib.parse import urljoin
from html.parser import HTMLParser
class Collector(HTMLParser):
    'coleta URLs de hyperklink em uma lista'
    def __init__(self, url):
       'inicializa analisador, o URL e uma lista'
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

    def handle_starttag(self, tag, attrs):
        'coleta URLs de hyperlink em sua forma absoluta'
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # constrói URL absoluto
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http': # coleta URLs HTTP
                        self.links.append(absolute)

    def getLinks(self):
        'retorna URLs de hyperlink em seu formato absoluto'
        return self.links