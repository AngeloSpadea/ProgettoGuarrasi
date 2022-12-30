# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:20:06 2022

@author: angel
"""

def analisi_pagamenti_utilizzati(dictionary):
    """
    Cerca in dictionary il valore con più e meno occorrenze e ne restituisce
    il relativo codice con il numero di occorrenze relativo
    Parameters
    ----------
    dictionary : dict
        keys: codici del pagamento
        values: occorrenze delle keys nei dati.

    Returns
    -------
    tupla di quattro elementi:
        primo elemento
            pagamento_id_max: float
                l'indice del pagamento più presente.
        secondo elemento
            pagamento_id_min : float
                l'indice del pagamento meno presente.
        terzo elemento
            occorrenze_max: float
                il numero delle occorrenze del pagamento più presente.
        quarto elemento
            occorrenze_min : float
                il numero delle occorrenze del pagamento meno presente.

    """
    pagamento_id_max=dictionary.idxmax()
    pagamento_id_min=dictionary.idxmin()
    occorrenze_max=max(dictionary)
    occorrenze_min=min(dictionary)
    
    return pagamento_id_max,pagamento_id_min,occorrenze_max,occorrenze_min