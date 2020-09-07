
#boleto.py trata de contabilizar los boletos y las cantidad de personas
#ademas de tener la opcion de poder pagar medio boleto o entero

#inicializamos las variables
c=0
l1=[]
pb=0
p=0
tr=0
x=input("ingrese C para comenzar, F para finalizar")
#Cargamos el comienzo y si el pasajero paga medio boleto o entero
while x=="C":
    t=input("ingrese MB para medio boleto, para boleto completo presione B")
    c=c+1
    if t=="MB":
        pb=92.50/2
        print("El pasajero debe pagar",pb,)
    else:
        t=="B"
        pb=92.50
        print("el pasajero debe pagar",pb,)
    l1.append(pb)
    x=input("ingrese C para continuar, F para finalizar")

#Mostramos el total recaudado y la cantidad de pasajeros
print("el total recaudado fue de ",sum(l1),)
print("la cantidad de pasajeros que subieron fueron ",c,)

