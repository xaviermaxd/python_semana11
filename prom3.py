empresas = {
    '101010' : 'gloria',
    '121212' : 'repsol',
    '111111' : 'cocacola',
}

while True:
    print("\n",
        "1) Registrar clientes \n",
        "2) Mostrar clientes \n",
        "3) Buscar clientes \n",
        "4) Actualizar clientes \n",
        "5) Eliminar clientes \n",
        "6) Salir \n",
        )
    
    opcion = int(input("escoger una opcion: "))

    if opcion == 1:
        print("registrar nueva empresa")
        ruc = input("ingrese el ruc: ")
        nombre = input("ingrese el nombre: ")
        empresas[ruc] = nombre

    elif opcion == 2:
        print("mostrar clientes")
        print(empresas)

    elif opcion == 3:
        print("Buscar clientes")
        ruc = input("ingrese el ruc que desea buscar: ")
        print(empresas.get(ruc,"sin resultados"))

    elif opcion == 4:
        print("actualizar datos")
        ruc = input("ingrese el ruc de la empresa que desea actualizar: ")
        nuevo_nombre = input("ingrese el nuevo nombre de la empresa: ")
        empresas[ruc] = nuevo_nombre

    elif opcion == 5:
        print("eliminar empresa registrada")
        ruc = input("ingrese el ruc de la empresa que desea eliminar: ")
        del empresas[ruc]

    elif opcion == 6:
        break





