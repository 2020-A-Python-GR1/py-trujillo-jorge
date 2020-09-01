import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'
    
    urls = ['https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=639&s=0&pp=25']
    
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
            
    def parse(self, response):
        pass