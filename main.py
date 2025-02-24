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

# Verificar la existencia de la columna de correos
email_column = "Email"
if email_column not in df.columns:
    raise ValueError(f"No se encontró la columna '{email_column}' en el archivo CSV")

# Extraer los correos electrónicos
emails = df[email_column].dropna().unique()

# Ruta del ejecutable de holehe (ajustar variables de entorno si es necesario)
holehe_executable = "C:/Users/User/Scripts/holehe.exe"

# Lista para almacenar los resultados
results = []

# Lista de términos a ignorar en la columna "Sitio"
ignore_terms = ["Email used", "Email not used", "Rate limit", "FullName", "https://"]

# Procesar cada correo
for email in emails:
    print(f"Procesando: {email}")
    result = subprocess.run([holehe_executable, email], capture_output=True, text=True)
    
    # Imprimir la salida para depuración
    print("Salida de holehe:")
    print(result.stdout)
    
    # Analizar la salida y filtrar solo sitios con "+"
    lines = result.stdout.split("\n")
    positive_sites = [re.sub(r'\[\+\]\s*', '', line).strip() for line in lines if line.strip().startswith("[+]")]
    
    # Filtrar sitios que contienen términos no deseados
    filtered_sites = [site for site in positive_sites if not any(term in site for term in ignore_terms)]
    
    # Guardar en formato Email | Sitio | [+]
    for site in filtered_sites:
        results.append({"Email": email, "Sitio": site, "[+]": "+"})

# Guardar los resultados en un archivo CSV
try:
    if results:
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["Email", "Sitio", "[+]"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)

        print(f"✅ Resultados guardados en {output_file}")
    else:
        print("⚠️ No se encontraron resultados positivos. Revisa la salida de holehe.")
except Exception as e:
    print(f"❌ Error al guardar el archivo CSV: {e}")