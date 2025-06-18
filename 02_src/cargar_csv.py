  
import pandas as pd

def cargar_datos(ruta_csv):
    """Carga el dataset desde un archivo CSV y lo retorna como DataFrame."""
    df = pd.read_csv(ruta_csv)
    return df
