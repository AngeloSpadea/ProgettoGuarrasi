# -*- coding: utf-8 -*-
"""
Created on Wen Dec  21 02:43:23 2022

@author: antonio
"""
import pandas as pd
def conta_i_pagamenti_per_distretti(data,Borough_val,paymentint):
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
    zone_lookup = pd.read_csv("./dati/taxi+_zone_lookup.csv", index_col="LocationID")
    risultato = data.groupby(['DOLocationID']).payment_type.value_counts()
    indicirisultato = risultato.index.to_frame(name=['LocalId', 'Payment'])
    risultato = pd.concat([indicirisultato, risultato], axis=1)
    definitiva = pd.merge(left=risultato, right=zone_lookup, left_on="LocalId", right_on='LocationID', how='outer')
    definitiva2 = definitiva[['Payment','payment_type','Borough']]
    sum_payment = definitiva2.query("Borough==@Borough_val and Payment==@paymentint").payment_type.sum()

    return sum_payment