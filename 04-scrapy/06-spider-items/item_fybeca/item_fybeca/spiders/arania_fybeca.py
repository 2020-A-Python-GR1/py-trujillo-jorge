import scrapy
from item_fybeca.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class AraniaFybeca(scrapy.Spider):
    name = 'fybeca'
    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=150Ypp=25'
    ]
    
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url = url)
    
    def parse(self, response):
        productos = response.css('div.product-tile-inner')
        for producto in productos:
            print(producto)
            detalles = producto.css('div.detail')
            tiene_detalles = len (detalles)> 0
            if(tiene_detalles):
                producto_loader = ItemLoader(#Instancia para cargar las propiedades del item
                    item = ProductoFybeca(),#clase item
                    selector = producto #selector por defecto
                )
                producto_loader.default_output_processor = TakeFirst()#para no guardar el arreglo
                producto_loader.add_css(
                    'titulo', #nombre de propiedad del item
                    'a.name::text' #css para obtener el dato
                )#capsula X 10 mg
                producto_loader.add_xpath(
                    'imagen',
                    'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src'
                )
                yield producto_loader.load_item()