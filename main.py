
from preguntas import (
    validar_respuesta,
    PREGUNTAS,
)

contador_de_respuestas_correctas = 0  # snake_case


for pregunta in PREGUNTAS.keys():
    respuesta = input(pregunta)
    if validar_respuesta(pregunta, respuesta):
        contador_de_respuestas_correctas += 1

print('Acertaste {} pregunta/s'.format(contador_de_respuestas_correctas))
