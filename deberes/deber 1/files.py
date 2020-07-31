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

    def show_sup(self,sup_name, data):
        print(self.from_dict_to_superhero(data[sup_name]))
        self.datos_file.close()

    def show_comic(self,serie_name,datos):
        print(self.from_dict_to_comicv(datos[serie_name]))
        self.datos_file.close()

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
        fl = Files("./series.json")
        fl.delete_when_delete(vol_name)
        del datos[vol_name]
        self.write_to_file(datos)
        
    def delete_when_delete(self, vol_name):
        fl = Files("./superheroes.json")
        datos_sup = fl.to_json()
        for sup in datos_sup:
            if(datos_sup[sup]['comics'].__contains__(vol_name)):
                fl.add_serie_to_superhero(sup,vol_name,datos_sup)    
        fl.write_to_file(datos_sup)

    def update_sup(self, sup_name, new_datos_sups,datos):
        if type(new_datos_sups.status)==type(1):
            new_datos_sups.status= self.from_int_to_bool(new_datos_sups.status)
        datos[sup_name]=new_datos_sups.from_sups_to_dict()[new_datos_sups.superhero_name]
        if new_datos_sups.superhero_name != sup_name:
            datos[new_datos_sups.superhero_name] = datos.pop(sup_name)
        self.datos_file.seek(0)
        self.datos_file.write(json.dumps(datos,indent=4))
        self.datos_file.truncate()

    def update_vol(self, vol_name, new_datos_vol,datos):
        if type(new_datos_vol.finalized)== type(1):
            new_datos_vol.finalized = self.from_int_to_bool(new_datos_vol.finalized)
        datos[vol_name]=new_datos_vol.from_comicv_to_dict()[new_datos_vol.serie_name]
        if new_datos_vol.serie_name != vol_name:
            datos[new_datos_vol.serie_name] = datos.pop(vol_name)
        self.write_to_file(datos)

    def from_dict_to_superhero(self, arr_de_datos):
        return Superhero(arr_de_datos["real_name"],
        arr_de_datos["superhero_name"],
        arr_de_datos["height"],
        arr_de_datos["apparence_year"],
        arr_de_datos["status"],
        arr_de_datos['comics'])

    def from_int_to_bool(self, numero):
        if numero == 1:
            return True
        if numero == 0:
            return False

    def from_bool_to_int(self, data):
        if data == True:
            return 1
        else:
            return 0

    def from_dict_to_comicv(self, arr_de_datos):
        return Comic_Serie(arr_de_datos["serie_name"],
        arr_de_datos["publish_year"],
        arr_de_datos["volumes"],
        arr_de_datos["finalized"],
        arr_de_datos["writer"])

    def add_serie_to_superhero(self, nombre_sup,nombre_serie, data):
        aux = data[nombre_sup]
        sup = self.from_dict_to_superhero(aux)
        if (sup.comics.__contains__(nombre_serie)):
            sup.delete_comic_serie(nombre_serie)
            self.update_sup(nombre_sup,sup,data)
            print('Se ha eliminado un a serie')
        else:
            sup.add_comic_serie(nombre_serie)
            self.update_sup(nombre_sup,sup,data) 
            print("Se ha añadido una serie")       


