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
    "unísono": 0,        # 1:1    = 2^(0/12)
    "segunda_menor": 1,   # 16:15  ≈ 2^(1/12)
    "segunda_mayor": 2,   # 9:8    ≈ 2^(2/12)
    "tercera_menor": 3,   # 6:5    ≈ 2^(3/12)
    "tercera_mayor": 4,   # 5:4    ≈ 2^(4/12)
    "cuarta_justa": 5,   # 4:3    ≈ 2^(5/12)
    "tritono": 6,        # √2:1   = 2^(6/12)
    "quinta_justa": 7,   # 3:2    ≈ 2^(7/12)
    "sexta_menor": 8,    # 8:5    ≈ 2^(8/12)
    "sexta_mayor": 9,    # 5:3    ≈ 2^(9/12)
    "séptima_menor": 10, # 16:9   ≈ 2^(10/12)
    "séptima_mayor": 11, # 15:8   ≈ 2^(11/12)
    "octava": 12         # 2:1    = 2^(12/12)
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