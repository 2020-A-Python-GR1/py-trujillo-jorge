# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:33:06 2020

@author: Jorge
"""
import pandas as pd

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

serie_artistas_duplicados = df['artist']

artistas = pd.unique(serie_artistas_duplicados)

print(type(artistas))

print(artistas.size)

blake = df['artist'] == 'Blake, William' # SERIE

print(blake.value_counts())
df_blake = df[blake]
































