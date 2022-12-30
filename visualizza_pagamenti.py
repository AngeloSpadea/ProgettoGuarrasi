# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:23:33 2022

@author: angel
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from carico_dati import carico_dati
from conta_i_pagamenti_per_distretti import conta_i_pagamenti_per_distretti

def visualizza_pagamenti(dictionary):
    """
    Dati il dictionary e i pagamenti_values crea e salva in ./output una figura
    con un istogramma dal nome barchart.png.
    Istogramma: 
        asse x: ci sono i codici dei pagamenti
        asse y: ci sono le occorrenze in scala logaritimica
    Il rettangolo con più occorrenze e quindi il più alto viene colorato in rosso
    Il rettangolo con meno occorrenze e quindi il più basso viene colorato in cyano
    Mentre tutti gli altri vengono colorati in nero    

    Parameters
    ----------
    dictionary : dict
        keys: codici del pagamento
        values: occorrenze delle keys nei dati.
    Returns
    -------
    None.

    """
    # labels: nome barre
    # values: altezza barre

    plt.figure(figsize=(5,3),)
    colors=['black', 'black', 'black', 'black', 'black', 'black']
    colors[int(dictionary.idxmax())]='red'
    colors[int(dictionary.idxmin())]='cyan'
    lista_conversione=['Void trip','Credit card','Cash','No charge','Dispute','Unknown']
    dictionary.index=lista_conversione[:len(dictionary)]
    bars = pd.Series(dictionary)
    
    bars.plot.bar(color=colors)  

    plt.savefig('./output/barchart.png', dpi=300)
    plt.show()
    
if __name__ == '__main__':
    
    Bourogh_list=['Bronx','Brooklyn','EWR','Manhattan','Queens','Staten Island','Unknown']
    anno = '2022'
    mese = '01'
    data=carico_dati(anno,mese)
    Borough_val = 'Bronx'
    dictionary=conta_i_pagamenti_per_distretti(data, Borough_val)
    ba=visualizza_pagamenti(dictionary)