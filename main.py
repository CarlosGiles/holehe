import pandas as pd
import subprocess
import csv
import re
from datetime import datetime

# Ruta del archivo CSV de entrada
file_path = "holehe_dataset.csv"

# Obtener la fecha actual en formato ddmmAAAA
fecha_actual = datetime.now().strftime("%d%m%Y")
# Ruta del archivo CSV de salida con la fecha en el nombre
output_file = f"holehe_results_{fecha_actual}.csv"

# Cargar el CSV
df = pd.read_csv(file_path,encoding='latin1')