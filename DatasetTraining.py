import pandas as pd
import numpy as np

# Crear datos ficticios para los dos entrenamientos: Chatbots y Data Science
# Entrenamiento Chatbots
chatbot_training_data = {
    "Fecha": pd.date_range(start="2024-01-01", periods=10, freq="M"),
    "Tipo de Entrenamiento": ["Intentos", "Entidades", "Flujos", "Diálogos", "Respuesta Automática"] * 2,
    "N° Sesiones": np.random.randint(1, 5, size=10),
    "Progreso (%)": np.random.randint(50, 100, size=10),
    "Evaluación del Usuario (1-5)": np.random.randint(1, 5, size=10)
}

df_chatbot_training = pd.DataFrame(chatbot_training_data)

# Entrenamiento Data Science
ds_training_data = {
    "Fecha": pd.date_range(start="2024-01-01", periods=10, freq="M"),
    "Tema": ["Python", "Análisis de Datos", "Visualización de Datos", "Modelado Predictivo", "Machine Learning"] * 2,
    "Horas de Entrenamiento": np.random.randint(1, 10, size=10),
    "Progreso (%)": np.random.randint(50, 100, size=10),
    "Evaluación del Usuario (1-5)": np.random.randint(1, 5, size=10)
}

df_ds_training = pd.DataFrame(ds_training_data)

# Guardar ambos DataFrames como CSV
df_chatbot_training.to_csv("C:/Users/YO/Desktop/DATOSFERA/chatbot_training.csv", index=False)
df_ds_training.to_csv("C:/Users/YO/Desktop/DATOSFERA/ds_training.csv", index=False)

print("Archivos CSV generados correctamente.")
