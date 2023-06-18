#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Fredy Yecid Castro Agray
"""
import pandas as pd
from datetime import datetime
#import numpy as np
from pkg.mod_generaArchivo import generar_csv

def leerBono( archivoLeeBono, fechaArchivo ):
    # Convertir la fecha
    fecha = datetime.strptime(fechaArchivo, '%d%m%Y')

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

    #Filtra SETTLEMENT_DATE > fecha
    datosBono = datosBono.loc[(datosBono['SETTLEMENT_DATE'] > fecha)]  
    print('Mayor SETTLEMENT_DATE ->', datosBono.shape[0])
    
    # datosBonoGenerar = pd.DataFrame(datosBono['SETTLEMENT_DATE'], index=datosBono['SETTLEMENT_DATE'])
    datosBonoGenerar = pd.DataFrame(datosBono['M_INSTRUMENT'])
    datosBonoGenerar['FECHA_PROCESO'] = fecha

    print(datosBonoGenerar)
    
    # Guardo la columna a mover
    columna = datosBonoGenerar['FECHA_PROCESO']
    # Obtener el nombre de la columna que deseas mover
    column_to_move = 'FECHA_PROCESO'
    # la elimino del dataframe
    datosBonoGenerar = datosBonoGenerar.drop('FECHA_PROCESO', axis=1)
    # Insertar la columna en la posición deseada
    datosBonoGenerar.insert(0, column_to_move, columna)

    # insertar en orden las columnas que van en el nuevo archivo 
    # 
    datosBonoGenerar = datosBonoGenerar.assign(M_PL_FMV2 = datosBono['M_PL_FMV2'],M_TP_NOMCUR = datosBono['M_TP_NOMCUR'],
                                               M_TP_NOMINAL = datosBono['M_TP_NOMINAL'], M_TP_PFOLIO = datosBono['M_TP_PFOLIO'],
                                               M_TP_PRICE = datosBono['M_TP_PRICE'], M_TP_RTVLC02 = datosBono['M_TP_RTVLC02'],
                                               M_TP_SECCOD = datosBono['M_TP_SECCOD'], VALOR_COMPRA = datosBono['VALOR_COMPRA'],
                                               PRECIO_LIMPIO_NEGOCIACION = datosBono['PRECIO_LIMPIO_NEGOCIACION'],
                                               PYG = datosBono['PYG'], PRECIO_SUCIO = datosBono['PRECIO_SUCIO'])

    print(datosBonoGenerar)
    # pasamos los datos al pkg que genera el archivo   
    generar_csv(datosBonoGenerar, 'prueba'+fechaArchivo+ '.txt')



    #print(datosBono)      
