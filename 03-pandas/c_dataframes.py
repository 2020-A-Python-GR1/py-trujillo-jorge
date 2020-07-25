# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:46:53 2020

@author: Jorge
"""


import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pand)

s1 = df1[0] 
#operacion con la serie
s2 = df1[1]
s3 = df1[2] 

df1[3] = s1
df1[4] = s1 *s2

datos_fisicos_uno = pd.DataFrame(
    arr_pand,
    columns = [
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'])

datos_fisicos_dos = pd.DataFrame(
    arr_pand,
    columns = [
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'],
    index = [
        'Jorge',
        'Alejandro'])

serie_peso = datos_fisicos_dos['Peso (kg)']
datos_jorge = serie_peso['Jorge']
print(serie_peso)
print(datos_jorge)

df1.index = ['jorge', 'alejandro']
df1.index = ['Rick', 'Morty']
df1.columns = ['A','B','C','D','E']
























