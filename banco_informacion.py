import streamlit as st
import pandas as pd
import os

# Configuración de rutas
base_path = 'C:/Users/YO/Desktop/DATOSFERA/'

# Función para cargar los datos según la selección
def cargar_datos(sector):
    archivo_csv = os.path.join(base_path, f"{sector}.csv")
    if os.path.exists(archivo_csv):
        return pd.read_csv(archivo_csv)
    else:
        st.error(f"No se encontró el archivo para el sector: {sector}")
        return pd.DataFrame()

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
