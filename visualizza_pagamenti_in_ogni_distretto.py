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
    

    Parameters
    ----------
    h : dict
        il set di dati raffinato su cui voglio svolgere le mie analisi.

    Returns
    -------
    Tanti grafici a torta quanto sono i bourogh dove vengono visualizzate le 
    distribuzioni dei vari pagamenti.

    """
    lista_conversione=['Void trip','Credit card','Cash','No charge','Dispute','Unknown']
    
    total={}
    for j in Bourogh_list:
        value=conta_i_pagamenti_per_distretti(data,j)
        value.index=lista_conversione[:len(value)]
        total[j]=value
    #values=list(total['Bronx'].index)
    #labels=list(total['Bronx'][:])
     
    
    plt.figure(figsize=(15,15))
    plt.style.use('ggplot')
    
    # axs[0, 0].plot(x, y)
    # axs[0, 1].plot(x, y, 'tab:orange')
    # axs[1, 0].plot(x, -y, 'tab:green')
    # axs[1, 1].plot(x, -y, 'tab:red')
    # cambia lo stile dei colori
    count=1;
    for i in total.keys():
        plt.subplot(3, 3, count)        
        plt.title(i)
        df = pd.Series(total[i])
        plot=df.plot.pie(autopct='%.2f %%',pctdistance=0.8)
        plot.set(ylabel=None)
        # a1.pie(labels, labels=values, explode=explode,pctdistance=0.8, autopct='%.2f %%')
        count+=1
    plt.savefig('./output/grafici_torta.png', dpi=100)
    plt.show()
    
    return total

if __name__ == '__main__':
    
    Bourogh_list=['Bronx','Brooklyn','EWR','Manhattan','Queens','Staten Island','Unknown']
    anno = '2022'
    mese = '01'
    data=carico_dati(anno,mese)
    Borough_val = 'Bronx'
    total=visualizza_pagamenti_in_ogni_distretto(data,Bourogh_list)



