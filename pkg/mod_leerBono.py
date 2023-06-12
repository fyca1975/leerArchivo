#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 06:24:23 2023

@author: fredy
"""
import pandas as pd

def leerBono( archivoLeeBono, fecha ):
    datosBono = pd.read_csv(archivoLeeBono, sep=";", header = 0 )
    # convertir trn date a campo fecha 
    # print(datosBono.head())
    print(datosBono)
    datosBono['SETTLEMENT_DATE'] = pd.to_datetime(datosBono['SETTLEMENT_DATE']
                                       , format="%d/%m/%Y")
    datosBono['TRN_DATE'] = pd.to_datetime(datosBono['TRN_DATE']
                                      , format="%d/%m/%Y")
    print('Fecha a procesar',fecha)
    print ('TRN_DATE-->', datosBono['TRN_DATE'].dtypes)
    # Quitamos los registros 
    # (df3[(df3.county=='Manhattan') & (df.party=='Democrat')])
    datosBono = datosBono[(datosBono['TRN_DATE']<= fecha) | 
                          (datosBono['SETTLEMENT_DATE']<= fecha)]
    print(datosBono)      
    # Quitar los espacios para poder realizar la comparacion .split
    datosBono['M_TP_PFOLIO'] = datosBono['M_TP_PFOLIO'].str.split(expand=True)
    datosBono = datosBono[datosBono.M_TP_PFOLIO.isin(
        ('FI1','FI2','FI3','FI4','FI6','FI7_SUBAST',''))]
    # print(datosBono['SETTLEMENT_DATE'])
    # print(datosBono.head())
  
    # datosBono['SETTLEMENT_DATE'] = pd.to_datetime(datosBono['SETTLEMENT_DATE']
    #                                   , format="%d/%m/%Y")
    # print(datosBono['SETTLEMENT_DATE'] - fecha )
    # print(fecha)
  