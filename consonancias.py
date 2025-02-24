"""
Módulo para la demostración y visualización de consonancias musicales.
"""

from interval_player import reproducir_intervalo_desde_nota
import time

def esperar_continuar():
    """Espera a que el usuario presione Enter para continuar"""
    input("\nPresione Enter para continuar con la demostración...")

def mostrar_tabla_razones(fundamental=440.0):
    """Muestra una tabla de razones de frecuencias para intervalos consonantes"""
    print("\nTabla de Razones Consonantes:")
    print("═" * 60)
    print("Intervalo        │ Razón │ Frecuencias     │ Explicación")
    print("─" * 60)
    print(f"Octava          │ 2:1   │ {fundamental:.1f}:{fundamental*2:.1f} │ La consonancia perfecta")
    print(f"Quinta justa    │ 3:2   │ {fundamental:.1f}:{fundamental*3/2:.1f} │ Base del círculo de quintas")
    print(f"Cuarta justa    │ 4:3   │ {fundamental:.1f}:{fundamental*4/3:.1f} │ Inversión de la quinta")
    print(f"Tercera mayor   │ 5:4   │ {fundamental:.1f}:{fundamental*5/4:.1f} │ Base acordes mayores")
    print(f"Tercera menor   │ 6:5   │ {fundamental:.1f}:{fundamental*6/5:.1f} │ Base acordes menores")
    print(f"Sexta mayor     │ 5:3   │ {fundamental:.1f}:{fundamental*5/3:.1f} │ Inversión tercera menor")
    print("─" * 60)
    esperar_continuar()

def demostrar_consonancias_perfectas(fundamental=440.0):
    """Demuestra los intervalos perfectamente consonantes"""
    print("\n1. Intervalos Perfectamente Consonantes")
    print("====================================")
    print("Estos intervalos tienen las razones más simples posibles.")
    esperar_continuar()
    
    # Octava (2:1)
    print("\nOctava (2:1)")
    print("------------")
    print("• La razón más simple posible")
    print("• Base de la percepción musical")
    print("• Las notas suenan tan similares que comparten el mismo nombre")
    esperar_continuar()
    
    # Quinta justa (3:2)
    print("\nQuinta Justa (3:2)")
    print("----------------")
    print("• Segunda razón más simple")
    print("• Fundamental en la música occidental")
    print("• Base del círculo de quintas")
    esperar_continuar()
    
    # Cuarta justa (4:3)
    print("\nCuarta Justa (4:3)")
    print("----------------")
    print("• Complemento de la quinta en la octava")
    print("• Tercera razón más simple")
    print("• Fundamental en melodías")
    esperar_continuar()

def demostrar_consonancias_imperfectas(fundamental=440.0):
    """Demuestra los intervalos imperfectamente consonantes"""
    print("\n2. Intervalos Imperfectamente Consonantes")
    print("======================================")
    print("Estos intervalos tienen razones simples pero más complejas.")
    esperar_continuar()
    
    # Tercera mayor (5:4)
    print("\nTercera Mayor (5:4)")
    print("-----------------")
    print("• Base de los acordes mayores")
    print("• Carácter brillante y estable")
    print("• Primera consonancia 'imperfecta'")
    esperar_continuar()
    
    # Tercera menor (6:5)
    print("\nTercera Menor (6:5)")
    print("-----------------")
    print("• Base de los acordes menores")
    print("• Carácter más melancólico")
    print("• Contraste expresivo con la tercera mayor")
    esperar_continuar()
    
    # Sexta mayor (5:3)
    print("\nSexta Mayor (5:3)")
    print("---------------")
    print("• Inversión de la tercera menor")
    print("• Consonancia amplia y brillante")
    print("• Importante en melodías")
    esperar_continuar()

def visualizar_consonancia(razon_num, razon_den, longitud=50):
    """Visualiza la simplicidad de una razón de frecuencias"""
    simplicidad = 1 / (razon_num + razon_den)
    barras = int(simplicidad * longitud)
    return "█" * barras + "░" * (longitud - barras)

def mostrar_grados_consonancia():
    """Muestra una visualización de los grados de consonancia"""
    print("\nGrados de Consonancia (más barras = más consonante)")
    print("===============================================")
    razones = [
        (2, 1, "Octava     "),
        (3, 2, "Quinta     "),
        (4, 3, "Cuarta     "),
        (5, 4, "3ª Mayor   "),
        (6, 5, "3ª Menor   "),
        (5, 3, "6ª Mayor   ")
    ]
    
    for num, den, nombre in razones:
        print(f"{nombre} ({num}:{den}): {visualizar_consonancia(num, den)}")

def ejemplo_consonancias_completo():
    """Ejemplo completo de consonancias musicales"""
    print("\nDemostración Completa de Consonancias Musicales")
    print("==========================================")
    
    # 1. Mostrar tabla de razones
    mostrar_tabla_razones()
    
    # 2. Demostrar consonancias perfectas
    demostrar_consonancias_perfectas()
    
    # 3. Demostrar consonancias imperfectas
    demostrar_consonancias_imperfectas()
    
    # 4. Visualización de grados de consonancia
    mostrar_grados_consonancia() 