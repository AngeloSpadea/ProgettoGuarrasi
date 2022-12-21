# -*- coding: utf-8 -*-
"""
Created on Wen Dec  21 02:43:23 2022

@author: Angelo
@author: Antonio
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def carico_dati(anno,mese):
    """
    

    Parameters
    ----------
    anno : int
         rappresenta l'anno su cui voglio svolgere l'analisi.
         l'int deve essere di fortmato **** (Esempio: 2022).
    mese : string
        rappresenta il numero del mese su cui voglio svolgere l'analisi.
        l'int deve essere di fortmato ** (Esempio: 04)
    bourogh : string
        rappresenta il distretto su cui voglio svolgere l'analisi.

    Returns
    -------
    il dataset grezzo e una stringa nella quale c'è un messaggio 
    nel quale viene specificato l'esito della funzione. Ad esempio 
    "Ho caricato i dati correttamente" o "Non sono riuscito a caricare i dati"

    """
    anno = '2022'
    mese = '04'
    print(f'./dati/{anno}/yellow_tripdata_{anno}-{mese}.parquet')
    data = pd.read_parquet(f'./dati/{anno}/yellow_tripdata_{anno}-{mese}.parquet')
    

    return data