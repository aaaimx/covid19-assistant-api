# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:28:18 2020
@author: maorc
"""
import numpy as np
# Vector que se obtiene del frontend
valr=np.array([4, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1])
 # Procesamiento para calcular el elemento a leer a partir del vector
t=np.linspace(36,40,4)
q=np.linspace(0,10,4)
cuatros=np.zeros((11))
for i in range(11):
    cuatros[i]=4**(10-i)
# Cálculo del elemento por leer en el archivo
num=int(sum((valr-1)*cuatros)+1)
# Lectura del archivo
fid=open('hiper.txt','r')
a=fid.read()
fid.close()
# Diagnóstico
b=a[num-1]
