# proyecto calculadora
def operaciones (num1,num2,operacion,):
    if operacion == "suma":
        resultado = num1 + num2
        print ("el resultado de la suma es: ", resultado)
    elif operacion == "resta":
        resultado = num1 - num2
        print ("el resultado de la resta es: ", resultado)
    elif operacion == "multiplicacion":
        resultado = num1 * num2
        print ("el resultado de la multiplicacion es: ", resultado)
    elif operacion == "division":    
        resultado = num1 / num2
        print ("el resultado de la division es: ", resultado) 
    return resultado



print ("esto es una calculadora")
num1 = input("ingrese el primer numero: ")
num1 = int(num1)
num2 = input("ingrese el segundo numero: ")
num2 = int(num2)

operacion = input("ingrese la operacion que desea realizar (suma,resta,multiplicacion o division):")

resultado = operaciones(num1,num2,operacion)

print (resultado)




repeticion = input("desea realizar otra operacion? (si o no): ")

if repeticion == "si":
    mismo_numero = input("desea utilizar el mismo numero? (si o no): ")
    if mismo_numero == "si":
        num1 = resultado
        num2 = input("ingrese el segundo numero: ")
        num2 = int(num2)
        operacion = input("ingrese la operacion que desea realizar (suma,resta,multiplicacion o division):")
        print (operaciones(num1,num2,operacion))
    else:
        num1 = input("ingrese el primer numero: ")
        num1 = int(num1)
        num2 = input("ingrese el segundo numero: ")
        num2 = int(num2)
        operacion = input("ingrese la operacion que desea realizar (suma,resta,multiplicacion o division):")
        print (operaciones(num1,num2,operacion))
        
else:
    print ("gracias por utilizar la calculadora")
