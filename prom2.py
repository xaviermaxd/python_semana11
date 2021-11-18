correos = {}
while True:
    email = input("ingrese un correo: ")
    contraseña = input("ingrese una contraseña: ")
    print(" ")
    if correos.get(email) is None:
        correos[email] = contraseña
    else:
        print("el correo ya existe")

    nuevo = input("desea ingresar un nuevo correo? (si/no) : ")
    print(" ")
    if nuevo == "no":
        print("correo registrado: ",correos)
        break