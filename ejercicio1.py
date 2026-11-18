from datetime import date


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


def solicitar_nacimiento():
    """Solicita un año de nacimiento válido.

    Returns:
        int: Año de nacimiento introducido.
    """
    while True:
        try:
            year = int(input("Introduce tu año de nacimiento: "))

            year_actual = date.today().year

            if not 1900 <= year <= year_actual:
                raise ValueError(
                    f"El año debe estar entre 1900 y {year_actual}."
                )

            return year

        except ValueError as error:
            print(f"Error: {error}")


def main():
    """Solicita los datos y calcula los años transcurridos."""
    nombre = solicitar_nombre()
    year_nacimiento = solicitar_nacimiento()

    year_actual = date.today().year

    years = year_actual - year_nacimiento

    print(f"¡Hola {nombre}! - Naciste hace {years} años.")


if __name__ == "__main__":
    main()
