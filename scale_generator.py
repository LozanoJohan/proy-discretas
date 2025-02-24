"""
Módulo para la generación de escalas musicales temperadas.
"""

import numpy as np

def generate_tempered_scale(base_freq=440, num_notes=12):
    """
    Genera las frecuencias de una escala temperada.
    
    Args:
        base_freq (float): Frecuencia de la nota base (por defecto 440 Hz para La4)
        num_notes (int): Número de notas en la escala (por defecto 12 para una octava)
    
    Returns:
        list: Lista de frecuencias calculadas
    """
    frequencies = [base_freq * (2 ** (i / num_notes)) for i in range(num_notes)]
    return frequencies

# Nombres de notas estándar
NOTE_NAMES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

def get_note_frequencies():
    """
    Obtiene un diccionario de notas y sus frecuencias correspondientes.
    
    Returns:
        dict: Diccionario con nombres de notas como claves y frecuencias como valores
    """
    frequencies = generate_tempered_scale()
    return dict(zip(NOTE_NAMES, frequencies)) 