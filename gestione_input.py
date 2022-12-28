# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 15:48:47 2022

@author: alber
"""

import argparse

def gestione_input():

    parser=argparse.ArgumentParser(description='gestione taxi')
    
    group_mese=parser.add_mutually_exclusive_group()
    group_anno=parser.add_mutually_exclusive_group()
    group_distretto=parser.add_mutually_exclusive_group()
    
    group_mese.add_argument('-m','--mese',help="inserire il mese",
                        type=str, default='04', choices=["01", "02","03", "04", "05", "06", "07","08","09","10","11","12"])
    
    group_anno.add_argument('-a', '--anno',help="inserire l'anno per esempio '2021' '2022'", default='2022',
                        type=str)
    
    group_distretto.add_argument('-d', '--distretto',help="inserire il distretto su cui si vuole fare l'analisi ", 
                        default='Bronx', type=str, choices=['Bronx','Brooklyn','EWR','Manhattan','Queens','Staten Island','Unknown'])
 
   
    group_mese.add_argument('-mm','--mesi',help="lista dei mesi su cui fare l'analisi",default=[])
    group_anno.add_argument('-aa','--anni',help="lista degli anni su cui fare l'analisi",default=[])
    group_distretto.add_argument('-dd','--distretti',help="lista dei distretti su cui fare l'analisi",default=[])
    
    args=parser.parse_args()
    
    mese=args.mese
    anno=args.anno
    distretto=args.distretto
    mesi=args.mesi
    anni=args.anni
    distretti=args.distretti
    
    return mese,anno,distretto,mesi,anni,distretti
    
prova=gestione_input()
