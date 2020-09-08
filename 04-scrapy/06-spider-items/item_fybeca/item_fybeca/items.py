# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader.processors  import MapCompose
from scrapy.loader.processors  import TakeFirst

# src="../../images/thumbnail/294930.jpg"
# http://www.fybeca.com/images/thumbnail/294930.jpg"

def transformar_url_imagen(text):
    url_fybeca = 'https://www.fybeca.com'
    cadena_texto = '../..'
    return text.replace(cadena_texto,url_fybeca)

class ProductoFybeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field(
        input_processor = MapCompose(#Lista de funciones
            transformar_url_imagen
        ),
        output_processor = TakeFirst() # Obtenemos una lista []
                                        #Sacamos
    )
    

class ItemFybecaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
