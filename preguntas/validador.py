from .preguntas import PREGUNTAS


def validar_respuesta(pregunta, respuesta):
    respuesta = respuesta.lower()
    if PREGUNTAS[pregunta] == respuesta:
        return True
    return False
