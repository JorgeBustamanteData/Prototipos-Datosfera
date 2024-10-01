import streamlit as st
import pandas as pd
import os


# Cargar los archivos CSV de sectores
sectores = ['comercio', 'construccion', 'servicios', 'turismo', 'alimentacion', 'entretenimiento', 'confeccion', 'finanzas', 'educacion', 'transporte', 'agricultura', 'industria', 'automotriz']

# Cargar la información desde los CSV que están en la misma carpeta que la app
df_sectores = {}

for sector in sectores:
    try:
        df_sectores[sector] = pd.read_csv(f'{sector}.csv')
    except FileNotFoundError:
        st.warning(f"Archivo '{sector}.csv' no encontrado.")
        continue

# Título y descripción
st.title("Banco de Información - Datosfera y Jorge Bustamante")
st.write("""
    Bienvenido al banco de información. Selecciona un sector económico para visualizar los datos correspondientes.
""")

# Seleccionar sector
sector_elegido = st.selectbox("Selecciona un sector", sectores)

# Mostrar los datos del sector elegido
if sector_elegido in df_sectores:
    st.write(df_sectores[sector_elegido])
else:
    st.write(f"No se encontró información para el sector {sector_elegido}.")

# Títulos y presentación de la alianza
st.title("Banco de Información de Datosfera")
st.write("Accede a nuestras bases de datos sectoriales y explora los datos que tu empresa necesita.")
st.write("**Alianza con Datosfera**: Consulta o solicita análisis específicos basados en datos obtenidos de fuentes confiables para sectores clave.")
st.write("Selecciona una categoría de datos para comenzar:")

# Opciones de sectores económicos
sectores = ['comercio', 'construccion', 'servicios', 'turismo', 'alimentacion', 'entretenimiento',
            'confeccion', 'finanzas', 'educacion', 'transporte', 'agricultura', 'industria', 'automotriz']

# Menú de selección del sector
sector_seleccionado = st.selectbox("Selecciona un sector económico", sectores)

# Cargar los datos del sector seleccionado
df = cargar_datos(sector_seleccionado)

# Mostrar los datos si están disponibles
if not df.empty:
    st.write(f"**Datos del sector: {sector_seleccionado.capitalize()}**")
    st.dataframe(df)

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

else:
    st.error(f"No se encontraron datos para el sector: {sector_seleccionado}")

# Pie de página
st.write("---")
st.write("**Datosfera - Transformando datos en valor**")
