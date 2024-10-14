import streamlit as st
import random

# Función para generar un ejercicio de cinemática
def generar_ejercicio():
    velocidad = random.randint(5, 20)  # Velocidad en m/s
    tiempo = random.randint(2, 10)     # Tiempo en segundos
    distancia = velocidad * tiempo     # Distancia calculada
    return velocidad, tiempo, distancia

# Generar un nuevo ejercicio
velocidad, tiempo, distancia_correcta = generar_ejercicio()

# Mostrar el ejercicio al usuario
st.title("Ejercicios de Cinemática")
st.write(f"Un objeto se mueve a una velocidad de {velocidad} m/s durante {tiempo} segundos.")
st.write("¿Cuál es la distancia recorrida por el objeto?")

# Entrada para la respuesta del usuario
respuesta_usuario = st.number_input("Ingresa tu respuesta (en metros):", min_value=0)

# Botón para verificar la respuesta
if st.button("Verificar respuesta"):
    if respuesta_usuario == distancia_correcta:
        st.success("¡Correcto! 🎉 La distancia recorrida es de {} metros.".format(distancia_correcta))
    else:
        st.error("Incorrecto. La respuesta correcta es {} metros.".format(distancia_correcta))
