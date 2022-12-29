# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:20:06 2022

@author: angel
"""

def analisi_pagamenti_utilizzati(dictionary):
    """
    Cerca in dictionary il valore con più e meno occorrenze e ne restituisce
    il relativo codice

    Parameters
    ----------
    dictionary : dict
        keys: codici del pagamento
        values: occorrenze delle keys nei dati.

    Returns
    -------
    tupla di due elementi:
        primo elemento
            max_pagamento : int
                l'indice del pagamento più presente.
        secondo elemento
            min_pagamento : int
                l'indice del pagamento meno presente.

    """
    pagamento_id_max=dictionary.idxmax()
    pagamento_id_min=dictionary.idxmin()
    occorenze_max=max(dictionary)
    occorenze_min=min(dictionary)
    print("Il valore più presente è "+str(pagamento_id_max)+" con "+str(occorenze_max)+" occorenze","Il valore meno presente è "+str(pagamento_id_min)+" con "+str(occorenze_min)+" occorenze")
    return "Ho fatto"