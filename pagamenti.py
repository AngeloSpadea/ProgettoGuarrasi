# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:19:29 2022

@author: angel
"""

def pagamenti(data,lista_indici):
    """
    La funzione prende in ingresso i dati e restituisce un dizionario che ha 
    come chiavi il codice del pagamento e come valori le occorenze presenti 
    delle chiavi nel dataset

    Parameters
    ----------
    data : DataFrame
        set di dati su cui fare le analisi.
    lista_indici: list
        lista dei codici dei pagamenti

    Returns
    -------
    dictionary : dict
        keys: codici del pagamento
        values: occorrenze delle keys nei dati.

    """
    dictionary={}
    for i in lista_indici:
        pagamento=(data.payment_type==i).sum()
        if pagamento!=0:    
            dictionary[i]=pagamento    
    return dictionary