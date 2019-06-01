# Lógica de Sistemas
# Primer Semestre
# Humberto José Orellana Colindres
# 0907 - 19 -10906




num=int(input("Ingrese el primer numero "))
num1=int(input("Ingrese el segundo numero "))
num2=int(input("Ingrese el tercer numero "))

opc=int(input("Ingrese un número para elegir una opcion: 1 o 2 "))

if(opc==1):

    if(num1==0):
        if(num<num2):
            ressul= num2-num
            print("Se ha restado al tercer numero, el primero")
            print(ressul)
        else:
            ressul= num-num2
            print("Se ha restado al primer numero el tercero")
            print(ressul)
    elif(num<num2):
        ressul=num*num1*num2
        print("La operación que se esta realizando es una multiplicación")
        print (ressul)
    elif(num==num2):
        ressul=num+num1+num2
        print("La operación que se esta realizando es una suma")
        print(ressul)
# En esta parte, el codigo lo que hace es concatenar los números ya dados.
elif(opc==2):
    print("Número concatenados")
    print(num + num1 + num2)
    #Justamente aquí se me olvidó que llevaba el examen, y recuerdo que así iba, pero no estoy seguro.
    # Admito que me dormí nomás vine, ya estaba cansado.
    # Que tenga buen finde. Inge.
    for i in range(num2):
        # Imprime la multiplicación de los primeros dos números la cantidad de veces que haya sido indicada con el tercer número
        print(num*num1, end="")
    print()
    print("Fin")
