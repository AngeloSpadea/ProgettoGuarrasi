# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 15:48:47 2022

@author: alber
"""

import argparse

parser=argparse.ArgumentParser(description='gestione taxi')

parser.add_argument('mese',help="inserire il mese sottoforma di stringa. per esempio '01' '02' '03' ...",
                    type=str,default='04')

parser.add_argument('anno',help="inserire l'anno sottoforma di stringa. per esempio '2021' '2022'",
                    type=str,default='2022')

if __name__=='__main__':
    args=parser.parse_args()
    print(f'argument2 {args}')
    print(f'argument1 {args.anno}')
    print(f'argument1 {args.mese}')