#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 06:41:31 2023

@author: fredy
"""
import os

def leerArchivo(rutaOrigen: str):
    print('ruta obtenida -> :', rutaOrigen)
    with os.scandir(rutaOrigen) as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
    # Obtener lafecha de trabajo
    fechaCrea = [i[-8:] for i in ficheros if i[:3] == 'PNL' ]
    return(fechaCrea[0])