# -*- coding: utf-8 -*-
"""
==================================
Fuzzy Inference Script     
==================================
Created on Tue Mar 24 12:28:18 2020
@author: maorc
"""
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Vector que se obtiene del frontend
values = [4, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1] 

def get_diagnosis(values):
    """
    Get Diagnosis of diseases given a array of values
    :args:
        values: list() 
        An array of 11 integers
    :retuns:
        hiper[pos]: an integer as diagnostic
    """
    # Procesamiento para calcular el elemento a leer a partir del vector
    values = np.array(values)
    t = np.linspace(36,40,4)
    q = np.linspace(0,10,4)
    cuatros = np.zeros((11))

    for i in range(11):
        cuatros[i] = 4 ** (10 - i)
        
    # Cálculo del elemento por leer en el archivo
    pos = int(sum((values - 1) * cuatros) + 1) - 1

    # Lectura del archivo
    with open(os.path.join(BASE_DIR, 'hiper.txt'),'r') as fid:
        hiper = fid.read()
        fid.close()

        # Diagnóstico
        return int(hiper[pos])
