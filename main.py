# -*- coding: utf-8 -*-
"""
Created on Wen Dec  21 02:43:23 2022

@author: Angelo
@author: Antonio
"""

import pandas as pd
from conta_i_pagamenti_per_distretti import conta_i_pagamenti_per_distretti
from carico_dati import carico_dati
from pulizia_dati import pulizia_dati
from pagamenti import pagamenti
from analisi_pagamenti_utilizzati import analisi_pagamenti_utilizzati
from visualizza_pagamenti import visualizza_pagamenti


#richiedo all'utente l'inserimento dei possibili input della funzione 
anno=input("Inserire l'anno su cui si vuole fare l'analisi ")
mese=input("Inserire il mese su cui si vuole fare l'analisi ")
bourough=input("Inserire il distretto su cui si vuole fare l'analisi ")

anno = '2022'
mese = '04'
Borough_val = 'Bronx'
#carico il dataset grezzo (da cartella ./dati/anni/{anno}) e la tabella con 
#i codici dei distretti (da cartella ./dati/tabelle_di_conversione/) in @data
data=carico_dati(anno,mese)

#h=pulizia_dati(c)

#trova_pagamento_piu_utilizzato(h)

#trova_pagamento_meno_utilizzato(h)

#chiamo la funzione per caricarmi i risultati della ricerca
paymentint = 1
risultato = conta_i_pagamenti_per_distretti(data,Borough_val,paymentint)


print(risultato)

#visualizza_pagamenti_in_ogni_distretto(h)

