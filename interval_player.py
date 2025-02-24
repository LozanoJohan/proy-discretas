"""
Módulo para la reproducción de intervalos musicales.
"""

import numpy as np
import sounddevice as sd
from tone_generator import generate_sine_wave

def generar_intervalo(freq1, freq2, duracion=2.0, sample_rate=44100, amplitud=0.5):
    """
    Genera y reproduce dos notas simultáneamente.
    
    Args:
        freq1 (float): Frecuencia de la primera nota en Hz
        freq2 (float): Frecuencia de la segunda nota en Hz
        duracion (float): Duración del intervalo en segundos
        sample_rate (int): Tasa de muestreo en Hz
        amplitud (float): Amplitud de cada onda (se divide entre 2 para evitar clipping)
    """
    onda1 = generate_sine_wave(freq1, duracion, sample_rate, amplitud)
    onda2 = generate_sine_wave(freq2, duracion, sample_rate, amplitud)
    onda_combinada = onda1 + onda2
    sd.play(onda_combinada, samplerate=sample_rate)
    sd.wait()

# Definición de intervalos comunes (en semitonos)
INTERVALOS = {
    "unísono": 0,
    "segunda_menor": 1,
    "segunda_mayor": 2,
    "tercera_menor": 3,
    "tercera_mayor": 4,
    "cuarta_justa": 5,
    "tritono": 6,
    "quinta_justa": 7,
    "sexta_menor": 8,
    "sexta_mayor": 9,
    "séptima_menor": 10,
    "séptima_mayor": 11,
    "octava": 12
}

def reproducir_intervalo_desde_nota(nota_base, intervalo, duracion=2.0):
    """
    Reproduce un intervalo desde una nota base.
    
    Args:
        nota_base (float): Frecuencia de la nota base en Hz
        intervalo (str): Nombre del intervalo (debe estar en INTERVALOS)
        duracion (float): Duración del intervalo en segundos
    """
    if intervalo not in INTERVALOS:
        raise ValueError(f"Intervalo no válido. Opciones: {list(INTERVALOS.keys())}")
    
    semitonos = INTERVALOS[intervalo]
    freq2 = nota_base * (2 ** (semitonos / 12))
    generar_intervalo(nota_base, freq2, duracion) 