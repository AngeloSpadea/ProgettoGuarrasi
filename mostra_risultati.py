# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 21:22:44 2022

@author: angel
"""
from fpdf import FPDF

def mostra_risultati(anno,pagamento_id_max,pagamento_id_min,occorrenze_max,occorrenze_min,mese='',Bourogh_val=''):
    """
    La funzione presi i dati analizzati crea e salva in ./output un pdf contenente
    la descrizione del lavoro svolto dal nome Risultati.pdf    

    Parameters
    ----------
    anno : str
        l'anno su cui stiamo svolgendo l'analisi.
    pagamento_id_max : float
        DESCRIPTION.
    pagamento_id_min : float
        DESCRIPTION.
    occorrenze_max : float
        DESCRIPTION.
    occorrenze_min : float
        DESCRIPTION.
    mese : str, optional
        Il mese su cui si sta svolgendo l'analisi. The default is ''.
    Bourogh_val : str, optional
        Il distretto su cui si sta svolgendo l'analisi. The default is ''.

    Returns
    -------
    None.

    """
    pdf = FPDF()
     
    # Add a page
    pdf.add_page()
     
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size = 20)
     
    # create a cell
    pdf.cell(200, 10, txt = "Report per mese/anno e per distretto",
             ln = 1, align = 'C')
    
    pdf.set_font("Arial", size = 10)
    # add another cell
    pdf.cell(200, 10, txt = "Il pagamento più utilizzato è id con tot occorrenze e il pagamento meno utilizzato è id con tot occorenze",
             ln = 2, align = 'C')
    
    # pdf.cell(200, 10, txt = "Il pagamento meno utilizzato è id con tot occorenze",
    #          ln = 3, align = 'C')
    
    pdf.image('./output/barchart.png',w=150, x=35, y=28)
    
    pdf.image('./output/grafici_torta.png',w=200, x=0, y=120)
    
    pdf.set_font("Arial", size = 20)
    
    pdf.cell(200, 190, txt = "I grafici a torta per ogni distretto",
              align = 'C')
    # save the pdf with name .pdf
    pdf.output("./output/Risultati.pdf") 
    
    print("Report pronto")
    
if __name__ == '__main__':    
    
    mostra_risultati()