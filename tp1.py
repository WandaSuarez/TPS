def EsEntero():
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            return num
        except ValueError:
            print("Error: Debe ingresar un número entero. Inténtalo de nuevo.")




def ejercicio_1():
    def tipo_de_triangulo(a,b,c):
        if a==b==c:
           return "equilatero"
        elif a==b or b==c or a==c:
            return"isoceles"
        else:
            return"escaleno"
        

    a=float(input("Ingrese el primer lado del triangulo: "))
    b=float(input("Ingrese el segundo lado del triangulo: "))
    c=float(input("Ingrese el tercer lado del triangulo: "))

    print("El triangulo es", tipo_de_triangulo(a,b,c))


def ejercicio_2():
    ancho=float(input("Ingrese el ancho en metros: "))
    alto=float(input("Ingrese el alto en metros: "))
    largo=float(input("Ingrese el largo en metros: "))

    area_de_pared= 2*(alto+ancho)*largo
    area_puerta= 0.8*2

    area_total=area_de_pared-area_puerta
    litros_de_pintura= area_total/10
    print("Se necesitan", litros_de_pintura, "litros de pintura para pintar la haabitacion.")


def ejercicio_3():
    print("No esta hecho, hay q preguntar")

def ejercicio_4():
    num1=int(input("Ingrese un numero: "))
    num2=int(input("Ingrese un numero: "))
    num3=int(input("Ingrese un numero: "))

    if num1 > num2 and num1 > num3:
        print("El numero mayor es: ",num1)
    elif num2 > num1 and num2 > num3:
        print("El numero mayor es: ",num2)
    elif num3 > num1 and num3 > num2:
        print("El numero mayor es: ",num3)
    else:
        print("Los numeros son iguales, ninguno es mayor a otro")


def ejercicio_5():
    cadena=input("Ingrese una oracion: ")
    espacio=cadena.count(" ")
    print("La oracion ingresa tiene ",espacio, "espacios.")

def ejercicio_6():
    num=int(input("Ingresa un numero positivo: "))
    for i in range(1,num+1):
     print(i)

def ejercicio_7():
    num=int(input("Ingresa un numero positivo: "))
    for i in range(2,12,2):
        print(i)

def ejercicio_8():
    num_a_ingresar=int(input("Cuantos valores quiere ingresar? "))
    uma=0
    for i in range(num_a_ingresar):
        valor=float(input("Ingrese un valor: "))
        suma=suma+valor
    promedio= suma/num_a_ingresar
    print("la suma de los numeros ingresados es:",suma)
    print("El promedio de los numeros ingresados es: ",promedio)


def ejercicio_9():
    def multiplos_entre_a_y_b(a, b, x):
     multiplos=[]
    for i in range(a, b+1):
        if i % x == 0:
            multiplos.append(i)
            print(i)
        return multiplos

    a = int(input("Ingrese el valor de A: "))
    b = int(input("Ingrese el valor de B: "))
    x = int(input("Ingrese el valor de X: "))
    
    multiplos= multiplos_entre_a_y_b(a,b,x)
    print("Los multiplos de", x ," que esten entre", a ,"y", b ," son: ",multiplos)


def ejercicio_10():
    ancho = int(input("Ingrese el ancho del rectangulo: "))
    largo = int(input("Ingrese el largo del rectangulo: "))

    if largo > 40:
        print("el largo no puede ser mayor a 40")
    else:
        for i in range(largo):
            for j in range(ancho):
                print("*", end="")
            print()


def ejercicio_11():
    suma=0
    cantidad=0

    while True:
     numero=int(input("ingrese un numero entero positivo (o un numero negativo para terminar): "))
     if numero < 0:
        break
    suma +=numero
    cantidad +=1
    if cantidad >0:
        promedio= suma/cantidad
        print("el promedio es", promedio,"con un total de",cantidad,"ingresos")
    else:
        print("no se ingresaron numeros positivos")


def ejercicio_12():
    def secuencia_ordenada():
        numeros = []
        num = int(input("Ingrese un numero entero positivo (0 para finalizar): "))
        while num != 0:
            numeros.append(num)
            num = int(input("Ingrese otro numero entero positivo (0 para finalizar): "))
        ordenada = True
        for i in range(len(numeros)-1):
            if numeros[i] > numeros[i+1]:
                ordenada = False
                break
        if ordenada:
            print("La secuencia está ordenada de menor a mayor.")
        else:
            print("La secuencia está ordenada de mayor a menor.")

    secuencia_ordenada()

def ejercicio_13():
    caracter=input("Ingres un caracter: ")
    num=int(input("Ingrese la cantidad de veces que se repita el caracter: "))
    while num <=0:
        num=int(input("Ingrese un numero natural valido: "))
    cadena= caracter*num
    print(cadena)


def ejercicio_14():
    texto=input("ingrese un texto y le diremos cuantas vocales tiene:")
    vocales="aeiouAEIOU"
    cantidad_de_vocales=0
    for letra in texto:
        if letra in vocales:
            cantidad_de_vocales+=1
    print("la cantidad de vocales es: ", cantidad_de_vocales)
    #En el for La variable letra toma el valor de cada carácter en el texto y 
    #luego se verifica si es una vocal utilizando la función in para verificar
    #si el carácter está en la cadena de vocales.

def ejercicio_15():
    print("No esta hecho, hay q preguntar")

def ejercicio_16():
    print("No esta hecho, hay q preguntar")

def menu():
    print("Menu de ejercicios")
    print("1. ejercicio 1")
    print("2. ejercicio 2")
    print("3. ejercicio 3")
    print("4. ejercicio 4")
    print("5. ejercicio 5")
    print("6. ejercicio 6")
    print("7. ejercicio 7")
    print("8. ejercicio 8")
    print("9. ejercicio 9")
    print("10. ejercicio 10")
    print("11. ejercicio 11") 
    print("10. ejercicio 12")
    print("10. ejercicio 13")
    print("10. ejercicio 14")
    print("10. ejercicio 15")
    print("10. ejercicio 16")
    print("0. Salir")

    while True:
        opcion = input("Ingresa una opción: ")
        if opcion.isnumeric() and 0 <= int(opcion) <= 16:
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")
    
    if opcion == "0":
        print("¡bayy!")
    else:
        opcion = int(opcion)
        if opcion == 1:
            ejercicio_1()
        elif opcion == 2:
            ejercicio_2()
        elif opcion == 3:
            ejercicio_3()
        elif opcion == 4:
            ejercicio_4()
        elif opcion == 5:
            ejercicio_5()
        elif opcion == 6:
            ejercicio_6()
        elif opcion == 7:
            ejercicio_7()
        elif opcion == 8:
            ejercicio_8()
        elif opcion == 9:
            ejercicio_9()
        elif opcion == 10:
            ejercicio_10()
        elif opcion == 11:
            ejercicio_11()
        elif opcion == 12:
            ejercicio_12()
        elif opcion == 13:
            ejercicio_13()
        elif opcion == 14:
            ejercicio_14()
        elif opcion == 15:
            ejercicio_15()
        elif opcion == 16:
            ejercicio_16()
        

menu()