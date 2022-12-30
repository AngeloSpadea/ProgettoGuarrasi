# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 15:48:47 2022

@author: alber
"""

import argparse

def gestione_input():

    parser=argparse.ArgumentParser(description='gestione taxi')
    
    parser.add_argument('-m','--mese',help="inserire il mese",
                        type=str, default='04', choices=["01", "02","03", "04", "05", "06", "07","08","09","10","11","12"])
    
    parser.add_argument('-a', '--anno',help="inserire l'anno per esempio '2021' '2022'", default='2022',
                        type=str)
    
    parser.add_argument('-d', '--distretto',help="inserire il distretto su cui si vuole fare l'analisi ", 
                        default='Bronx', type=str, choices=['Bronx','Brooklyn','EWR','Manhattan','Queens','Staten Island','Unknown'])
    
    args=parser.parse_args()
    
    mese=args.mese
    anno=args.anno
    distretto=args.distretto
    
    return mese,anno,distretto
    
prova=gestione_input()
