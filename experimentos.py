import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import io

# Título principal con la alianza y diseño más atractivo
st.title("💡 Prototipo de Experimentación Empresarial")
st.subheader("Una herramienta de **análisis empresarial** creada en alianza con **Datosfera**")

# Breve descripción sobre el propósito del prototipo
st.write("""
Bienvenido al Prototipo de Experimentación, diseñado para ayudar a las empresas a **optimizar procesos**
y tomar decisiones basadas en **datos reales**. Aquí podrás simular diferentes experimentos y observar 
cómo tus decisiones pueden afectar los resultados de tu negocio.
""")

# Separador estético
st.markdown("---")

# Selección del tipo de experimento con mayor explicación didáctica
st.header("🔬 Simulación de Experimentos")
st.write("""
Elige el tipo de experimento que deseas realizar:
""")
tipo_experimento = st.selectbox("Selecciona el tipo de experimento:", 
                                ["A/B Testing", "Multivariable", "Comparación de Escenarios"])

# Definición del objetivo de la experimentación con más detalles explicativos
st.header("🎯 Objetivos y Métricas")
st.write("""
Selecciona qué objetivo deseas optimizar en tu experimento. Esto puede ir desde el **aumento de ventas**, 
la **reducción de costos**, o incluso la **mejora en la satisfacción del cliente**.
""")
objetivo = st.selectbox("Selecciona el objetivo que deseas optimizar:",
                        ["Aumentar Ventas", "Reducir Costos", "Mejorar Satisfacción del Cliente", 
                         "Reducir Tiempo de Entrega"])

# Variables clave para modificar en el experimento
st.write("### Define las variables que quieres modificar:")
if tipo_experimento == "A/B Testing":
    st.write("Vas a comparar dos variantes para ver cuál ofrece el mejor resultado.")
    variable_1 = st.slider("Variable A", min_value=0.0, max_value=100.0, value=50.0)
    variable_2 = st.slider("Variable B", min_value=0.0, max_value=100.0, value=50.0)
else:
    st.write("Selecciona las variables que deseas modificar en tu experimento:")
    variable_1 = st.slider("Variable 1", min_value=0.0, max_value=100.0, value=50.0)
    variable_2 = st.slider("Variable 2", min_value=0.0, max_value=100.0, value=50.0)
    variable_3 = st.slider("Variable 3", min_value=0.0, max_value=100.0, value=50.0)

# Botón para simular los resultados
if st.button("🚀 Simular Resultados"):
    # Generar datos ficticios para la simulación
    np.random.seed(42)  # Semilla para reproducibilidad
    resultados = {
        "Escenario": ["Variable A/B", "Variable 1", "Variable 2", "Variable 3"],
        "Impacto en Ventas (%)": np.random.uniform(-10, 20, size=4),
        "Impacto en Costos (%)": np.random.uniform(-5, 15, size=4),
        "Satisfacción del Cliente (%)": np.random.uniform(50, 95, size=4)
    }
    
    df_resultados = pd.DataFrame(resultados)
    
    # Mostrar los resultados en una tabla
    st.success("Resultados del experimento:")
    st.dataframe(df_resultados)
    
    # Visualización gráfica mejorada
    fig = px.bar(df_resultados, x="Escenario", y=["Impacto en Ventas (%)", "Impacto en Costos (%)"], 
                 barmode="group", title="📊 Impacto en Ventas y Costos por Escenario", 
                 color_discrete_sequence=px.colors.qualitative.Vivid)
    st.plotly_chart(fig)
    
    # Recomendaciones automáticas
    st.subheader("💡 Recomendaciones:")
    if df_resultados["Impacto en Ventas (%)"].max() > 10:
        st.write("🔍 **Recomendación**: Continúa con la Variable A/B, ya que generó el mayor impacto positivo en ventas.")
    elif df_resultados["Impacto en Costos (%)"].min() < 0:
        st.write("🔍 **Recomendación**: La Variable 3 mostró una reducción significativa de costos. Considera optimizar en esa dirección.")
    else:
        st.write("🔍 **Recomendación**: Ninguna variable tuvo un impacto destacado. Revisa las estrategias antes de implementar cambios.")

# Mejoras estéticas para los reportes
st.subheader("📄 Generación de Reportes")
st.write("Puedes descargar los resultados de tu experimento en formato CSV.")

# Botón para descargar reporte CSV
csv_buffer = io.StringIO()
df_resultados.to_csv(csv_buffer, index=False)

st.download_button(
    label="📥 Descargar Reporte en CSV",
    data=csv_buffer.getvalue(),
    file_name="resultados_experimento.csv",
    mime="text/csv",
)

# Pie de página con la alianza
st.markdown("---")
st.markdown("**Este prototipo fue desarrollado por Datosfera en colaboración con Jorge Bustamante**. \nConvierta sus datos en decisiones empresariales estratégicas.")
st.write("Desarrollado con ❤️ y 💻 por Datosfera")

