"""
@author: Fredy Yecid Castro Agray
"""
import pandas as pd

def generar_csv(dataset, nombre_archivo):
    df = pd.DataFrame(dataset)  # Crea un DataFrame a partir del dataset
    
    # Guarda el DataFrame en un archivo CSV
    df.to_csv(nombre_archivo, index=False)
    
    print(f"Archivo {nombre_archivo} generado exitosamente.")