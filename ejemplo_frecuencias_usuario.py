"""
Ejemplo de generación de sonido con frecuencias ingresadas por el usuario.
"""

from interval_player import generar_intervalo

def ejemplo_frecuencias_usuario():
    """
    Permite al usuario ingresar dos frecuencias y escuchar el sonido resultante.
    Las frecuencias deben estar entre 200 Hz y 2000 Hz (rango audible humano).
    """
    print("\nEjemplo de Generación de Sonido con Frecuencias Personalizadas")
    print("=" * 60)
    print("\nIngrese dos frecuencias entre 200 Hz y 2000 Hz para generar un sonido.")
    print("Este ejemplo le permitirá explorar diferentes combinaciones de frecuencias.")
    
    while True:
        try:
            # Solicitar primera frecuencia
            freq1 = float(input("\nIngrese la primera frecuencia (Hz): "))
            if not 200 <= freq1 <= 2000:
                print("Error: La frecuencia debe estar entre 200 Hz y 2000 Hz")
                continue
                
            # Solicitar segunda frecuencia
            freq2 = float(input("Ingrese la segunda frecuencia (Hz): "))
            if not 200 <= freq2 <= 2000:
                print("Error: La frecuencia debe estar entre 200 Hz y 2000 Hz")
                continue
            
            # Mostrar información sobre la razón de frecuencias
            ratio = max(freq1, freq2) / min(freq1, freq2)
            print(f"\nRazón de frecuencias: {ratio:.3f}")
            print("(Las razones más simples tienden a sonar más consonantes)")
            
            # Generar y reproducir el intervalo
            print("\nReproduciendo sonido...")
            generar_intervalo(freq1, freq2, duracion=3.0)
            
            # Preguntar si desea continuar
            continuar = input("\n¿Desea probar otras frecuencias? (s/n): ").lower()
            if continuar != 's':
                break
                
        except ValueError:
            print("Error: Por favor ingrese un número válido")
        except Exception as e:
            print(f"Error inesperado: {e}")
            break
    
    print("\n¡Gracias por explorar las frecuencias musicales!")

if __name__ == "__main__":
    ejemplo_frecuencias_usuario() 