compras = []
montocompra = float(input("ingrese compra, 0 para salir: "))
compras.append(montocompra)
totalcompras = 0
n = 0
while montocompra != 0:
        n += 1
        montocompra = float(input("ingrese compra, 0 para salir: "))
        if montocompra < 0:
            print("numero no valido. ingrese cantidad nueva")
            n -= 1
            continue;
        if montocompra == 0:
            break;
        compras.append(montocompra)
        
print("num articulos: ", n)
print("lista articulos: ", compras)

if sum(compras) > 1000:
    print("Subtotal: ", sum(compras), "\Descuento: ", sum(compras) * .1, "total a pagar: ",sum(compras) *.9)
else:
    print("Total a pagar", sum(compras))