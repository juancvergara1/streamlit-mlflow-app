import streamlit as st
import pandas as pd
from joblib import load

# Cargar el modelo desde el archivo .pkl
model_path = "gym_workout_modelfinal.pkl"  # Ruta al modelo guardado
loaded_model = load(model_path)

# Título de la aplicación
st.title("Predicción del Tipo de Ejercicio")

# Instrucciones
st.write("Ingresa los detalles a continuación para predecir el tipo de ejercicio que realiza el miembro del gimnasio.")

# Entradas del usuario
st.header("Ingrese los detalles para la predicción:")
age = st.number_input("Edad", min_value=10, max_value=100, value=25)
gender = st.selectbox("Género", options=["Male", "Female"])
weight = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, value=70.0)
height = st.number_input("Altura (m)", min_value=1.0, max_value=2.5, value=1.7)
bmi = weight / (height ** 2)
session_duration = st.number_input("Duración de la Sesión (horas)", min_value=0.1, max_value=5.0, value=1.5)
calories_burned = st.number_input("Calorías Quemadas", min_value=50, max_value=2000, value=500)
max_bpm = st.number_input("Frecuencia Cardíaca Máxima", min_value=50, max_value=220, value=180)
resting_bpm = st.number_input("Frecuencia Cardíaca en Reposo", min_value=30, max_value=100, value=60)

# Crear un DataFrame con las entradas
input_data = pd.DataFrame({
    "Age": [age],
    "Gender": [1 if gender == "Male" else 0],
    "Weight (kg)": [weight],
    "Height (m)": [height],
    "BMI": [bmi],
    "Session_Duration (hours)": [session_duration],
    "Calories_Burned": [calories_burned],
    "Max_BPM": [max_bpm],
    "Resting_BPM": [resting_bpm],
    "Avg_BPM": [(max_bpm + resting_bpm) / 2],  # Ejemplo de cálculo
    "Experience_Level": ["Intermediate"],  # Valor predeterminado
    "Fat_Percentage": [20.0],  # Valor predeterminado
    "Water_Intake (liters)": [2.5],  # Valor predeterminado
    "Workout_Frequency (days/week)": [3],  # Valor predeterminado
})

# Predicción
if st.button("Predecir"):
    try:
        prediction = loaded_model.predict(input_data)
        st.success(f"El modelo predice que el tipo de ejercicio es: {prediction[0]}")
    except Exception as e:
        st.error(f"Ocurrió un error al realizar la predicción: {e}")

