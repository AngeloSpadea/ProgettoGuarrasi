# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 21:22:44 2022

@author: angel
"""
from fpdf import FPDF

def mostra_risultati():
    pdf = FPDF()
     
    # Add a page
    pdf.add_page()
     
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
     
    # create a cell
    pdf.cell(200, 10, txt = "GeeksforGeeks",
             ln = 1, align = 'C')
     
    # add another cell
    pdf.cell(200, 10, txt = "A Computer Science portal for geeks.",
             ln = 2, align = 'C')
    
    #pdf.image('barchart.png',w=150)
    
    # save the pdf with name .pdf
    pdf.output("./output/risultati.pdf") 
    
mostra_risultati()