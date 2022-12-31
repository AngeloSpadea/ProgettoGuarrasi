# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:20:23 2022

@author: angel
"""
import matplotlib.pyplot as plt
import pandas as pd
from conta_i_pagamenti_per_distretti import conta_i_pagamenti_per_distretti
from carico_dati import carico_dati

def visualizza_pagamenti_in_ogni_distretto(data,Bourogh_list):
    """
    La funzione crea dei barchart per ogni distretto e li salva in ./output in 
    un immagine dal nome grafici_torta.png

    Parameters
    ----------
    h : dict
        il set di dati raffinato su cui voglio svolgere le mie analisi.

    Returns
    -------
    Tanti grafici a torta quanto sono i bourogh dove vengono visualizzate le 
    distribuzioni dei vari pagamenti.

    """
    #Preparazione dei grafici con la sostituzione dei codici relativi ai tipi 
    # di pagamento con i relativi nomi
    
    lista_conversione=['Void trip','Credit card','Cash','No charge','Dispute','Unknown']
    
    total={}
    for j in Bourogh_list:
        value=conta_i_pagamenti_per_distretti(data,j)
        value.index=lista_conversione[:len(value)]
        total[j]=value
    
     
    #Creazione della figura che conterranno tutti i grafici relativi ad ogni quartiere

    plt.figure(figsize=(15,15))
    plt.style.use('ggplot')
    
    
    count=1;
    for i in total.keys():
        plt.subplot(3, 3, count)        
        plt.title(i)
        df = pd.Series(total[i])
        df.plot.barh()
        
        count+=1
    
    #Salvataggio e visualizzazione dei grafici relativi ad ogni quartiere
    
    plt.savefig('./output/grafici.png', dpi=100)
    plt.show()

#prove per vedere il corretto funzionamento di visualizza_pagamenti_in_ogni_distretto
if __name__ == '__main__':
    
    Bourogh_list=['Bronx','Brooklyn','EWR','Manhattan','Queens','Staten Island','Unknown']
    anno = '2022'
    mese = '01'
    data=carico_dati(anno,mese)
    Borough_val = 'Bronx'
    total=visualizza_pagamenti_in_ogni_distretto(data,Bourogh_list)



