# Función para calcular la clasificación de compromiso de una sesión
# Requisito: Módulo funcional basado en duración y clics

def calcular_clasificacion(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


def main():

    sesiones_clientes = [
        [101, 200, 10],  # Alto
        [102, 45, 12],   # Bajo
        [103, 120, 5],   # Medio
        [104, 190, 2],   # Bajo
        [105, 175, 7]    # Medio
    ]

    print("INFORME DE NIVEL DE COMPROMISO POR SESIÓN")
    print("-" * 45)
    print(f"{'ID Cliente':<15} | {'Clasificación Final'}")
    print("-" * 45)

    for sesion in sesiones_clientes:

        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        resultado = calcular_clasificacion(duracion, clics)

        print(f"{id_cliente:<15} | {resultado}")


if __name__ == "__main__":
    main()