# -*- coding: utf-8 -*-
"""
Created on Wen Dec  21 02:43:23 2022

@author: antonio
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def carico_dati(anno,mese,bourogh):
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
    
    mese = '04'
    print(f'./dati/2022/yellow_tripdata_2022-{mese}.parquet')
    data = pd.read_parquet(f'./dati/2022/yellow_tripdata_2022-{mese}.parquet')
    

    return data