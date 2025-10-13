# calculadora de temperatura

print ("calculadora de conversion de temperatura")
print ("elija a que quiere convertir su operacion")
print (" 1. Convertir de Fahrenheit a Celsius ")
print (" 2. Convertir de celsius a fahrenheit ")

opcion = int(input("elija una opcion (1 o 2)\n"))
if opcion == 1:
    f = float(input("ingrese la temperatura en fahrenheit \n"))
    c = (f - 32) * 5/9
    print ("la temperatura en celsius es:" , c)
if opcion == 2:
    c = float(input("ingrese la temperatura en celsius \n"))
    f = (c * 9/5) + 32
    print (" la temperatura en celsius es:" , f)
 
