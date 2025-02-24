"""
Módulo para la demostración y visualización de disonancias musicales.
"""

from interval_player import reproducir_intervalo_desde_nota
import time

def esperar_continuar():
    """Espera a que el usuario presione Enter para continuar"""
    input("\nPresione Enter para continuar con la demostración...")

def mostrar_tabla_razones_disonantes(fundamental=440.0):
    """Muestra una tabla de razones de frecuencias para intervalos disonantes"""
    print("\nTabla de Razones Disonantes:")
    print("═" * 60)
    print("Intervalo        │ Razón  │ Explicación")
    print("─" * 60)
    print("Segunda menor    │ 16:15  │ Semitono cromático, máxima tensión")
    print("Segunda mayor    │ 9:8    │ Tono entero, disonancia suave")
    print("Séptima menor    │ 16:9   │ Disonancia expresiva (blues/jazz)")
    print("Tritono         │ √2:1   │ División exacta de la octava")
    print("─" * 60)
    esperar_continuar()

def demostrar_disonancias_suaves(fundamental=440.0):
    """Demuestra los intervalos con disonancia suave"""
    print("\n1. Disonancias Suaves")
    print("===================")
    print("Estos intervalos crean tensión moderada y movimiento musical.")
    esperar_continuar()
    
    # Segunda mayor (9:8)
    print("\nSegunda Mayor (9:8)")
    print("-----------------")
    print("• Intervalo melódico básico")
    print("• Disonancia constructiva")
    print("• Base del movimiento melódico")
    esperar_continuar()
    
    # Séptima menor (16:9)
    print("\nSéptima Menor (16:9)")
    print("------------------")
    print("• Disonancia expresiva")
    print("• Característica del blues y jazz")
    print("• Crea tensión que busca resolver")
    esperar_continuar()

def demostrar_disonancias_fuertes(fundamental=440.0):
    """Demuestra los intervalos con disonancia fuerte"""
    print("\n2. Disonancias Fuertes")
    print("====================")
    print("Estos intervalos crean máxima tensión y conflicto sonoro.")
    esperar_continuar()
    
    # Segunda menor (16:15)
    print("\nSegunda Menor (16:15)")
    print("-------------------")
    print("• Mínima distancia entre notas")
    print("• Máxima tensión cromática")
    print("• Razón muy compleja")
    esperar_continuar()
    
    # Tritono (√2:1)
    print("\nTritono (√2:1)")
    print("-------------")
    print("• 'Diabolus in Musica'")
    print("• Divide la octava exactamente a la mitad")
    print("• La disonancia más inestable")
    esperar_continuar()

def visualizar_disonancia(complejidad, longitud=50):
    """Visualiza el grado de disonancia"""
    barras = int((complejidad / 10) * longitud)
    return "█" * barras + "░" * (longitud - barras)

def mostrar_grados_disonancia():
    """Muestra una visualización de los grados de disonancia"""
    print("\nGrados de Disonancia (más barras = más disonante)")
    print("============================================")
    intervalos = [
        (3, "Segunda mayor  "),
        (5, "Séptima menor "),
        (7, "Segunda menor "),
        (9, "Tritono       ")
    ]
    
    for nivel, nombre in intervalos:
        print(f"{nombre}: {visualizar_disonancia(nivel)}")

def ejemplo_disonancias_completo():
    """Ejemplo completo de disonancias musicales"""
    print("\nDemostración Completa de Disonancias Musicales")
    print("=========================================")
    
    # 1. Mostrar tabla de razones
    mostrar_tabla_razones_disonantes()
    
    # 2. Demostrar disonancias suaves
    demostrar_disonancias_suaves()
    
    # 3. Demostrar disonancias fuertes
    demostrar_disonancias_fuertes()
    
    # 4. Visualización de grados de disonancia
    mostrar_grados_disonancia()
    
    # 5. Mostrar comparación visual
    print("\nComparación Visual de Tensión Musical:")
    print("===================================")
    print("Consonancia perfecta (quinta justa):")
    print("░" * 50)
    print("Disonancia suave (segunda mayor):")
    print("░" * 30 + "█" * 20)
    print("Disonancia fuerte (tritono):")
    print("█" * 50) 