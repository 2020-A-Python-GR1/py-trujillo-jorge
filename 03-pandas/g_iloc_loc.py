# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:47 2020

@author: Jorge
"""

import pandas as pd
import numpy as np
path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

#loc

primero = df.loc[1035]

print(primero)
print(primero['artist'])
print(primero.index)

serie_vertical = df['artist']
print(serie_vertical)
print(serie_vertical.index)

df_1035 = df[df.index == 1035]

segundo = df.loc[1035] #filtrar por indice
segundo = df.loc[[1035,1036]]

segundo = df.loc[3:5]
segundo = df.loc[df.index == 1035]

segundo = df.loc[1035,'artist']#1 indice
segundo = df.loc[1035,['artist','medium']]



datos = {
    "nota 1":{
        "Pepito":7,
        "Juanita":8,
        "Maria":9
        },
    "nota 2":{
        "Pepito":7,
        "Juanita":8,
        "Maria":9
        },
    "disciplina":{
        "Pepito":4,
        "Juanita":9,
        "Maria":2
        }
    }

notas = pd.DataFrame(datos)

condicion_nota = notas["nota 1"] > 7
condicion_disc = notas["disciplina"]> 7
condicion_nota_dos = notas["nota 2"] > 7

mayores_siete = notas.loc[condicion_nota,["nota 1"]]

pasaron = notas.loc[condicion_nota][condicion_nota_dos][condicion_disc]

notas.loc[:,"disciplina"]=7

########Promedio de las 3 notas (n1+n2+n3)/3


prom = np.mean(np.transpose(notas.loc[:]))

