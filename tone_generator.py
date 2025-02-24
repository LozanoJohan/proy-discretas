"""
Módulo para la generación y reproducción de tonos musicales.
"""

import numpy as np
import sounddevice as sd

def generate_sine_wave(frecuencia, duracion=1.0, sample_rate=44100, amplitud=1.0):
    """
    Genera una onda sinusoidal.
    
    Args:
        frecuencia (float): Frecuencia del tono en Hz
        duracion (float): Duración del tono en segundos
        sample_rate (int): Tasa de muestreo en Hz
        amplitud (float): Amplitud de la onda (0.0 a 1.0)
    
    Returns:
        numpy.ndarray: Array con la forma de onda generada
    """
    t = np.linspace(0, duracion, int(sample_rate * duracion), False)
    return amplitud * np.sin(2 * np.pi * frecuencia * t)

def reproducir_tono(frecuencia, duracion=1.0, sample_rate=44100, amplitud=1.0, wait=True):
    """
    Genera y reproduce un tono puro.
    
    Args:
        frecuencia (float): Frecuencia del tono en Hz
        duracion (float): Duración del tono en segundos
        sample_rate (int): Tasa de muestreo en Hz
        amplitud (float): Amplitud de la onda (0.0 a 1.0)
        wait (bool): Esperar a que termine la reproducción
    """
    onda = generate_sine_wave(frecuencia, duracion, sample_rate, amplitud)
    sd.play(onda, samplerate=sample_rate)
    if wait:
        sd.wait() 