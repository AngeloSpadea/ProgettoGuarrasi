# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 16:41:23 2022

@author: angel
"""

import pandas as pd
import carico_dati
import pulizia_dati
import trova_pagamento_piu_utilizzato
import trova_pagamento_meno_utilizzato
import visualizza_pagamenti_in_ogni_distretto


anno=input("Inserire l'anno su cui si vuole fare l'analisi ")
mese=input("Inserire il mesej su cui si vuole fare l'analisi ")
bourough=input("Inserire il distretto su cui si vuole fare l'analisi ")


c=carico_dati(anno,mese,bourough)

h=pulizia_dati(c)

trova_pagamento_piu_utilizzato(h)

trova_pagamento_meno_utilizzato(h)

visualizza_pagamenti_in_ogni_distretto(h)

