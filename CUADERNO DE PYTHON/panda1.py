# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 19:28:32 2023

@author: Neymar
"""

import pandas as pd 
titulos=pd.read_csv('data/titles.csv')
print(titulos.head(10))
print("\n*2")
elenco=pd.read_csv('data/cast.csv')
print(elenco.head(10))





#cuantass peliculas listadas en el dataframe
print(len(titulos))
#cuantos elementos estan listados en el dataframe elenco

print(len(elenco))


#listar todas las perliculas que contengan la palabra spyderm

consulta1=titulos[titulos.title.str.contains("Spyder")]
print(consulta1)