
def solicitar_nombre():
    """Solicita un nombre que no esté vacío.

    Returns:
        str: Nombre introducido por el usuario.
    """
    while True:
        nombre = input("Introduce tu nombre: ").strip()

        if nombre:
            return nombre

        print("Error: el nombre no puede estar vacío.")


def main():
    """Muestra el nombre en mayúsculas y lo repite según su longitud."""
    nombre = solicitar_nombre()

    print(f"Nombre en mayúsculas: {nombre.upper()}")

    longitud = len(nombre)
    print(f"Número de caracteres: {longitud}")

    for _ in range(longitud):
        print(nombre)


if __name__ == "__main__":
    main()
