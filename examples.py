"""
Ejemplos de uso de las diferentes funcionalidades del proyecto.
"""

from scale_generator import generate_tempered_scale, get_note_frequencies
from tone_generator import reproducir_tono, generate_sine_wave
from interval_player import generar_intervalo, reproducir_intervalo_desde_nota
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

def ejemplo_serie_armonica():
    """
    Demonstración de la serie armónica natural, la base matemática de los tonos musicales.
    Reproduce los primeros 8 armónicos de una nota fundamental.
    """
    print("\nEjemplo 4: Serie Armónica Natural")
    print("================================")
    
    # Frecuencia fundamental (La2 = 110 Hz para mejor audibilidad)
    fundamental = 110.0
    
    print("\nReproduciendo fundamental (110 Hz)")
    reproducir_tono(fundamental, 2.0, amplitud=0.8)
    time.sleep(0.5)
    
    for i in range(2, 9):
        freq = fundamental * i
        print(f"\nArmónico {i}: {freq:.1f} Hz")
        print(f"Razón con fundamental: {i}:1")
        reproducir_tono(freq, 2.0, amplitud=0.8)
        time.sleep(0.5)

def ejemplo_progresion_geometrica():
    """
    Demostración de la progresión geométrica en la escala temperada.
    Muestra cómo cada nota está separada por un factor constante (2^(1/12)).
    """
    print("\nEjemplo 5: Progresión Geométrica en la Escala")
    print("=========================================")
    
    factor = 2 ** (1/12)
    base_freq = 440.0
    
    print(f"Factor entre semitonos consecutivos: {factor:.4f}")
    print("Reproduciendo progresión de 4 notas consecutivas...")
    
    for i in range(4):
        freq = base_freq * (factor ** i)
        print(f"\nNota {i+1}: {freq:.2f} Hz")
        print(f"Factor acumulado: {(factor ** i):.4f}")
        reproducir_tono(freq, 1.0)
        time.sleep(0.5)

def ejemplo_acordes_pitagoricos():
    """
    Demostración de acordes basados en las proporciones pitagóricas.
    Compara acordes con razones simples vs temperados.
    """
    print("\nEjemplo 6: Acordes Pitagóricos vs Temperados")
    print("========================================")
    
    fundamental = 440.0  # La4
    
    # Acorde mayor pitagórico (razones 4:5:6)
    print("\nAcorde mayor con razones puras (4:5:6)")
    tercera_pura = fundamental * 5/4  # 550 Hz
    quinta_pura = fundamental * 3/2    # 660 Hz
    
    t = np.linspace(0, 2.0, int(44100 * 2.0), False)
    acorde_puro = 0.3 * (np.sin(2 * np.pi * fundamental * t) +
                        np.sin(2 * np.pi * tercera_pura * t) +
                        np.sin(2 * np.pi * quinta_pura * t))
    sd.play(acorde_puro, samplerate=44100)
    sd.wait()
    time.sleep(1)
    
    # Acorde mayor temperado
    print("\nAcorde mayor temperado")
    tercera_temp = fundamental * (2 ** (4/12))  # Tercera mayor temperada
    quinta_temp = fundamental * (2 ** (7/12))   # Quinta temperada
    
    acorde_temp = 0.3 * (np.sin(2 * np.pi * fundamental * t) +
                        np.sin(2 * np.pi * tercera_temp * t) +
                        np.sin(2 * np.pi * quinta_temp * t))
    sd.play(acorde_temp, samplerate=44100)
    sd.wait()

def ejemplo_batimentos():
    """
    Demostración de batimentos (beats) entre frecuencias cercanas.
    Este fenómeno matemático explica por qué ciertas combinaciones suenan disonantes.
    """
    print("\nEjemplo 7: Batimentos entre Frecuencias")
    print("====================================")
    
    freq1 = 440.0  # La4
    
    # Demostración con diferentes diferencias de frecuencia
    for diff in [1, 2, 5, 10]:
        freq2 = freq1 + diff
        print(f"\nBatimentos entre {freq1} Hz y {freq2} Hz")
        print(f"Frecuencia de batimento esperada: {diff} Hz")
        
        t = np.linspace(0, 3.0, int(44100 * 3.0), False)
        señal = 0.5 * (np.sin(2 * np.pi * freq1 * t) + np.sin(2 * np.pi * freq2 * t))
        sd.play(señal, samplerate=44100)
        sd.wait()
        time.sleep(1)

def ejemplo_piano_temperado():
    """
    Visualización de la evolución desde la serie armónica hasta el piano temperado.
    """
    print("\nEjemplo 8: De la Serie Armónica al Piano")
    print("=====================================")
    
    def mostrar_piano(notas_destacadas=None):
        """Muestra un piano de dos octavas con notas destacadas"""
        if notas_destacadas is None:
            notas_destacadas = []
        
        teclas_blancas = ["C", "D", "E", "F", "G", "A", "B"]
        teclas_negras = ["C#", "D#", "", "F#", "G#", "A#", ""]
        
        # Teclas negras
        linea = "  "
        for octava in range(2):
            for n in teclas_negras:
                if n == "":
                    linea += "    "
                elif n in notas_destacadas:
                    linea += "█▄█ "
                else:
                    linea += "███ "
        print(linea)
        
        # Teclas blancas
        linea = "  "
        for octava in range(2):
            for n in teclas_blancas:
                if n in notas_destacadas:
                    linea += "▓▓▓▓"
                else:
                    linea += "░░░░"
        print(linea)

    def mostrar_escala_armonica(fundamental=440, num_armonicos=16):
        """Muestra los armónicos y su relación con las notas musicales"""
        print("\nSerie Armónica Natural:")
        print("═" * 60)
        print("Armónico │ Frecuencia │ Razón  │ Nota más cercana")
        print("─" * 60)
        
        for i in range(1, num_armonicos + 1):
            freq = fundamental * i
            # Encontrar la nota más cercana
            semitono = round(12 * np.log2(freq/fundamental)) % 12
            notas = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
            nota = notas[semitono]
            print(f"{i:8d} │ {freq:9.1f} │ {i:1d}:1   │ {nota}")
            
            if i in [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 16]:
                print("─" * 60)

    # 1. Mostrar la serie armónica
    print("\n1. Serie Armónica Natural (primeros 16 armónicos)")
    print("============================================")
    mostrar_escala_armonica(220)  # Usando A3 como fundamental para mejor visualización
    
    # 2. Mostrar cómo los armónicos forman acordes naturales
    print("\n2. Armónicos que forman el acorde mayor natural")
    print("==========================================")
    print("Armónicos 4:5:6 forman un acorde mayor perfecto:")
    print("4º armónico → Fundamental")
    print("5º armónico → Tercera mayor")
    print("6º armónico → Quinta justa")
    mostrar_piano(["C", "E", "G"])
    
    # 3. Mostrar el problema de las quintas
    print("\n3. El Círculo de Quintas Natural")
    print("============================")
    print("Generando notas por quintas perfectas (3:2):")
    quintas = ["C", "G", "D", "A", "E", "B", "F#"]
    for i, nota in enumerate(quintas):
        print(f"Quinta {i+1}: {nota}")
    mostrar_piano(quintas)
    
    # 4. Mostrar la solución temperada
    print("\n4. La Escala Temperada")
    print("===================")
    print("División de la octava en 12 partes iguales:")
    notas_cromaticas = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    for i, nota in enumerate(notas_cromaticas):
        print(f"Semitono {i+1}: {nota}")
    
    # 5. Piano completo
    print("\n5. El Piano Moderno")
    print("================")
    print("Teclas blancas: notas diatónicas (escala de Do mayor)")
    print("Teclas negras: notas cromáticas")
    mostrar_piano()
    
    # 6. Comparación final
    print("\nComparación de intervalos naturales vs temperados:")
    print("============================================")
    print("Quinta natural (3:2):      701.96 cents")
    print("Quinta temperada (2^(7/12): 700.00 cents")
    print("Diferencia (coma pitagórica): 1.96 cents")

if __name__ == "__main__":
    print("Ejemplos de uso del proyecto de música")
    print("=====================================")
    
    while True:
        print("\nSeleccione un ejemplo para ejecutar:")
        print("1. Escala temperada")
        print("2. Intervalos consonantes")
        print("3. Intervalos disonantes")
        print("4. Serie armónica")
        print("5. Progresión geométrica")
        print("6. Acordes pitagóricos")
        print("7. Batimentos")
        print("8. Piano y escala temperada")
        print("0. Salir")
        
        opcion = input("\nIngrese el número del ejemplo (0-8): ")
        
        if opcion == "0":
            break
        elif opcion == "1":
            ejemplo_escala()
        elif opcion == "2":
            ejemplo_consonancias()
        elif opcion == "3":
            ejemplo_disonancias()
        elif opcion == "4":
            ejemplo_serie_armonica()
        elif opcion == "5":
            ejemplo_progresion_geometrica()
        elif opcion == "6":
            ejemplo_acordes_pitagoricos()
        elif opcion == "7":
            ejemplo_batimentos()
        elif opcion == "8":
            ejemplo_piano_temperado()
        else:
            print("Opción no válida") 