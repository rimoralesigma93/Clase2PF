conteo = 0
total = 0
monto = float(input("Ingrese el onto de la compra(0 para salir: "))
while monto != 0:
    while monto>0:
        total += monto
        conteo += 1
        monto = float(input("Ingrese el monto de la compra, 0 para salir: "))
        print("Cantidad de articulos: ", conteo)
        if total > 1000:
            print("Subtotal: ", total, "\Descuento: ", total * .1, "total a pagar: ", total *.9)
        else:
            print("Total a pagar", total)
            