# CALCULO DE PROBABILIDADES
# -------------------------

import numpy as np
import pandas as pd
import scipy.stats as st

# CALCULO DE P(X < 12) para X ~ N(12, 5)
st.norm.cdf(12,loc=12, scale=5)

# CALCULO DEL CUANTIL 0.5: P(X < ?) = 0.5 para X ~ N(12, 5)
st.norm.ppf(0.5, loc=12, scale=5)


## INTERVALOS DE CONFIANZA
# ------------------------

# EJERCICIO Intervalo de conf para la varianza
def var_confidence_interval(data, alpha=0.05):
    v = data.var()
    l_inf = (data.size-1.0)*data.var()/st.chi2.ppf(1.-alpha/2., data.size-1.0)
    l_sup = (data.size-1.0)*data.var()/st.chi2.ppf(alpha/2., data.size-1.0)
    return v, l_inf, l_sup

X = st.norm(loc=12.0, scale=10.0)
samples = pd.DataFrame(X.rvs(size=10000).reshape(100,100))
a = samples.loc[:,0]

# EJERCICIO Intervalo de conf para una proporción

def p_confidence_interval(x, n, alpha=0.05):
    p = x/n
    l_inf = p-st.norm.ppf(1-alpha/2)*np.sqrt((p)*(1-p)/n) - 1/(2.*n)
    l_sup = p+st.norm.ppf(1-alpha/2)*np.sqrt((p)*(1-p)/n) + 1/(2.*n)
    return p, l_inf, l_sup

x = 25 # Presentan la característica de los elegidos
n = 100 # Tamaño de la muestra

p_confidence_interval(x=25, n=100, alpha= 0.01)


# EJERCICIO Intervalo de conf para el cociente de varianzas

def p_confidence_interval(x, n, alpha=0.05):
    p = x/n
    l_inf = p-st.norm.ppf(1-alpha/2)*np.sqrt((p)*(1-p)/n) - 1/(2.*n)
    l_sup = p+st.norm.ppf(1-alpha/2)*np.sqrt((p)*(1-p)/n) + 1/(2.*n)
    return p, l_inf, l_sup

x = 25 # Presentan la característica de los elegidos
n = 100 # Tamaño de la muestra

def IC_cociente_varianzas(data1, data2, alpha= 0.05):
    var1 = data1.var()
    var2 = data2.var()
    m = data1.size
    n = data2.size
    l_inf = st.f.ppf(alpha/2, m-1, n -1)*var1/var2
    l_sup = st.f.ppf(1.0-alpha/2, m-1, n -1)*var1/var2
    return var1/var2, l_inf, l_sup

data1 = samples.loc[:,0]
data2 = samples.loc[:,1]
