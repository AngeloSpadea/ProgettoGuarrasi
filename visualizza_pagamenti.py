# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:23:33 2022

@author: angel
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def visualizza_pagamenti(dictionary):
    """
    Dati il dictionary e i pagamenti_values crea una figura con un istogramma.
    Istogramma: 
        asse x: ci sono i codici dei pagamenti
        asse y: ci sono le occorrenze in scala logaritimica
    al rettangolo più alto viene applicata una texture di stelline
    al rettangolo più basso viene applicata una texture zebrata
    

    Parameters
    ----------
    dictionary : dict
        keys: codici del pagamento
        values: occorrenze delle keys nei dati.
    pagamenti_values : tupla con due elementi
        primo elemento
            max_pagamento : int
                l'indice del pagamento più presente.
        secondo elemento
            min_pagamento : int
                l'indice del pagamento meno presente.

    Returns
    -------
    None.

    """
    # labels: nome barre
    # values: altezza barre

    plt.figure(figsize=(5,3),)
    bars = pd.Series(dictionary)
    bars.plot.bar()
    # hatch: texture
    # bars[values.index(pagamenti_values[0])].set_hatch("*")
    # bars[values.index(pagamenti_values[1])].set_hatch("/")
    # oppure
    #patterns = ['/', 'O', '*']
    #for i, bar in enumerate(bars):
        #bar.set_hatch(patterns[i])

    plt.savefig('./output/barchart.png', dpi=300)
    plt.show()