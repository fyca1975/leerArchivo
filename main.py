#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Fredy Yecid Castro Agray 
"""
import os
from datetime import datetime
##from pkg.mod_leerpnlbonos import leerPnlBonos 
from pkg.mod_leerArchivo import leerArchivo
from pkg.mod_leerBono import leerBono

def run():
    # Obtener la ruta actual
    rutaActual = os.path.dirname(os.path.abspath(__file__))
    # utiliza paquete para traer la fecha de trabajo 
    fechaArchivo=leerArchivo(rutaActual)
    ##archivoLeePNL = 'PNL_'+ fechaArchivo
    archivoLeeBono = 'batch_Bonos_'+ fechaArchivo + '.txt'
    ##leerPnlBonos(archivoLeePNL,archivoLeeBono )
    # convierte el str a formato de fecha
    #date_object = datetime.strptime(fechaArchivo, '%d%m%Y')
    leerBono(archivoLeeBono, fechaArchivo )


if __name__ == '__main__':
    run()
    
