monto= int(input("ingrese el monto de su compra: "))
if monto > 100:
    descuento= monto*0.10
    montofinal= monto-descuento
    print("felicidades se le aplicara un 10% de descuento a su compra")
    print("el total a pagar: $ ",montofinal)
else:
    print("el monto no alcanza el minimo para recibir el descuento")
    print("el monto a pagar es: $",monto)