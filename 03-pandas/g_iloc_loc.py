# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:47 2020

@author: Jorge
"""

import pandas as pd
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