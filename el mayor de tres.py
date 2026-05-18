
#El mayor de 3 numeros

num1 = int(input("ingrese el primer numero \n"))
num2 = int(input("ingrese el segundo numero \n"))
num3 = int(input("ingrese el tercer numero \n"))

if (num1>= num2 and num1 >= num3):
    mayor = num1
elif ( num2 >= num1 and num2 >= num3):
    mayor = num2
else: 
    mayor = num3

print ("El numero mayor es:", mayor)