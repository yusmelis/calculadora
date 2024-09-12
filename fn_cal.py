def menu_principal() -> str:
    """muestra un menu de opciones a elegir

    Returns:
        str: devuelve la opcion elegida
    """
    limpiar_pantalla()
    print(f"{'Calculadora':^50s}")
    print("1- Ingrese primer operando")
    print("2- Ingrese segundo operando")
    print("3- Elegir Operacion")
    print("4- Mostrar resultado")
    print("5- Salir")
    return input("ingrese una opcion desde 1 a 5: ")


def menu_calculos(A: int, B: int) -> str:
    """ menu de opciones de operaciones matematicas

    Returns:
        str: devuelve la opcion elegida
    """
    limpiar_pantalla()
    print(f"{'Operaciones Matematicas':^50s}")
    print(f"a- Calcular la suma {A} + {B}")
    print(f"b- Calcular la resta {A} - {B}")
    print(f"c- Calcular la Division {A} / {B}")
    print(f"d- Calcular la Multiplicacion {A} * {B}")
    print(f"e- Calcular {A} ! ")
    print("f- Salir")
    return input("ingrese una opcion desde a...f: ")


def pedir_confirmacion(mensaje: str) -> bool:
    """consulta al usuario si desea finalizar el programa

    Args:
        mensaje (str): muestra lo que desea solicitar al usuario

    Returns:
        bool: retorna True si confirma salida o False de lo contrario
    """
    respuesta = input(mensaje).lower()
    return respuesta == 's'


def pausar():
    """consulta si deseas continuar
    """
    import os
    os.system("pause")


def limpiar_pantalla():
    """elimina lo mostrado en consola anteriormente
    """
    import os
    os.system("cls")


def ingresar_numero(mensaje: str) -> int:
    """solicita un numero y si puede ser convertilo a entero lo devuelve

    Returns:
        int:  numero entero validado

    """

    while True:
        numero = input(mensaje)
        if not numero.isdigit():
            print("numero invalido")
        else:
            return int(numero)


def suma(numero_1: int, numero_2: int) -> int:
    """suma dos numero enteros

    Args:
        numero_1 (int):primer numero
        numero_2 (int):segundo numero

    Returns:
        int: resultado de suma de dos numeros
    """
    return numero_1 + numero_2


def resta(numero_1: int, numero_2: int) -> int:
    """resta dos numero

    Args:
        numero_1 (int):primer numero
        numero_2 (int):segundo numero

    Returns:
        int: resultado de resta de dos numeros
    """
    return numero_1 - numero_2


def dividir(numero_1: int, numero_2: int) -> float:
    """Divide dos numero

    Args:
        numero_1 (int):primer numero
        numero_2 (int):segundo numero

    Returns:
        float: resultado de divide de dos numeros
    """
    if not numero_2 == 0:
        return numero_1 / numero_2
    raise ZeroDivisionError("No se puede dividir por cero")


def multiplicar(numero_1: int, numero_2: int) -> int:
    """realiza el producto de dos numeros

    Args:
        numero_1 (int): primer numero
        numero_2 (int): segundo numero

    Returns:
        int: el resultado de multiplicar dos numeros
    """
    return numero_1 * numero_2


def factorial(numero: int) -> int:
    """_multiplica todos los numeros menores al recibidos

    Args:
        numero (int): numero a factoriar_

    Returns:
        int: factorial encontrado

    """
    if numero >= 0:
        if numero == 0:
            factorial = 1
        else:
            factorial = numero
            while numero > 1:
                numero -= 1
                factorial *= numero
        return factorial
    raise ValueError("el factorial es solo  para numeros naturales")


# ---------------------------------------------------
