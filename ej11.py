def Ejercicio11():
    n1 = int(input("¿Cuántos autos vendió este mes?."))
    n2 = int(input("¿Cuál es el total del valor de todos los autos que vendió? Ingrese la cifra."))

    comision = 200 * n1
    adicional = n2 * 0.005

    salarioTotal = 5500 + comision + adicional

    print("Tu salario es de: " )
Ejercicio11()