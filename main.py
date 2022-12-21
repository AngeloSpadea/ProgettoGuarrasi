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
from trova_pagamento_piu_utilizzato import trova_pagamento_piu_utilizzato
from trova_pagamento_meno_utilizzato import trova_pagamento_meno_utilizzato
from visualizza_pagamenti_in_ogni_distretto import visualizza_pagamenti_in_ogni_distretto


#richiedo all'utente l'inserimento dei possibili input della funzione 
anno=input("Inserire l'anno su cui si vuole fare l'analisi ")
mese=input("Inserire il mesej su cui si vuole fare l'analisi ")
bourough=input("Inserire il distretto su cui si vuole fare l'analisi ")

anno = '2022'
mese = '04'
Borough_val = 'Bronx'
#carico il mese richiesto in @data prendendolo dalla cartella dati/*
data=carico_dati(anno,mese)
#carico la tabella con i nomi dei quartieri e il loro codice
zone_lookup = pd.read_csv("./dati/taxi+_zone_lookup.csv", index_col="LocationID")

#h=pulizia_dati(c)

#trova_pagamento_piu_utilizzato(h)

#trova_pagamento_meno_utilizzato(h)

#chiamo la funzione per caricarmi i risultati della ricerca
paymentint = 1
risultato = conta_i_pagamenti_per_distretti(data,Borough_val,paymentint)


print(risultato)

#visualizza_pagamenti_in_ogni_distretto(h)

