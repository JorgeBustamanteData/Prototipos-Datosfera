import pandas as pd
import numpy as np
import random
import os

# Ruta base para almacenar los archivos CSV
base_path = 'C:/Users/YO/Desktop/DATOSFERA/'

# Función para generar datos ficticios con variedad de columnas
def generar_datos_sector(nombre_sector, n_registros):
    fechas = pd.date_range(start="2023-01-01", end="2023-12-31", periods=n_registros).strftime('%d-%m-%Y')
    
    # Crear columnas específicas según el sector económico
    if nombre_sector == "salud":
        columnas = {
            'Fecha': fechas,
            'Pacientes Atendidos': np.random.randint(50, 300, size=n_registros),
            'Gastos Médicos (USD)': np.random.uniform(1000, 50000, size=n_registros),
            'Personal Médico': np.random.randint(10, 100, size=n_registros)
        }
    elif nombre_sector == "tecnologia":
        columnas = {
            'Fecha': fechas,
            'Proyectos Desarrollados': np.random.randint(1, 20, size=n_registros),
            'Presupuesto (USD)': np.random.uniform(10000, 200000, size=n_registros),
            'Ingenieros Contratados': np.random.randint(5, 50, size=n_registros)
        }
    elif nombre_sector == "comercio":
        columnas = {
            'Fecha': fechas,
            'Ventas (USD)': np.random.uniform(5000, 50000, size=n_registros),
            'Clientes Nuevos': np.random.randint(10, 300, size=n_registros),
            'Promociones Aplicadas': np.random.randint(0, 20, size=n_registros)
        }
    elif nombre_sector == "construccion":
        columnas = {
            'Fecha': fechas,
            'Proyectos Terminados': np.random.randint(1, 10, size=n_registros),
            'Costos Totales (USD)': np.random.uniform(50000, 500000, size=n_registros),
            'Trabajadores en Obra': np.random.randint(20, 500, size=n_registros)
        }
    elif nombre_sector == "servicios":
        columnas = {
            'Fecha': fechas,
            'Clientes Atendidos': np.random.randint(50, 500, size=n_registros),
            'Tiempo de Respuesta (días)': np.random.uniform(1, 10, size=n_registros),
            'Costo del Servicio (USD)': np.random.uniform(100, 1000, size=n_registros)
        }
    elif nombre_sector == "turismo":
        columnas = {
            'Fecha': fechas,
            'Reservas': np.random.randint(10, 200, size=n_registros),
            'Gasto Promedio (USD)': np.random.uniform(200, 3000, size=n_registros),
            'Hoteles Participantes': np.random.randint(1, 50, size=n_registros)
        }
    elif nombre_sector == "alimentacion":
        columnas = {
            'Fecha': fechas,
            'Unidades Vendidas': np.random.randint(1000, 50000, size=n_registros),
            'Gasto Total (USD)': np.random.uniform(10000, 100000, size=n_registros),
            'Restaurantes Afiliados': np.random.randint(5, 100, size=n_registros)
        }
    elif nombre_sector == "entretenimiento":
        columnas = {
            'Fecha': fechas,
            'Espectadores': np.random.randint(100, 10000, size=n_registros),
            'Eventos Realizados': np.random.randint(1, 50, size=n_registros),
            'Ingresos por Entradas (USD)': np.random.uniform(5000, 200000, size=n_registros)
        }
    elif nombre_sector == "confeccion":
        columnas = {
            'Fecha': fechas,
            'Prendas Vendidas': np.random.randint(500, 20000, size=n_registros),
            'Gasto en Materiales (USD)': np.random.uniform(10000, 100000, size=n_registros),
            'Trabajadores Contratados': np.random.randint(10, 200, size=n_registros)
        }
    elif nombre_sector == "finanzas":
        columnas = {
            'Fecha': fechas,
            'Inversiones Realizadas': np.random.randint(5, 100, size=n_registros),
            'Capital Movido (USD)': np.random.uniform(50000, 5000000, size=n_registros),
            'Clientes Nuevos': np.random.randint(10, 500, size=n_registros)
        }
    elif nombre_sector == "educacion":
        columnas = {
            'Fecha': fechas,
            'Estudiantes Inscritos': np.random.randint(100, 5000, size=n_registros),
            'Ingresos Totales (USD)': np.random.uniform(10000, 1000000, size=n_registros),
            'Docentes Contratados': np.random.randint(10, 500, size=n_registros)
        }
    elif nombre_sector == "transporte":
        columnas = {
            'Fecha': fechas,
            'Cargas Transportadas': np.random.randint(100, 10000, size=n_registros),
            'Kilómetros Recorridos': np.random.uniform(500, 10000, size=n_registros),
            'Vehículos Disponibles': np.random.randint(5, 100, size=n_registros)
        }
    elif nombre_sector == "agricultura":
        columnas = {
            'Fecha': fechas,
            'Hectáreas Cosechadas': np.random.uniform(10, 1000, size=n_registros),
            'Toneladas Producidas': np.random.uniform(100, 10000, size=n_registros),
            'Gasto en Fertilizantes (USD)': np.random.uniform(500, 50000, size=n_registros)
        }
    elif nombre_sector == "industria":
        columnas = {
            'Fecha': fechas,
            'Productos Fabricados': np.random.randint(1000, 50000, size=n_registros),
            'Costos de Producción (USD)': np.random.uniform(5000, 100000, size=n_registros),
            'Fábricas Operando': np.random.randint(1, 100, size=n_registros)
        }
    elif nombre_sector == "automotriz":
        columnas = {
            'Fecha': fechas,
            'Vehículos Vendidos': np.random.randint(10, 1000, size=n_registros),
            'Ingresos (USD)': np.random.uniform(50000, 1000000, size=n_registros),
            'Concesionarios Afiliados': np.random.randint(1, 50, size=n_registros)
        }

    df = pd.DataFrame(columnas)
    
    # Guardar en archivo CSV
    csv_file = base_path + f'{nombre_sector}.csv'
    df.to_csv(csv_file, index=False)
    print(f"Archivo '{csv_file}' generado correctamente con {n_registros} registros.")

# Lista de sectores económicos
sectores = [
    'salud', 'tecnologia', 'comercio', 'construccion', 'servicios', 
    'turismo', 'alimentacion', 'entretenimiento', 'confeccion', 
    'finanzas', 'educacion', 'transporte', 'agricultura', 
    'industria', 'automotriz'
]

# Generar datos ficticios para cada sector
n_registros_por_sector = 100  # Número de registros por sector
for sector in sectores:
    generar_datos_sector(sector, n_registros_por_sector)

print("Archivos CSV de todos los sectores generados correctamente.")
