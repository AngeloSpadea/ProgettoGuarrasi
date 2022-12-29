# -*- coding: utf-8 -*-
"""
Created on Wen Dec  21 02:43:23 2022

@author: Angelo
@author: Antonio
"""

from carico_dati import carico_dati
from pagamenti import pagamenti
from analisi_pagamenti_utilizzati import analisi_pagamenti_utilizzati
from visualizza_pagamenti import visualizza_pagamenti
from gestione_input import gestione_input
from visualizza_pagamenti_in_ogni_distretto import visualizza_pagamenti_in_ogni_distretto

#funzione che gestisce gli ingressi in particolare restituisce una tupla che ha
#come elemento 0 il mese,elemento 1 l'anno, elemento 2 il distretto
ingressi=gestione_input()
    
anno = ingressi[1]
mese = ingressi[0]
Borough_val = ingressi[2]
#carico il dataset grezzo (da cartella ./dati/anni/{anno}) e la tabella con 
#i codici dei distretti (da cartella ./dati/tabelle_di_conversione/) in @data
data=carico_dati(anno,mese)

#h=pulizia_dati(c)

#ho creato una lista di indici dei pagamenti provvisoria
lista_indici=[0,1,2,3,4,5,6]

#crea un dizionario con gli indici come chiave e con il numero delle occorenze come valori
dictionary=pagamenti(data, lista_indici)
#trova il pagamento il codice del pagamento più e meno utilizzato
k=analisi_pagamenti_utilizzati(dictionary)

#visualizza l'istogramma
visualizza_pagamenti(dictionary,k)

#visualizza i grafici a torta per ogni distretto nella Bourogh_list
Bourogh_list=['Bronx','Brooklyn','EWR','Manhattan','Queens','Staten Island','Unknown']
visualizza_pagamenti_in_ogni_distretto(data,Bourogh_list)

