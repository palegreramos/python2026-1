
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


def solicitar_anio_nacimiento():
    """Solicita un año de nacimiento válido.

    Returns:
        int: Año de nacimiento introducido.
    """
    while True:
        try:
            anio = int(input("Introduce tu año de nacimiento: "))

            anio_actual = date.today().year

            if not 1900 <= anio <= anio_actual:
                raise ValueError(
                    f"El año debe estar entre 1900 y {anio_actual}."
                )

            return anio

        except ValueError as error:
            print(f"Error: {error}")


def main():
    """Solicita los datos y calcula los años transcurridos."""
    nombre = solicitar_nombre()
    anio_nacimiento = solicitar_anio_nacimiento()

    anio_actual = date.today().year

    anios = anio_actual - anio_nacimiento

    print(f"¡Hola {nombre}! - Naciste hace {anios} años.")


if __name__ == "__main__":
    main()
