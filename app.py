import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os


# Verificar si el archivo existe en el repositorio
if os.path.exists('datos_prototipos_ficticios.csv'):
    df_total = pd.read_csv('datos_prototipos_ficticios.csv')
    st.write("Archivo cargado correctamente.")
else:
    st.write("Error: No se encontró el archivo 'datos_prototipos_ficticios.csv'.")


# Corregir formato de fecha
df_total['Fecha'] = pd.to_datetime(df_total['Fecha'], errors='coerce', format='%Y-%m-%d %H:%M:%S.%f')

# Si no se logra con microsegundos, intentamos un formato ISO estándar
df_total['Fecha'] = df_total['Fecha'].fillna(pd.to_datetime(df_total['Fecha'], errors='coerce', format='%Y-%m-%d'))

# Mostrar título y descripción
st.title("Visualización de Prototipos - Datosfera y Jorge Bustamante")
st.write("""
    Esta demostración muestra diferentes bases de datos ficticias generadas a partir de un sistema ERP como Odoo. 
    Explora los indicadores y gráficos para entender cómo estas métricas pueden impactar tu negocio.
""")

# Seleccionar la base de datos
base_datos = st.selectbox("Selecciona la base de datos", df_total['Categoria'].unique())

# Filtrar los datos según la base de datos seleccionada
df_filtrado = df_total[df_total['Categoria'] == base_datos]

# Identificar las columnas relevantes para la base de datos seleccionada
if base_datos == 'ventas':
    columnas_relevantes = ['Fecha', 'Ventas (USD)', 'Clientes Nuevos', 'Promedio de Pedido (USD)', 'Net Promoter Score (NPS)']
    tipo_grafico = 'barras'
elif base_datos == 'marketing':
    columnas_relevantes = ['Fecha', 'Gasto Publicitario (USD)', 'Conversiones', 'ROI (%)']
    tipo_grafico = 'histograma'
elif base_datos == 'contabilidad':
    columnas_relevantes = ['Fecha', 'Ventas (USD)', 'Clientes Nuevos', 'Promedio de Pedido (USD)', 'Net Promoter Score (NPS)', 'Utilidad Bruta (USD)']
    tipo_grafico = 'area'
elif base_datos == 'recursos_humanos':
    columnas_relevantes = ['Fecha', 'Tasa de Retención', 'Satisfacción del Empleado']
    tipo_grafico = 'barras'
elif base_datos == 'logistica':
    columnas_relevantes = ['Fecha', 'Órdenes Procesadas', 'Costos de Envío', 'Tiempo de Entrega']
    tipo_grafico = 'linea'

# Mostrar la tabla con los datos filtrados
st.write(df_filtrado[columnas_relevantes])

# Seleccionar una métrica para graficar
metrica = st.selectbox("Selecciona la métrica para visualizar", columnas_relevantes[1:])

# Gráfico dinámico en función de la métrica seleccionada con diferentes tipos de gráficos
if tipo_grafico == 'barras':
    fig = px.bar(df_filtrado, x='Fecha', y=metrica, title=f'Tendencia de {metrica} en el tiempo')
elif tipo_grafico == 'linea':
    fig = px.line(df_filtrado, x='Fecha', y=metrica, title=f'Tendencia de {metrica} en el tiempo')
elif tipo_grafico == 'histograma':
    fig = px.histogram(df_filtrado, x='Fecha', y=metrica, title=f'Distribución de {metrica}')
elif tipo_grafico == 'area':
    fig = px.area(df_filtrado, x='Fecha', y=metrica, title=f'Área de {metrica} a lo largo del tiempo')

st.plotly_chart(fig)

# Análisis predictivo o insight cualitativo
if st.button('Aplicar Análisis Predictivo'):
    if metrica in ['Ventas (USD)', 'Utilidad Bruta (USD)', 'Costos de Envío']:
        # Preparar los datos para el modelo predictivo
        df_filtrado['Fecha_num'] = pd.to_datetime(df_filtrado['Fecha'], errors='coerce').map(pd.Timestamp.toordinal)
        X = df_filtrado[['Fecha_num']]
        y = df_filtrado[metrica]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Modelo de regresión lineal
        modelo = LinearRegression()
        modelo.fit(X_train, y_train)

        # Predicción
        predicciones = modelo.predict(X_test)

        # Mostrar los resultados del análisis predictivo
        st.write(f"Predicciones para {metrica} en las fechas futuras:")
        resultados = pd.DataFrame({
            'Fecha': pd.to_datetime(X_test['Fecha_num'].map(pd.Timestamp.fromordinal)),
            'Predicción': predicciones
        })
        st.write(resultados)
    else:
        # Si no es una métrica numérica para predicción, proporcionar un insight cualitativo
        if metrica == 'Net Promoter Score (NPS)':
            st.write("El NPS es un indicador importante de la satisfacción del cliente. Un alto NPS puede indicar fidelidad del cliente, mientras que un bajo NPS puede señalar áreas de mejora en la experiencia del cliente.")
        elif metrica == 'Tasa de Retención':
            st.write("La tasa de retención es crítica en recursos humanos. Una tasa alta refleja la capacidad de la empresa para mantener a sus empleados, lo cual es esencial para reducir los costos asociados a la rotación de personal.")
        elif metrica == 'Satisfacción del Empleado':
            st.write("La satisfacción del empleado es clave para la productividad. Un ambiente de trabajo positivo y oportunidades de crecimiento son fundamentales para mantener altos niveles de satisfacción.")
        elif metrica == 'Conversiones':
            st.write("Las conversiones son un indicador clave de éxito en marketing. Un alto número de conversiones sugiere que las campañas publicitarias están atrayendo clientes potenciales y convirtiéndolos en compradores.")
        elif metrica == 'Órdenes Procesadas':
            st.write("El número de órdenes procesadas refleja la eficiencia de las operaciones logísticas. Un aumento en este indicador puede sugerir una mejora en los tiempos de procesamiento y en la satisfacción del cliente.")
        else:
            st.write(f"Esta métrica ({metrica}) no permite un análisis predictivo directo, pero es importante monitorearla para mantener una perspectiva estratégica.")
