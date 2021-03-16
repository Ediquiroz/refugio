def iva(n):
    iva=n
    costo = int(input("Cual es el monto que desea calcular?: "))
    calculo = costo * iva / 100
    print("El iva calculado es igual a: " + str(calculo) + "\n")
    return

print(iva(16))