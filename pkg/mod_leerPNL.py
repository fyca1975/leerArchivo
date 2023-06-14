#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 06:15:24 2023

@author: fredy
"""

import pandas as pd

def leerPNL(archivoLeePNL, archivoLeeBono ):
    datosPNL = pd.read_csv(archivoLeePNL, sep=";", header = 0 )
    # datosPNL = pd.read_csv(archivoLeePNL, sep=";", header = 0 )