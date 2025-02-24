"""
Programa principal para demostrar conceptos musicales,
con énfasis en consonancias y disonancias.
"""

from consonancias import ejemplo_consonancias_completo
from disonancias import ejemplo_disonancias_completo

def mostrar_menu():
    """Muestra el menú principal"""
    print("\nDemostración de Matemáticas en la Música")
    print("=====================================")
    print("\nOpciones:")
    print("1. Consonancias Musicales")
    print("2. Disonancias Musicales")
    print("3. Demostración Completa")
    print("0. Salir")

def ejecutar_demostracion_completa():
    """Ejecuta una demostración completa de consonancias y disonancias"""
    print("\n" + "=" * 60)
    print("DEMOSTRACIÓN COMPLETA: MATEMÁTICAS DE LA CONSONANCIA Y DISONANCIA")
    print("=" * 60)
    
    # Parte 1: Consonancias
    print("\nPARTE 1: CONSONANCIAS")
    print("==================")
    ejemplo_consonancias_completo()
    
    input("\nPresione Enter para continuar con las disonancias...")
    
    # Parte 2: Disonancias
    print("\nPARTE 2: DISONANCIAS")
    print("=================")
    ejemplo_disonancias_completo()
    
    # Conclusión
    print("\nCONCLUSIÓN")
    print("=========")
    print("• Las consonancias se basan en razones simples (2:1, 3:2, etc.)")
    print("• Las disonancias tienen razones más complejas (16:15, √2:1, etc.)")
    print("• La música utiliza la tensión entre ambas para crear expresión")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (0-3): ")
        
        if opcion == "0":
            break
        elif opcion == "1":
            ejemplo_consonancias_completo()
        elif opcion == "2":
            ejemplo_disonancias_completo()
        elif opcion == "3":
            ejecutar_demostracion_completa()
        else:
            print("Opción no válida") 