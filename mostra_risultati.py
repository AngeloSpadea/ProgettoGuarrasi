# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 21:22:44 2022

@author: angel
"""
from fpdf import FPDF

def mostra_risultati(anno,tupla,mese='',Bourogh_val=''):
    """
    La funzione presi i dati analizzati crea e salva in ./output un pdf contenente
    la descrizione del lavoro svolto dal nome Risultati.pdf    

    Parameters
    ----------
    anno : str
        l'anno su cui stiamo svolgendo l'analisi.
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
    pdf = FPDF()
     
    # Aggiungo una pagina
    pdf.add_page()
     
    # imposto lo stile e la grandezza del font
    pdf.set_font("Arial", size = 20)
    
    # creo una cella
    pdf.cell(200, 10, txt = "Report per mese/anno e per distretto",
             ln = 1, align = 'C')
    
    # imposto lo stile e la grandezza del font
    pdf.set_font("Arial", size = 10)
    
    # creo una cella
    pdf.cell(200, 10, txt = "Il pagamento più utilizzato è id con tot occorrenze e il pagamento meno utilizzato è id con tot occorenze",
             ln = 2, align = 'C')
    
    #Metto le immagini nel pdf
    pdf.image('./output/barchart.png',w=150, x=35, y=28)
    pdf.image('./output/grafici_torta.png',w=200, x=0, y=120)
    
    # imposto lo stile e la grandezza del font
    pdf.set_font("Arial", size = 20)
    
    # creo una cella
    pdf.cell(200, 190, txt = "I grafici a torta per ogni distretto",
              align = 'C')
    
    # salvo il pdf con il nome Risultati.pdf
    pdf.output("./output/Risultati.pdf") 
    
    print("Report pronto")
    
if __name__ == '__main__':    
    
    mostra_risultati()