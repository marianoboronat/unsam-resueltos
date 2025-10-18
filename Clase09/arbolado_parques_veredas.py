# fileparse.py
import csv
import pandas as pd
import seaborn as sns

# 9.6
df_lineal = pd.read_csv("arbolado-publico-lineal-2017-2018.csv")
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
df_lineal_seleccion

# 9.7
# boxplot diametro
df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')

# boxplot altura
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')