# -*- coding: utf-8 -*-
"""
Created on Wen Dec  21 02:43:23 2022

@author: antonio
"""
import pandas as pd

def conta_i_pagamenti_per_distretti(data,Borough_val = ''):
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
    
    Errors
    -------
    Se non si inserisce un quartiere valido restituisce errore

    """
    #presi i dati dalla tupla dati[0] effettuiamo il conteggio dei "payment_type" 
    #per ogni DOLocationID con un indice "DOLocationID,payment_type"
    risultato = data[0].groupby(['DOLocationID']).payment_type.value_counts()

    #in questa fase andiamo a modificare l'indice "DOLocationID,payment_type"
    #un doppio indice LocalId e Payment
    #per DOLocationID rinominato ---> LocalId 
    #per payment_type rinominato ---> Payment
    indicirisultato = risultato.index.to_frame(name=['LocalId', 'Payment'])

    #Andiamo ad abinare i due nuovi indici con i risultati trovati nella variabile
    #risultato, che ricordiamo è la somma payment_type gruppati per DOLocationID
    risultato = pd.concat([indicirisultato, risultato], axis=1)

    #Ora tramite i codici di LocalId, che sono i codici di zona mergiamo la tabella
    #con i codici di zona e i nomi dei quartieri che si trova nella tupla data[1]
    definitiva = pd.merge(left=risultato, right=data[1], left_on="LocalId", right_on='LocationID', how='outer')
    
    #In questa fase prendiamo poi solo le colonne che sono necessarie per l'analisi
    definitiva2 = definitiva[['Payment','payment_type','Borough']]


    #-- Codice per la ricerca --
    if Borough_val!='':
        try:    
            #-- Ricerca con parametro opzionale del quartiere -- 
            #vengono ritrnati le somme dei "payment_type" gruppati per quartiere
            sum_payment = definitiva2.query("Borough==@Borough_val").groupby(['Payment']).payment_type.sum()
        except  pd.errors.UndefinedVariableError:
            print("Quartiere inserito non valido")
            print("I quartieri di NewYork sono: Bronx, Brooklyn, EWR, Manhattan, Queens , Staten Island")
            print("Controlla di aver inserito la maiuscola nella prima lettera del quartiere oppure di aver inserito EWR tutto maiuscolo")
            exit()
    else: 
        #-- Ricerca senza parametro opzionale del quartiere -- 
        #vengono ritrnati le somme dei "payment_type" generali 
        sum_payment = definitiva2.groupby(['Payment']).payment_type.sum()

    #Pulizia della memoria
    del definitiva2, definitiva, risultato, indicirisultato    
    return sum_payment
