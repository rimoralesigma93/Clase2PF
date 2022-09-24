import math

class calculadora:
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

    def sumar(self):
        suma = self.num1 + self.num2
        print("el resultado de la suma es: ", suma)

    def restar(self):
        resta = self.num1 - self.num2
        print("el resultado de la resta es: ", resta)

    def multiplicar(self):
        multiplicacion = self.num1 * self.num2
        print("el resultado de la multiplicación es: ", multiplicacion)

    def dividir(self):
        division = self.num1 / self.num2
        print("el resultado de la division es: ", division)
    
    def raiz(self):
        raiz = math.sqrt(self.num1)
        print("Raiz cuadrada es: ", raiz)
    def potencia(self):
        potencia = pow(self.num1, self.num2)
        print("Potencia: ", potencia)
        
class cavanzada(calculadora):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def raiz(self):
        raiz = math.sqrt(self.num1)
        print("Raiz de del numero ", self.num1,"es: ", raiz)
    def potencia(self):
        potencia = pow(self.num1, self.num2)
        print("Resultado del numero potenciado es: ", potencia)
        

print("""
 Dime, ¿qué quieres hacer?
    
1) Sumar los dos números
2) Restar los dos números
3) Multiplicar los dos números
4) Dividir los dos numeros
5) Raiz cuadrada
6) Potencia
""")
opcion = int(input("Elige una opción: ") )  
num1 = input("ingrese un numero/ingrese solo un numero para la raiz cuadrada/ingrese el numero a potenciar: ")
if opcion != 5:
    num2 = input("ingrese el otro numero/ingrese la potencia: ")
    
calculadora = calculadora(num1, num2) 
cavanzada = cavanzada(num1, num2)  

if opcion == 1:
    calculadora.sumar()
if opcion == 2:
    calculadora.restar()
if opcion == 3:
    calculadora.multiplicar()
if opcion == 4:
    calculadora.dividir()
if opcion == 5:
    cavanzada.raiz()
if opcion == 6:
    cavanzada.potencia()
