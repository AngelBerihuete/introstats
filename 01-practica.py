# EJERCICIO 1
# -----------

import numpy as np
import pandas as pd

data = pd.DataFrame({
    'Genero': ['H', 'M', 'M', 'H', 'M', 'H', 'M', 'H', 'M', 'M'],
    'Respuesta': ['SI', 'NO', 'SI', 'SI', 'SI', 'NO', 'SI', np.nan, 'SI', 'SI'],
    'Tiempo': [1, 5, 9, 8, 7.5, 3.5, 11, 1, 8, 9],
})

data.loc[0:4,:]
data.loc[0:4,'Respuesta':'Tiempo'] # data.head(5).drop('Genero', axis=1)
data.loc[data.Respuesta == 'SI', :] # Selecccion con condicionales
data.to_csv('datosprueba.csv') # Guardamos los datos

# Observaciones
data.isnull().sum()


# EJERCICIO 2
# -----------

drinks = pd.read_csv('https://raw.githubusercontent.com/AngelBerihuete/introstats/master/datasets/drinks.csv')
drinks.head()
drinks.total_litres_of_pure_alcohol.plot(kind='hist', type = 'normed')

drinks.total_litres_of_pure_alcohol.mean()
drinks.total_litres_of_pure_alcohol.median()
drinks.total_litres_of_pure_alcohol.mode()

drinks.beer_servings.quantile([.25, .75])

drinks.beer_servings.quantile([.80])

# EJERCICIO 3
# -----------

drinks.total_litres_of_pure_alcohol.describe()['std']
drinks.total_litres_of_pure_alcohol.describe()['std']/drinks.total_litres_of_pure_alcohol.describe()['mean']
drinks.total_litres_of_pure_alcohol.plot(kind='box')

# EJERCICIO EXTRA
# ---------------
drinks.groupby(['continent']).total_litres_of_pure_alcohol.describe()

(9 - 8.617778)/2.647557 # EU 9 l/year
(5 - 3.007547)/2.647557 # AF 5 l/year

