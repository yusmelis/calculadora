from fn_cal import *

seguir = "s"
flag_operando_1 = False
flag_operando_2 = False
flag_calculos = False
while seguir == "s":

    match menu_principal():

        case "1":
            A = ingresar_numero("Ingresar primer numero Entero: ")
            print(f" A = {A}")
            flag_operando_1 = True
        case "2":
            if flag_operando_1 == False:
                print(" ingrese el primer operando antes del segundo")
            else:
                B = ingresar_numero("Ingresar segundo numero entero: ")
                print(f" B = {B}")
                flag_operando_2 = True
        case "3":
            if flag_operando_2 == False:
                print(" ingrese los operandos antes de realizar los calculos")
            else:
                terminar_caculos = "n"
                resultado_suma = None
                resultado_division = None
                resultado_resta = None
                resultado_multiplicacion = None
                resultado_factorial_a = None
                resultado_factorial_b = None
                while terminar_caculos == "n":
                    match menu_calculos(A, B):

                        case "a":
                            resultado_suma = suma(A, B)

                        case "b":
                            resultado_resta = resta(A, B)

                        case "c":
                            try:
                                resultado_division = dividir(A, B)
                            except ZeroDivisionError as e:
                                print(e)
                                exit()

                        case"d":
                            resultado_multiplicacion = multiplicar(A, B)

                        case "e":
                            try:
                                resultado_factorial_a = factorial(A)
                            except ValueError as e:
                                print(e)
                                exit()

                        case "f":
                            if pedir_confirmacion("confirma salida s/n : "):
                                terminar_caculos = "s"

                flag_calculos = True
        case "4":
            if flag_calculos == False:
                print("primero debes de realizar los calculos")

            else:
                if not resultado_suma == None:
                    print(f"el resultado {A} +{B} = {resultado_suma}")

                if not resultado_resta == None:
                    print(f"el resultado {A} -{B} = {resultado_resta}")

                if not resultado_division == None:
                    print(f"el resultado {A} /{B} = {resultado_division:.2f}")

                if not resultado_multiplicacion == None:
                    print(f"el resultado {
                          A} *{B} = {resultado_multiplicacion}")

                if not resultado_factorial_a == None:
                    print(f"el resultado de {A}!= {resultado_factorial_a} ")

        case "5":
            if pedir_confirmacion("confirma salida s/n : "):
                seguir = "n"

    pausar()

print("Fin del programa")
