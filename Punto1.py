def operaciones (num1,num2,operacion):
    match operacion:
        case"+":
            Resultado=num1+num2
        case"-":
            Resultado=num1-num2
        case"*":
            Resultado=num1*num2
        case"/":
            Resultado=num1/num2
    print(Resultado)
entrada=input("Ingresa los numeros y la operacion ").split(",")
x=float(entrada[0])
y=float(entrada[1])
z=entrada[2]
operaciones(x,y,z)
