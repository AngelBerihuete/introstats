# EJERCICIO 1
# -----------
import numpy as np
import pandas as pd

data = data = pd.DataFrame({
    'Piratas': [35000, 45000, 20000, 15000, 5000, 400, 15],
    'Temperatura': [14.2, 14.4, 14.6, 14.9, 15.4, 15.5, 15.9]
})

data.corr()

import statsmodels.api as sm
from statsmodels.formula.api import ols

piratas_model = ols('Temperatura ~ Piratas', data=data).fit()
piratas_model.summary()

sns.regplot(x='Temperatura', y='Piratas', data=data)
sns.regplot(x='Temperatura', y='Piratas', data=data, ci=68)

# EJERCICIO EXTRA (CONJUNTO DE ANSCOME)
# -------------------------------------

ans = sns.load_dataset("anscombe")
ans.groupby(['dataset']).corr()
sns.lmplot('x', 'y', ans, col='dataset', col_wrap=2, size=2)

ansI = ans.loc[ans.dataset == 'I']
ols('y ~ x', data=ansI).fit().summary()

ansII = ans.loc[ans.dataset == 'II']
ols('y ~ x', data=ansII).fit().summary()

ansIII = ans.loc[ans.dataset == 'III']
ols('y ~ x', data=ansIII).fit().summary()

ansIV = ans.loc[ans.dataset == 'IV']
ols('y ~ x', data=ansIV).fit().summary()



# EJERCICIO EXTRA
# ---------------

drinks = pd.read_csv('https://raw.githubusercontent.com/AngelBerihuete/introstats/master/datasets/drinks.csv')

drinks.corr()

drinks['beer_servings'].cov(drinks['total_litres_of_pure_alcohol'])
drinks['beer_servings'].corr(drinks['total_litres_of_pure_alcohol'])

import statsmodels.api as sm
from statsmodels.formula.api import ols

drinks_model = ols('total_litres_of_pure_alcohol ~ beer_servings', data=drinks).fit()

drinks_model.summary()

%pylab inline
%config InlineBackend.figure_format = 'retina' #[Truco] Resolución para pantallas HDPI

import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('ggplot')

sm.graphics.plot_regress_exog(drinks_model, "beer_servings")

from statsmodels.sandbox.regression.predstd import wls_prediction_std

# predictor variable
x = drinks[['beer_servings']]
# dependent variable
y = drinks[['total_litres_of_pure_alcohol']]

_, confidence_interval_lower, confidence_interval_upper = wls_prediction_std(drinks_model)

fig, ax = plt.subplots(figsize=(10,7))

ax.plot(x, y, 'o', label="datos")

ax.plot(x, drinks_model.fittedvalues, 'g--.', label="Ajuste (OLS)")
ax.plot(x, confidence_interval_upper, 'r--')
ax.plot(x, confidence_interval_lower, 'r--')
ax.legend(loc='best');

