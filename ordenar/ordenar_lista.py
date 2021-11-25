def ordenar(data):
    lista=data.split(",")
    lista_ordenada=sorted(lista)
    return print(lista_ordenada)
    # return print(lista.sort())
datos=input("ingrese los datos separados por una coma ")


ordenar(datos)