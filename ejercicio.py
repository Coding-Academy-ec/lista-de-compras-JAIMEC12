def convertir_lista_a_tupla(lista):
    return tuple(lista) # Utiliza una función para convertir 


def main():
    compras = input("Ingrese una lista de compras: ")
    productos = compras.split(", ")
    print(f"Los productos en la lista de compras son: {productos}")
    productos=convertir_lista_a_tupla(productos)
    print(f"Los productos en la lista de compras son: {productos}")

if __name__ == "__main__":
    main()