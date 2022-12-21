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
    max_pagamento=max(dictionary, key=dictionary.get)
    min_pagamento=min(dictionary, key=dictionary.get)
    print("Il valore più presente è "+str(max_pagamento)+" con "+str(dictionary[max_pagamento])+" occorenze","Il valore meno presente è "+str(min_pagamento)+" con "+str(dictionary[min_pagamento])+" occorenze")
    return max_pagamento,min_pagamento