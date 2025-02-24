"""
Ejemplos de uso de las diferentes funcionalidades del proyecto.
"""

from scale_generator import generate_tempered_scale, get_note_frequencies
from tone_generator import reproducir_tono, generate_sine_wave
from interval_player import generar_intervalo, reproducir_intervalo_desde_nota
from ejemplo_frecuencias_usuario import ejemplo_frecuencias_usuario
import numpy as np
import sounddevice as sd
import time

def esperar_sonido():
    """Espera a que el usuario presione Enter después de un sonido"""
    input("\nPresione Enter para escuchar el siguiente sonido...")

def ejemplo_escala():
    """Ejemplo de generación y reproducción de una escala temperada"""
    print("\nEjemplo 1: Reproduciendo escala temperada")
    frequencies = generate_tempered_scale()
    note_names = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    
    for name, freq in zip(note_names, frequencies):
        print(f"Nota {name}: {freq:.2f} Hz")
        reproducir_tono(freq, 0.5)
        time.sleep(0.1)

def ejemplo_consonancias():
    """
    Ejemplo detallado de intervalos consonantes en la música.
    Demuestra los intervalos más agradables al oído y sus razones matemáticas.
    """
    print("\nEjemplo 2: Intervalos Consonantes")
    print("==============================")
    print("Los intervalos consonantes son aquellos que tienen razones de frecuencia simples.")
    print("Cuanto más simple es la razón, más consonante es el intervalo.")
    
    # Nota base: La4 (A4)
    la4 = 440.0
    
    # 1. Intervalos perfectamente consonantes
    print("\n1. Intervalos Perfectamente Consonantes:")
    print("----------------------------------------")
    
    print("\nOctava (A3-A4) - La consonancia más perfecta")
    print("Razón de frecuencias 2:1 - La más simple posible")
    print("Esta simplicidad explica por qué las notas suenan 'igual' pero más agudas/graves")
    reproducir_intervalo_desde_nota(la4/2, "octava", 3.0)
    esperar_sonido()
    
    print("\nQuinta justa (A-E) - Segunda consonancia más importante")
    print("Razón de frecuencias 3:2 - Base del círculo de quintas")
    print("Fundamental en la música occidental y la afinación pitagórica")
    reproducir_intervalo_desde_nota(la4, "quinta_justa", 3.0)
    esperar_sonido()
    
    print("\nCuarta justa (A-D) - Tercera consonancia más importante")
    print("Razón de frecuencias 4:3")
    print("Complemento de la quinta en la octava")
    reproducir_intervalo_desde_nota(la4, "cuarta_justa", 3.0)
    esperar_sonido()
    
    # 2. Intervalos imperfectamente consonantes
    print("\n2. Intervalos Imperfectamente Consonantes:")
    print("----------------------------------------")
    
    print("\nTercera mayor (A-C#) - Consonancia dulce y brillante")
    print("Razón de frecuencias 5:4 - Base de los acordes mayores")
    reproducir_intervalo_desde_nota(la4, "tercera_mayor", 3.0)
    esperar_sonido()
    
    print("\nTercera menor (A-C) - Consonancia más melancólica")
    print("Razón de frecuencias 6:5 - Base de los acordes menores")
    reproducir_intervalo_desde_nota(la4, "tercera_menor", 3.0)
    esperar_sonido()
    
    print("\nSexta mayor (A-F#) - Consonancia amplia y brillante")
    print("Inversión de la tercera menor")
    reproducir_intervalo_desde_nota(la4, "sexta_mayor", 3.0)
    esperar_sonido()

def ejemplo_disonancias():
    """
    Ejemplo detallado de intervalos disonantes en la música.
    Demuestra los intervalos más tensos y sus características matemáticas.
    """
    print("\nEjemplo 3: Intervalos Disonantes")
    print("============================")
    print("Los intervalos disonantes tienen razones de frecuencia más complejas.")
    print("La complejidad de estas razones genera tensión y 'rudeza' en el sonido.")
    
    # Nota base: La4 (A4)
    la4 = 440.0
    
    # 1. Disonancias suaves
    print("\n1. Disonancias Suaves:")
    print("---------------------")
    
    print("\nSegunda mayor (A-B) - Disonancia suave")
    print("Intervalo fundamental en melodías")
    print("La tensión suave crea movimiento musical")
    reproducir_intervalo_desde_nota(la4, "segunda_mayor", 3.0)
    esperar_sonido()
    
    print("\nSéptima menor (A-G) - Disonancia expresiva")
    print("Crucial en el blues y jazz")
    print("Crea una tensión que 'quiere' resolver a la tercera")
    reproducir_intervalo_desde_nota(la4, "séptima_menor", 3.0)
    esperar_sonido()
    
    # 2. Disonancias fuertes
    print("\n2. Disonancias Fuertes:")
    print("----------------------")
    
    print("\nSegunda menor (A-A#) - Disonancia intensa")
    print("Intervalo cromático, muy cercano y tenso")
    print("Razón aproximada 16:15 - Muy compleja")
    reproducir_intervalo_desde_nota(la4, "segunda_menor", 3.0)
    esperar_sonido()
    
    print("\nTritono (A-D#) - La disonancia más fuerte")
    print("Históricamente conocido como 'Diabolus in Musica'")
    print("Divide la octava exactamente a la mitad")
    reproducir_intervalo_desde_nota(la4, "tritono", 3.0)
    esperar_sonido()
    
    # 3. Demostración de contraste
    print("\n3. Demostración de Contraste:")
    print("--------------------------")
    print("\nAlternando entre consonancia perfecta y disonancia máxima:")
    
    for _ in range(2):
        print("Quinta justa (consonante)...")
        reproducir_intervalo_desde_nota(la4, "quinta_justa", 2.0)
        esperar_sonido()
        print("Tritono (disonante)...")
        reproducir_intervalo_desde_nota(la4, "tritono", 2.0)
        esperar_sonido()

if __name__ == "__main__":
    print("Ejemplos de uso del proyecto de música")
    print("=====================================")
    
    while True:
        print("\nSeleccione un ejemplo para ejecutar:")
        print("1. Escala temperada")
        print("2. Intervalos consonantes")
        print("3. Intervalos disonantes")
        print("4. Frecuencias personalizadas")
        print("0. Salir")
        
        opcion = input("\nIngrese el número del ejemplo (0-4): ")
        
        if opcion == "0":
            break
        elif opcion == "1":
            ejemplo_escala()
        elif opcion == "2":
            ejemplo_consonancias()
        elif opcion == "3":
            ejemplo_disonancias()
        elif opcion == "4":
            ejemplo_frecuencias_usuario()
        else:
            print("Opción no válida") 