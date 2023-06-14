#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 05:59:17 2023

@author: fredy
"""

import pandas as pd

def leerPnlBonos (archivoLeePNL: str, archivoLeeBono: str ):
    # Leer archivos planos y trabajarlos en dataframe
    # datosPNL = pd.read_csv(archivoLeePNL, sep=";", header = 0)
    datosBono = pd.read_csv(archivoLeeBono, sep=";", header = 0)  
    #Tomar solo las columnas a trabajar 
    datosPNL =  datosPNL [['ContractNB','P&L (Abs)', 'PV effect']]
    datosBono = datosBono [["M_CONTRACT","M_PL_FMV2"]]
    print(datosPNL)   
    print(datosBono) 
    # para poder revisar los tipos de datos a comparar 
    #print('tipo de datos PNL', datosPNL.dtypes)     
    #print('tipo de datos bonos', datosBono.dtypes)
    # merge para generar los contract iguales 
    #tambien se puede trabajar con join pero funciona diferente 
    dfResulta = datosPNL.merge(datosBono, 
                               left_on = 'ContractNB', right_on= 'M_CONTRACT')
    print(dfResulta)
    dfResulta['resultado'] = dfResulta['P&L (Abs)'] + dfResulta['PV effect']
    print(dfResulta)
    print(dfResulta.set_index("ContractNB").head())