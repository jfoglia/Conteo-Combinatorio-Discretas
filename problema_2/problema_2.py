import math
from itertools import combinations


def leer_entero(mensaje):
    """Lee un entero válido."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Por favor ingresa un número no negativo.")
                continue
            return valor
        except ValueError:
            print("Error: debes ingresar un número entero.")


def calcular_combinaciones(alfabeto, longitud, repetir):
    """
    Calcula la cantidad de contraseñas posibles.
    """
    if alfabeto <= 0:
        return 0

    if not repetir and longitud > alfabeto:
        return 0

    if repetir:
        return alfabeto ** longitud

    return math.perm(alfabeto, longitud)


def leer_restricciones():
    """
    Lee las restricciones configuradas por el usuario.
    """
    restricciones = []

    if input_invalido("¿Debe contener al menos un dígito? (s/n): ") == "s":
        cantidad = leer_entero("  -> ¿Cuántos dígitos tiene el alfabeto?: ")
        restricciones.append(("Dígitos", cantidad))

    if input_invalido("¿Debe contener al menos una letra mayúscula? (s/n): ") == "s":
        cantidad = leer_entero("  -> ¿Cuántas mayúsculas tiene el alfabeto?: ")
        restricciones.append(("Mayúsculas", cantidad))

    if input_invalido("¿Debe contener al menos un símbolo especial? (s/n): ") == "s":
        cantidad = leer_entero("  -> ¿Cuántos símbolos tiene el alfabeto?: ")
        restricciones.append(("Símbolos", cantidad))

    return restricciones


def input_invalido(entrada):
    while True:
        try:
            valor = input(entrada).strip().lower()
            if valor != "s" and valor != "n":
                print("\npor favor ingresa una respuesta válida.\n")
                continue
            return valor
        except AttributeError:
            print("por favor ingresa una respuesta válida (s/n): ")

        


def validar_restricciones(alfabeto_len, longitud, restricciones):
    """
    Verifica que las restricciones sean consistentes.
    """
    total_categorias = sum(cantidad for _, cantidad in restricciones)

    if total_categorias > alfabeto_len:
        print("\nERROR:")
        print("La suma de las categorías supera el tamaño del alfabeto.")
        return False

    if len(restricciones) > longitud:
        print("\nERROR:")
        print("La longitud de la contraseña es insuficiente para cumplir")
        print("todas las categorías obligatorias.")
        return False

    return True


def aplicar_inclusion_exclusion(
    alfabeto_len,
    longitud,
    repetir,
    restricciones
):
    """
    Aplica el principio de inclusión-exclusión.
    """

    universo = calcular_combinaciones(
        alfabeto_len,
        longitud,
        repetir
    )

    exclusiones_totales = 0

    print("\nDESARROLLO DEL CÁLCULO")
    print("-" * 40)
    print(f"Universo total = {universo}")

    for k in range(1, len(restricciones) + 1):

        signo = 1 if k % 2 != 0 else -1

        for combinacion in combinations(restricciones, k):

            nombres = [nombre for nombre, _ in combinacion]

            caracteres_prohibidos = sum(
                cantidad for _, cantidad in combinacion
            )

            alfabeto_reducido = (
                alfabeto_len - caracteres_prohibidos
            )

            if alfabeto_reducido < 0:
                casos_invalidos = 0
            else:
                casos_invalidos = calcular_combinaciones(
                    alfabeto_reducido,
                    longitud,
                    repetir
                )

            exclusiones_totales += signo * casos_invalidos

            print(
                f"{'Excluir' if signo > 0 else 'Reincluir'} "
                f"{', '.join(nombres)} -> "
                f"{casos_invalidos}"
            )

    resultado_final = universo - exclusiones_totales

    return universo, exclusiones_totales, resultado_final


def crear_grupos():
    """
    Permite al usuario definir grupos personalizados.
    """
    grupos = {}

    while True:

        nombre = input(
            "\nNombre del grupo: "
        ).strip()

        caracteres = input(
            f"Caracteres del grupo '{nombre}': "
        ).strip()

        grupos[nombre] = caracteres

        continuar = input(
            "¿Desea agregar otro grupo? (s/n): "
        ).strip().lower()

        if continuar != "s":
            break

    return grupos


def modo_grupos():
    """
    Maneja la extensión opcional de grupos.
    """

    grupos = crear_grupos()

    tamaño_alfabeto = sum(
        len(caracteres)
        for caracteres in grupos.values()
    )

    print("\nGrupos registrados:")
    for nombre in grupos:
        print(f"- {nombre}")

    print(f"\nTamaño total del alfabeto: {tamaño_alfabeto}")

    longitud = leer_entero(
        "\nIngresa la longitud de la contraseña: "
    )

    repetir = (
        input(
            "¿Está permitida la repetición? (s/n): "
        ).strip().lower() == "s"
    )

    total = calcular_combinaciones(
        tamaño_alfabeto,
        longitud,
        repetir
    )

    print("\n" + "=" * 50)
    print(f"TOTAL DE CONTRASEÑAS POSIBLES: {total}")
    print("=" * 50)


def modo_normal():
    """
    Modo principal solicitado por el ejercicio.
    """

    longitud = leer_entero(
        "Ingresa la longitud de la contraseña: "
    )

    alfabeto_len = leer_entero(
        "Ingresa el tamaño del alfabeto permitido: "
    )

    repetir = (
        input(
            "¿Está permitida la repetición? (s/n): "
        ).strip().lower() == "s"
    )

    restricciones = leer_restricciones()

    if not validar_restricciones(
        alfabeto_len,
        longitud,
        restricciones
    ):
        return

    universo, descartadas, validas = (
        aplicar_inclusion_exclusion(
            alfabeto_len,
            longitud,
            repetir,
            restricciones
        )
    )

    print("\n" + "=" * 50)
    print(f"Contraseñas posibles sin restricciones : {universo}")
    print(f"Contraseñas descartadas                : {descartadas}")
    print(f"CONTRASEÑAS VÁLIDAS FINALES            : {validas}")
    print("=" * 50)


def main():

    print("\n", "=" * 50, sep="")
    print(" Bienvenido al contador de contraseñas")
    print("=" * 50)

    while True:

        agrupacion = input(
            "\n¿Deseas definir grupos de caracteres? (s/n): "
        ).strip().lower()

        if agrupacion == "s":
            modo_grupos()

        elif agrupacion == "n":
            modo_normal()

        else:
            print("Opción no válida.")
            continue

        continuar = input(
            "\n¿Deseas realizar otro cálculo? (s/n): "
        ).strip().lower()

        if continuar != "s":
            print("\nGracias por usar el contador de contraseñas.")
            break


if __name__ == "__main__":
    main()