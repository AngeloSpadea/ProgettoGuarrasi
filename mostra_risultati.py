# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 21:22:44 2022

@author: angel
"""
from fpdf import FPDF

def mostra_risultati(anno,numero_dati,tupla,mese='',Bourogh_val=''):
    """
    La funzione presi i dati analizzati crea e salva in ./output un pdf contenente
    la descrizione del lavoro svolto dal nome Risultati.pdf    

    Parameters
    ----------
    anno : str
        l'anno su cui stiamo svolgendo l'analisi.
    numero_dati: int
        il numero di dati analizzati
    tupla : tupla
        pagamento_id_max : float
            l'indice del pagamento più presente.
        pagamento_id_min : float
            l'indice del pagamento meno presente.
        occorrenze_max : float
            il numero delle occorrenze del pagamento più presente.
        occorrenze_min : float
            il numero delle occorrenze del pagamento meno presente.
    mese : str, optional
        Il mese su cui si sta svolgendo l'analisi. The default is ''.
    Bourogh_val : str, optional
        Il distretto su cui si sta svolgendo l'analisi. The default is ''.

    Returns
    -------
    None.

    """
    lista_conversione=['Void trip','Credit card','Cash','No charge','Dispute','Unknown']
    pdf = FPDF()
     
    # Aggiungo una pagina
    pdf.add_page()
     
    # imposto lo stile e la grandezza del font
    pdf.set_font("Arial", size = 20)
    
    testo="Report per il "+mese+' '+anno+' '+Bourogh_val
    # creo una cella
    pdf.cell(200, 10, txt = testo,
             ln = 1, align = 'C')
    
    # imposto lo stile e la grandezza del font
    pdf.set_font("Arial", size = 10)
    
    # creo una cella
    pdf.cell(200, 10, txt = "Autori: Antonio Spadea, Angelo Spadea, Alberto Bianchi",
             ln = 2, align= 'C')
    
    # creo una cella
    pdf.cell(200, 10, txt = "Il programma sta analizzando un dataset di "+str(numero_dati)+" occorrenze",
             ln = 3)
    
    testo1="Il valore più presente è "+lista_conversione[int(tupla[0])]+" con "+str(tupla[2])+" occorenze e il valore meno presente è "+lista_conversione[int(tupla[1])]+" con "+str(tupla[3])+" occorenze"
    
    # creo una cella
    pdf.cell(200, 10, txt = testo1,
             ln = 4)
    
    #Metto le immagini nel pdf
    pdf.image('./output/barchart.png',w=150, x=35, y=50)
    
    # Aggiungo una pagina
    pdf.add_page()
    pdf.image('./output/grafici.png',w=200, x=0, y=50)
    
    # imposto lo stile e la grandezza del font
    pdf.set_font("Arial", size = 20)
    
    # creo una cella
    pdf.cell(200, 10, txt = "I pagamenti per ogni distretto",
              align = 'C')
    
    # salvo il pdf con il nome Risultati.pdf
    pdf.output("./output/Risultati.pdf") 
    
    print("Report pronto")

    #Pulizia della memoria
    del testo1, testo, lista_conversione
