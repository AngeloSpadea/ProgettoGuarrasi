# -*- coding: utf-8 -*-
"""
Created on Sun Dec  19 00:43:23 2022

@author: antonio
"""

def conta_i_pagamenti_per_distretti(h):
    """
    Description
    ----------
    La funzione prende in analisi il dataset pulito e per ogni Taxi Zone (DOLocationID)
    conta quanti pagamenti per metodo(payment_type) vengono fatti 

    DOLocationID è un intero che va da 1-263
    payment_type è un intero che va da 1-6 e rappresentano con
    1= Credit card
    2= Cash
    3= No charge
    4= Dispute
    5= Unknown
    6= Voided trip

    Parameters
    ----------
    h : dict
        il set di dati raffinato su cui faccio le mie analisi.

    Returns
    -------
    risultato : Series dove come indice abbiamo (x,y) 
        x = Taxi Zone e y = rappresenta il codice di pagamento

    """
    
    risultato = h.groupby(['DOLocationID']).payment_type.value_counts()
    return risultato