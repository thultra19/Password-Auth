print("validacion de correo")
correo = str(input("Ingrese su correo electrónico:\n"))
longitud = len(correo)

for longitud in correo:

    if correo.find("@") != -1 and correo.find(".") != -1:
        if correo.find("@") < correo.find("."):
            print(f"correo válido")
            break
        else:
            print(f"correo no válido")
            break
    else:
        print("correo no válido")

#if correo.find("@") >0 and correo.find(".") >0:
#        print("Correo electrónico válido")
#        break
#    else:        print("Correo electrónico no válido")
    