import streamlit as st
import pandas as pd
import os

# Definir los sectores disponibles
sectores = ['comercio', 'construccion', 'servicios', 'turismo', 'alimentacion', 'entretenimiento', 
            'confeccion', 'finanzas', 'educacion', 'transporte', 'agricultura', 'industria', 'automotriz']

# Mostrar título y descripción
st.title("Banco de Información - Datosfera y Jorge Bustamante")
st.write("""
    Bienvenido al banco de información. Selecciona un sector económico para visualizar los datos correspondientes.
""")

# Seleccionar el sector
sector_seleccionado = st.selectbox("Selecciona un sector", sectores)

# Intentar cargar el archivo CSV correspondiente al sector seleccionado
try:
    # Leer el archivo CSV para el sector seleccionado
    df = pd.read_csv(f'{sector_seleccionado}.csv')
    
    # Mostrar los datos del sector si el archivo fue encontrado
    st.write(f"**Mostrando datos del sector: {sector_seleccionado.capitalize()}**")
    st.dataframe(df)  # Mostrar los datos en la tabla

    # Botón para solicitar análisis personalizado
    st.subheader("¿Te interesa un análisis personalizado?")
    st.markdown("Puedes solicitar un estudio detallado o adquirir esta base de datos para tu consulta.")
    
    if st.button("Solicitar Análisis"):
        st.write("¡Gracias por tu interés! Un miembro de nuestro equipo se pondrá en contacto para ofrecerte un análisis personalizado.")
    
    # Mensaje emergente para la compra de base de datos
    st.success(f"¿Te gustaría adquirir la base de datos del sector {sector_seleccionado}? Contáctanos para más información.")
    
    # Explicación de análisis predictivo o insights
    st.subheader("Servicios Adicionales")
    st.write("Ofrecemos más que solo datos. Realiza predicciones, análisis personalizados y estudios a medida sobre los datos que seleccionas.")
    st.markdown("[Conoce más sobre nuestros servicios adicionales](https://tu-dominio.com/servicios)")

    # Simulación de análisis predictivo
    if st.button("Generar Insight Predictivo"):
        if sector_seleccionado == 'comercio':
            st.write("Predicción de crecimiento en comercio para el próximo trimestre: 12%.")
        elif sector_seleccionado == 'finanzas':
            st.write("Insight: Se espera una mejora en la rentabilidad del 8% en los próximos meses en el sector financiero.")
        else:
            st.write("Este sector aún no tiene un análisis predictivo automático. Contáctanos para un análisis específico.")

except FileNotFoundError:
    st.error(f"El archivo para el sector '{sector_seleccionado}' no fue encontrado. Asegúrate de que el archivo '{sector_seleccionado}.csv' esté en la carpeta correcta.")

# Pie de página
st.write("---")
st.write("**Datosfera - Transformando datos en valor**")
