# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:26:55 2020

@author: Jorge
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)
sub_df = df.iloc[49989:50519:,].copy()
#Tipos Archivos

#JSON
#Excel

path_excel = "./data/artwork_data.xlsx"
#Con indice como cilumna
#sub_df.to_excel(path_excel)
#Sin el indice como columna
#sub_df.to_excel(path_excel,index=False)
sub_df.to_excel(path_excel, columns = ['artist'],engine='xlsxwriter')

path_excel_mt = "./data/artwork_data_mt.xlsx"
writer = pd.ExcelWriter(path_excel_mt, engine='xlsxwriter')
sub_df.to_excel(writer,sheet_name = 'Primera', columns = ['artist'])
sub_df.to_excel(writer,sheet_name = 'Segunda', columns = ['artist'])
sub_df.to_excel(writer,sheet_name = 'Tercera', columns = ['artist'])
writer.save()

#Formato condicional
num_artistas = sub_df['artist'].value_counts()

path_excel_colores =  "./data/artwork_data_colores.xlsx"

writer = pd.ExcelWriter(path_excel_colores,engine='xlsxwriter')

num_artistas.to_excel(writer,sheet_name='Artistas')
hoja_artistas = writer.sheets['Artistas']

rango_celdas = 'B2:B{}'.format(len(num_artistas.index)+1)

formato_artistas = {
    "type":"2_color_scale",
    "min_value":"10",
    "min_type":"percentile",
    "max_value":"99",
    "max_type":"percentile"}
hoja_artistas.conditional_format(rango_celdas,formato_artistas)
writer.save()

########## SQL #################

with sqlite3.connect("bdd-artist.bdd") as conexion:
    sub_df.to_sql('py_artistas', conexion)
    
################# JSON #############
sub_df.to_json('artistas.json')
sub_df.to_json('artistas_tabla.json', orient = 'table')
























