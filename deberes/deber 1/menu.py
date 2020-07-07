import pruebas
import os
import files
from classes import *

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        option = int(input("""BIENVENIDO
    1. Superheroes
    2. Serie de Comics
    3. Salir
    Ingrese la opción:\n"""))
    except ValueError as identifier:
        option = -1
   
    switcher = {
        1:superhero_menu,
        2:serie_menu,
        3: exit
    }
    func = switcher.get(option, lambda:main_menu())
    return func()

def serie_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        option = int(input("""Menú de serie de comics
    1. Añadir serie
    2. Ver informacion de serie
    3. Modificar informacion de serie
    4. Eliminar serie de comics
    5. Atrás
    Ingrese la opción:\n"""))
    except ValueError as identifier:
        option = -1
    
    switcher={
        1:create_serie,
        2:watch_serie,
        3:update_serie,
        4:delete_serie,
        5:main_menu
        }
    func=switcher.get(option,lambda :serie_menu())
    return func()

def superhero_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        option = int(input("""Menú de superheroe
    1. Añadir superheroe
    2. Ver Superheroe
    3. Modificar Superheroe
    4. Eliminar Superheroe
    5. Atrás
    Ingrese la opción:\n"""))
    except ValueError as identifier:
        option = -1
    
    switcher={
        1:create_superhero,
        2:watch_superhero,
        3:update_superhero_menu,
        4:delete_superhero,
        5:main_menu
        }
    func=switcher.get(option,lambda: superhero_menu())
    return func()

def update_superhero_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        option = int(input("""Menú de superheroe
    1. Editar datos
    2. Añadir/quitar series
    3. Atrás
    Ingrese la opción:\n"""))
    except ValueError as identifier:
        option = -1
    
    switcher={
        1:update_superhero,
        2:add_remove_serie,
        3:superhero_menu
        }
    func=switcher.get(option,lambda: update_superhero_menu())
    return func()

def watch_superhero():
    file = files.Files("./superheroes.json")
    data = file.to_json()
    print(f"Los superheroes registrados son: {data.keys()}")
    nombre_sup = str(input("Nombre del superheroe: \n"))
    if data.keys().__contains__(nombre_sup):
        file.show_sup(nombre_sup, data)
    else:
        print("El superheroe ingresado no esta registrado")
    input("Presione enter para continuar")
    superhero_menu()

def create_superhero():
    file = files.Files("./superheroes.json")
    data = file.to_json()
    print(f"Los superheroes registrados son: {data.keys()}")
    print("CREACION NUEVO SUPERHEROE")
    new_sup={
    "real_name": input(f"Nombre real :\n"),
    "superhero_name" : input(f"Nombre de superheroe: \n"),
    'height': float(input(f"Altura:\n")),
    'apparence_year': int(input(f"Año de aparición:\n")),
    'status':file.from_int_to_bool(int(input(f"Estatus (1 activo 0 inactivo):\n"))),
    'comics':[]
    }
    file.add_sup(file.from_dict_to_superhero(new_sup),data)
    input("Presione enter para continuar")
    superhero_menu()

def update_superhero():
    file = files.Files("./superheroes.json")
    data = file.to_json()
    print(f"Los superheroes registrados son: {data.keys()}\n")
    serie_name = str(input("Ingrese el nombre del superheroe a modificar:\n"))
    old_serie = data[serie_name]
    new_sup={
    "real_name": input(f"Nombre real [default:{old_serie['real_name']}]:\n") or old_serie['real_name'],
    "superhero_name" : input(f"Nombre de superheroe [default:{old_serie['superhero_name']}]:\n") or old_serie['superhero_name'],
    'height': float(input(f"Altura [default:{old_serie['height']}]:\n") or old_serie['height']),
    'apparence_year': int(input(f"Año de aparición [default:{old_serie['apparence_year']}]:\n") or old_serie['apparence_year']),
    'status':int(input(f"Estatus (1 activo 0 inactivo) [default:{old_serie['status']}]:\n") or file.from_bool_to_int(old_serie['status'])),
    'comics':old_serie['comics']
    }
    file.update_sup(serie_name,file.from_dict_to_superhero(new_sup),data)
    print("Editado correctamente")
    input("Enter para continuar")
    superhero_menu()

def delete_superhero():
    file = files.Files("./superheroes.json")
    data = file.to_json()
    print(f"Los superheroes registrados son: {data.keys()}\n")
    serie_name = str(input("Ingrese el nombre del superheroe a Eliminar:\n"))
    try:
        file.delete_sup(serie_name,data)
        print('Eliminado correctamente')
        input('Presione enter para continuar')
        superhero_menu()
    except Exception as id:
        print("No se pudo eliminar, asegurese de escribir bien el nombre")
        input("Enter para continuar")
        superhero_menu()

def delete_serie():
    file = files.Files("./series.json")
    data = file.to_json()
    print(f"Las series registradas son: {data.keys()}")
    serie_name = str(input("Ingrese el nombre de la serie a Eliminar:\n"))
    if data.keys().__contains__(serie_name):
        file.delete_vol(serie_name,data)
        print('Eliminado correctamente')
        input('Presione enter para continuar')
    else:
        print("No se pudo eliminar, asegurese de escribir bien el nombre")
        input("Enter para continuar")
    serie_menu()

def add_remove_serie():
    sup_name=input("Ingrese el superheroe a editar\n")
    file_sup = files.Files("./superheroes.json")
    data = file_sup.to_json()
    print("AÑADIR/QUITAR SERIE\n")
    print(f"Las series registradas son: {data.keys()}\n")
    if data.keys().__contains__(sup_name):
        file_serie= files.Files("./series.json")
        data_series = file_serie.to_json()
        print(f'Todas las series registradas en el programa son: \n{data_series.keys()}')
        #show all series
        print(f"Las series registradas en {sup_name} son:\n {data[sup_name]['comics']}")
        serie_name = input('Ingrese la serie a añadir o quitar\n')
        if data_series.keys().__contains__(serie_name):
            file_sup.add_serie_to_superhero(sup_name,serie_name,data)
            input('Presione enter para continuar')
            update_superhero_menu()
        else:
            print("La serie no se encuentra registrada")
            input('Presione enter para continuar')
            update_superhero_menu()
    else:
        print('El superheroe ingresado no está registrado')
        input('Presione enter para continuar')
        superhero_menu()     
    
def create_serie():
    data = files.Files("./series.json")
    print(f"Las series registradas son: {data.to_json().keys()}\n")
    new_serie={
    "serie_name": input(f"Nombre de la serie de comic:\n"),
    "publish_year" : int(input(f"Año de publicación: \n")),
    'volumes': int(input(f"Número de volumenes:\n")),
    'finalized': data.from_int_to_bool(int(input(f"1 Finalizada. 0 no finalizada):\n"))),
    'writer': input(f"Escritor:\n")
    }
    data.add_volume(data.from_dict_to_comicv(new_serie),data.to_json())
    input("Presione enter para continuar")
    serie_menu()

def watch_serie():
    file = files.Files("./series.json")
    data = file.to_json()
    print(f"Las series registradas son: {data.keys()}")
    nombre_sup = str(input("Nombre de la serie: \n"))
    if data.keys().__contains__(nombre_sup):
        file.show_comic(nombre_sup, data)
    else:
        print("La serie ingresada no esta registrada")
    input("Presione enter para continuar")
    serie_menu()

def update_serie():
    file = files.Files("./series.json")
    data = file.to_json()
    print(f"Las series registradas son: {data.keys()}\n")
    serie_name = str(input("Ingrese el nombre de la serie a modificar:\n"))
    old_serie = data[serie_name]
    new_serie={
    "serie_name": input(f"Nombre [default:{old_serie['serie_name']}]:\n")or old_serie['serie_name'] ,
    "publish_year" : int(input(f"Año de publicación [default:{old_serie['publish_year']}]:\n") or old_serie['publish_year']),
    'volumes': int(input(f"Número de issues [default:{old_serie['volumes']}]:\n") or old_serie['volumes']),
    'finalized': int(input(f"1 Finalizado 0 No finalizado [default:{old_serie['finalized']}]:\n") or file.from_bool_to_int(old_serie['finalized'])),
    'writer':input(f"Escritor [default:{old_serie['writer']}]:\n") or old_serie['writer']
    }
    file.update_vol(serie_name,file.from_dict_to_comicv(new_serie),data)
    print("Editado correctamente")
    input("Enter para continuar")
    serie_menu()
main_menu()