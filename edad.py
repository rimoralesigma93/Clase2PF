edad = int(input("Que edad tienes?: "))
genero = str(input("Genero: "))

if edad >= 18: 
    print(f"Eres mayor de edad y tu genero es {genero}")
elif edad < 1:
    print("Edad Invalida")    
else:
    print(f"Eres menor de edad y tu genero es {genero}")