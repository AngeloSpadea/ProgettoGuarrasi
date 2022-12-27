# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 15:48:47 2022

@author: alber
"""

import argparse

def gestione_input():

    parser=argparse.ArgumentParser(description='gestione taxi')
    
    parser.add_argument('mese',help="inserire il mese sottoforma di stringa. per esempio '01' '02' '03' ...",
                        type=str,default='04')
    
    parser.add_argument('anno',help="inserire l'anno sottoforma di stringa. per esempio '2021' '2022'",
                        type=str,default='2022')
    
    args=parser.parse_args()
    anno=args.anno
    mese=args.mese
    return mese,anno
    
prova=gestione_input()
