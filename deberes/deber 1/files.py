import json
from io import StringIO
from classes import *
class Files:
    ruta = ""
    datos_file = ""
    def __init__(self, ruta):
        self.ruta= ruta
        self.datos_file = open(ruta,'r+')

    def to_json(self):
        data = json.load(self.datos_file)
        return data
        
    def get_values(self, dict):
        print(dict.keys())

    def show_sup(self,sup_name, datos):
        print(Superhero().from_dict_to_superhero(datos[sup_name]))

    def show_comic(self,serie_name, datos):
        print(Comic_Serie().from_dict_to_comicv(datos[serie_name]))
        pass

    def write_to_file(self,datos):
        self.datos_file.seek(0)
        self.datos_file.write(json.dumps(datos,indent=4))
        self.datos_file.truncate()
        self.datos_file.close()

    def add_sup(self,new_sup, datos):
        datos.update(new_sup.from_sups_to_dict())
        self.write_to_file(datos)
    
    def add_volume(self,new_vol, datos):
        datos.update(new_vol.from_comicv_to_dict())
        self.write_to_file(datos)
         
    def delete_sup(self, sup_name, datos):
        del datos[sup_name]
        self.write_to_file(datos)

    def delete_vol(self, vol_name, datos):
        del datos[vol_name]
        self.write_to_file(datos)

    def update_sup(self, sup_name, new_datos_sups,datos):
        datos[sup_name]=new_datos_sups.from_sups_to_dict()[new_datos_sups.superhero_name]
        if new_datos_sups.superhero_name != sup_name:
            datos[new_datos_sups.superhero_name] = datos.pop(sup_name)
        self.write_to_file(datos)

    def update_vol(self, vol_name, new_datos_vol,datos):
        datos[vol_name]=new_datos_vol.from_sups_to_dict()[new_datos_vol.superhero_name]
        if new_datos_vol.superhero_name != vol_name:
            datos[new_datos_vol.superhero_name] = datos.pop(vol_name)
        self.write_to_file(datos)
