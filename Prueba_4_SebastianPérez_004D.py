
datos = {
    "comprador":[
        
    ]
}
def validar_numero (mensaje_input:str):
    while True:
        try:
            numero = int(input(mensaje_input))
            if numero <= 0:
                print("El numero debe ser mayor a 0")
            continue
        except ValueError:
            print("Debe ser un numero entero")
        return numero
    
def comprar_entradas ():
    if len(datos["comprador"]) == 0:
        print("No hay registros del comprador.")
        return
    print("Lista de compradores")
    for comprador in datos["comprador"]:
        print(f"Nombre de comprador: -{comprador["nombre_comprador"]}] \n[Tipo de entrada (G/V){comprador["categoria"]}], [Código de acceso:] - [{comprador["codigo"]}]")

while True:
    print("---MENU PRINCIPAL---")
    print("1.- Comprar entrada")
    print("2.- Consultar comprador.")
    print("3.- Cancelar compra.")
    print("4.- Salir.")

    opc = int(input("Ingrese la opcion: "))

    if opc  == 1:
        while True:
            nombre_comprador = input("Ingrese el nombre del comprador: ")
            if len(nombre_comprador) == 0:
                print ("El nombre no puede estar vacio")
                continue
            nombre_repetido = 0
            for comprador in datos ["comprador"]:
                if comprador("nombre".lower()) == nombre_comprador.lower():
                    nombre_repetido = 1
                    break
                elif nombre_repetido == 0:
                    break  
                

            while True:
                categoria = input("Ingrese el tipo de entrada(G/V): ")
                if categoria in ["comprador"]:
                    continue
                while True:
                    codigo = validar_numero("Ingrese el codigo:")
                   
                    datos["comprador"].append[{
                                                "nombre":nombre_comprador,
                                                "categoria":categoria,
                                                "codigo":codigo 

                    }]
                    print("Código validado. ¡Entrada registrada con éxito!")
                        
    elif opc == 2:
        print("Consultar comprador")   
        busqueda = input("Ingrese nombre del comprador")
        encontrado = 0
        for i in datos["comprador"]:
            if (busqueda.lower() == (i("nombre_comprador".lower()))):
                print("Informacion comprador.")
                print(f"Nombre del comprador: {i("nombre_comprador")}")
                print(f"Tipo de entrada: {i("categoria")}")
                print(f"codigo{i("codigo")}")
    elif opc == 3:
        print("Cancelar Compra.")
        nombre_comprador = validar_numero("Ingrese nombre de comprador a cancelar:")
        eliminado = 0
        indice = 0
        while True:
            if datos ["comprador"][indice] == nombre_comprador:
                entrada_eliminada = datos ["comprador"].pop (indice)
                print(f"¡Compra cancelada!")
                eliminado = 1
                break
            elif eliminado == 0:
                print("Nombre no valido.")
    elif opc == 4:
        print("Programa terminado...")
        break
    else:
       print("Operacion no valida.")






