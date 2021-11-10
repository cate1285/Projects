usuarioEnBD="Cate"
claveEnBD="How deep is your"
saldo=500000


def validaUsuario(u,p):
  if u == usuarioEnBD and p==claveEnBD:
    return True
  return False
 
def login():
  usuario=input("Ingrese el usuario")
  clave=input("ingrese la clave")
  return validaUsuario(usuario,clave)

def retirar(valor):
  if valor > saldo:
    print("Saldo insuficiente, el saldo es de ", saldo)
    return opciones()

  print ("Transaccion realizada, nuevo saldo", saldo - valor)
  return opciones()

def depositar(valor):
    print("Transaccion realizada, nuevo saldo",saldo + valor)
    return opciones()

def accion (opcion):
    if opcion ==1:
        valor=int(input("Ingresa el valor a depositar "))
        return depositar(valor)
    if opcion ==2:
        valor=int(input("ingresa el valor a retirar"))
        return retirar(valor)
    return False,saldo

def ejecutar():
  if not login():
    print("Usuario o contraseña invalidos")
  return opciones()

def opciones():
    opcion=int(input("  que desea hacer ? ingrese la opcion 1 o 2 o 3 para salir"))
    if opcion == 3:
        return despedida()

    return accion(opcion)
    
def despedida():
    print("Gracias por usar cajero x")  


ejecutar()