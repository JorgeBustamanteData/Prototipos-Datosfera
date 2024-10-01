import pandas as pd
import os

# Ruta base de los archivos
base_path = 'C:/Users/YO/Desktop/DATOSFERA/'
categorias = ['ventas', 'marketing', 'contabilidad', 'recursos_humanos', 'logistica']

dfs = []

# Leer los archivos de cada categoría y añadir la columna 'Categoria'
for categoria in categorias:
    csv_file = base_path + f'datos_{categoria}_ficticios.csv'
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        df['Categoria'] = categoria  # Añadir la columna de categoría
        dfs.append(df)
    else:
        print(f"Error: No se encontró el archivo '{csv_file}'")

# Unir todas las categorías en un solo dataframe
df_total = pd.concat(dfs, ignore_index=True)

# Guardar el archivo consolidado
df_total.to_csv(base_path + 'datos_prototipos_ficticios.csv', index=False)
print("Archivo consolidado 'datos_prototipos_ficticios.csv' generado correctamente.")
