compras = []
montocompra = int(input("ingrese minutos, 0 para salir: "))
compras.append(montocompra)
totalcompras = 0
n = 0
while montocompra != 0:
        n += 1
        montocompra = float(input("ingrese minutos, 0 para salir: "))
        if montocompra < 0:
            print("numero no valido. ingrese cantidad nueva")
            n -= 1
            continue;
        if montocompra == 0:
            break;
        compras.append(montocompra)
        

hora = 0
pagototal = 0

minutostotales=sum(compras)

horas = minutostotales/60
print("horas: ", horas)
pagototal = horas * 15


if minutostotales > 480:
    print("Tarifa", pagototal+200+25)
else:
    print("Tarifa: ", pagototal+25)
