#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 06:24:23 2023

@author: Fredy Yecid Castro Agray
"""
import pandas as pd
#import numpy as np
from pkg.mod_generaArchivo import generar_csv

def leerBono( archivoLeeBono, fecha ):
    # Crea dataset con pandas para trabajar los datos del archivo
    datosBono = pd.read_csv(archivoLeeBono, sep=";", header = 0 )
   
    # print(datosBono.head())
    print(datosBono.shape[0])
     # convertir trn date a campo fecha 
    datosBono['SETTLEMENT_DATE'] = pd.to_datetime(datosBono['SETTLEMENT_DATE']
                                       , format="%d/%m/%Y")
    datosBono['TRN_DATE'] = pd.to_datetime(datosBono['TRN_DATE']
                                      , format="%d/%m/%Y")
    print('Fecha a procesar',fecha)
    print ('TRN_DATE-->', datosBono['TRN_DATE'].dtypes)

    # Quitamos los registros menores e iguales a la fecha de proceso 
    datosBono = datosBono.loc[(datosBono['TRN_DATE']<= fecha)]
    print('Despues de <=', datosBono.shape[0])
    
    #Quita los espacios en el campo M_TP_PFOLIO
    datosBono['M_TP_PFOLIO'] = datosBono['M_TP_PFOLIO'].str.split(expand=True)
    
    # solo dejamos en el dataset los siguientes portafolios
    datosBono = datosBono[datosBono.M_TP_PFOLIO.isin(
        ('FI1','FI2','FI3','FI4','FI6','FI7_SUBAST',''))]
    print('Despues de portafolios ->', datosBono.shape[0])
  
    # los stldate vacios se quitan del data set 
    datosBono = datosBono.dropna(subset=['SETTLEMENT_DATE'])
    print('Despues de quitar nulos ->', datosBono.shape[0])

    # genera solo los mayores 
    datosBono = datosBono.loc[(datosBono['SETTLEMENT_DATE'] > datosBono['TRN_DATE'])]  
    print('Mayor fecha ->', datosBono.shape[0])

    # pasamos los datos al pkg que genera el archivo 
    generar_csv(datosBono, 'prueba.csv')



    #print(datosBono)      
