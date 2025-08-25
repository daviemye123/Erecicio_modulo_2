def contra ():
    """
    usando una variable con nombre user para que el usaurio ingrese la contraseña
    if user < str(user) para poder leer lo que se guardo en la variable
    validando con elif,any para saber si no existen ningun digito
    .isupper para saber si tiene mayuscula
    .islower para saber si tiene numero
    return:user si no es valida
    """
    while True:
       user=input("Ingresar contraseña ")
       if user < str(user):
           print("no es valida la contraseña")
       elif not any(c.isupper() for c in user):
           print("debe tener almenos una mayuscula")
       elif not any(c.islower() for c in user):
           print("debe tener almenos un numero")
       else:
           print("exito saliendo by")
           break
if __name__ == '__main__':
    contra()