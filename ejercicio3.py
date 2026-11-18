def solicitar_entero():
    """Solicita un número entero mayor o igual que 2.

    Returns:
        int: Número entero válido introducido.
    """
    while True:
        try:
            numero = int(input("Introduce un número entero: "))

            if numero < 2:
                raise ValueError("El número debe ser mayor o igual que 2.")

            return numero

        except ValueError as error:
            print(f"Error: {error}")


def obtener_pares(limite):
    """Obtiene los números pares desde 2 hasta el límite.

    Args:
        limite (int): Número máximo del intervalo.

    Returns:
        list: Lista de números pares.
    """
    # Devuelve una lista de números pares utilizando range() con step 2
    return list(range(2, limite + 1, 2))


def main():
    """Solicita un número y muestra los números pares."""
    limite = solicitar_entero()

    pares = obtener_pares(limite)

    print(f"Números pares del 2 al {limite}:")

    for numero in pares:
        print(numero)


if __name__ == "__main__":
    main()
