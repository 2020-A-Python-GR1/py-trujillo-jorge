import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'
    
    urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html']
    
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
            
    def parse(self, response):
        etiqueta_contenedora = response.css('article.product_pod')
        titulos = etiqueta_contenedora.css('h3 > a::text').extract()
        imagen = etiqueta_contenedora.css('div.image_container > a > img::attr(src) ').extract()
        dinero = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        stock = etiqueta_contenedora.css('div.product_price > p.instock::text').extract()
        stars = etiqueta_contenedora.css('p.star-rating::attr(class)').extract()
        print(imagen)
        print(dinero)
        print(stock)
        print(stars)