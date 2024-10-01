import streamlit as st
import pandas as pd
import plotly.express as px

# Títulos y descripción de la página
st.title("🎓 Prototipo de Entrenamiento")
st.markdown("""
**Bienvenido al módulo de entrenamiento interactivo. Aquí puedes explorar los datos de los cursos de Chatbots y Data Science ofrecidos por nuestra alianza con Datosfera.**  
Elige un tipo de entrenamiento para visualizar el progreso y obtener insights adicionales sobre los contenidos abordados.
""")

# Añadir una imagen representativa de entrenamiento
st.image("C:/Users/YO/Desktop/DATOSFERA/entrenamiento_banner.png", caption="Entrenamiento en Chatbots y Data Science", use_column_width=True)

# Selección de tipo de entrenamiento
tipo_entrenamiento = st.selectbox("Selecciona el tipo de entrenamiento", ["Chatbots", "Data Science"])

# Cargar los datasets correspondientes
if tipo_entrenamiento == "Chatbots":
    st.subheader("🚀 Progreso del Entrenamiento en Chatbots")
    st.markdown("""
    El curso de **Chatbots** cubre las siguientes áreas clave:
    - **Diseño de Conversaciones**: Cómo estructurar interacciones conversacionales efectivas.
    - **Entrenamiento de Modelos NLP**: Uso de NLP para mejorar la precisión de respuestas.
    - **Integración con Plataformas**: Automatización y despliegue en plataformas como WhatsApp y Facebook.
    """)
    
    df = pd.read_csv("C:/Users/YO/Desktop/DATOSFERA/chatbot_training.csv")
    st.write(df)
    
    # Visualización gráfica del progreso
    fig = px.bar(df, x="Tipo de Entrenamiento", y="Progreso (%)", color="N° Sesiones", title="Progreso por Tipo de Entrenamiento", 
                 text="Progreso (%)", height=400)
    fig.update_layout(xaxis_title="Tipo de Entrenamiento", yaxis_title="Progreso (%)")
    st.plotly_chart(fig)
    
elif tipo_entrenamiento == "Data Science":
    st.subheader("📊 Progreso del Entrenamiento en Data Science")
    st.markdown("""
    El curso de **Data Science** cubre los siguientes temas clave:
    - **Análisis Exploratorio de Datos**: Técnicas para entender mejor los datos.
    - **Modelado Predictivo**: Creación de modelos de predicción.
    - **Visualización de Datos**: Herramientas para generar gráficos y reportes visuales.
    - **Machine Learning**: Implementación de algoritmos de aprendizaje automático.
    """)
    
    df = pd.read_csv("C:/Users/YO/Desktop/DATOSFERA/ds_training.csv")
    st.write(df)
    
    # Visualización gráfica del progreso
    fig = px.bar(df, x="Tema", y="Progreso (%)", color="Horas de Entrenamiento", title="Progreso por Tema de Entrenamiento", 
                 text="Progreso (%)", height=400)
    fig.update_layout(xaxis_title="Tema", yaxis_title="Progreso (%)")
    st.plotly_chart(fig)

# Insighst adicionales
st.markdown("""
## 🎯 Insights y Próximos Pasos
Nuestros sistemas de entrenamiento te permiten seguir el progreso de cada sesión y medir los resultados obtenidos. 

- **Análisis Personalizado**: Ofrecemos un análisis detallado del desempeño de cada participante.
- **Mejoras en el Proceso de Entrenamiento**: Sugerimos áreas de mejora en función de las métricas de progreso.
- **Automatización del Seguimiento**: Herramientas avanzadas para evaluar el aprendizaje a lo largo del tiempo.

👉 Contacta con nosotros para más información sobre entrenamientos personalizados.
""")

# Barra de progreso global
total_progreso = df["Progreso (%)"].mean()
st.progress(total_progreso / 100)

# Pie de página con imagen alusiva a la alianza
st.image("C:/Users/YO/Desktop/DATOSFERA/alianza_datosfera.png", caption="Automatización y Entrenamiento con Datosfera", use_column_width=True)
