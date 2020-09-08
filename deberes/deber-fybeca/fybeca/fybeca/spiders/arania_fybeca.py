import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'fybeca' #Heredado
    
    start_urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=446&s=0&pp=25',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=537&s=0&pp=25',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=627&s=0&pp=25',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=558&s=0&pp=25',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=489&s=0&pp=25',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=562&s=0&pp=25',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=457&s=0&pp=25'
    ]
    
    regla_uno=(
        Rule(
            LinkExtractor(),
            callback = 'parse_page'#Nombre funcion a ejecutar para parsear
        ),
    )

    rules = regla_uno #heredada
    
    def parse_page(self, response):
        lista_productos = response.css('li.product-tile::attr(data-name)').extract()
        for product in lista_productos:
            with open('productos.txt','a+', encoding='utf-8') as archivo:
                archivo.write(product +  '\n')
        