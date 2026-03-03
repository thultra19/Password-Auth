print("Autenticación de contraseñas")


def validar_contrasena(contrasena: str):
    especiales = "!@#$%^&*()_+-=[]|;':,./<>?"

    errores = ""
    # flags and positions (0 means not found)
    has_upper = False
    has_digit = False
    has_special = False
    pos_upper = 0
    pos_digit = 0
    pos_special = 0

    # length check
    if len(contrasena) < 8:
        errores += "Debe tener al menos 8 caracteres\n"

    # scan left-to-right and stop when all required types are found
    for idx, c in enumerate(contrasena, start=1):
        if (not has_upper) and c.isupper():
            has_upper = True
            pos_upper = idx
        if (not has_digit) and c.isdigit():
            has_digit = True
            pos_digit = idx
        if (not has_special) and c in especiales:
            has_special = True
            pos_special = idx

        if has_upper and has_digit and has_special:
            break

    if not has_upper:
        errores += "Debe contener al menos una letra mayúscula\n"
    if not has_digit:
        errores += "Debe contener al menos un número\n"
    if not has_special:
        errores += "Debe contener al menos un carácter especial (por ejemplo !@#$%...)\n"

    valida = (errores == "")
    # return: valid flag, error string, and positions (0 if not found)
    return valida, errores.rstrip(), pos_upper, pos_digit, pos_special


print("La contraseña debe tener: mínimo 8 caracteres, 1 mayúscula, 1 número y 1 carácter especial.")
contrasena = input("Ingrese su contraseña:\n")

valida, errores, pos_upper, pos_digit, pos_special = validar_contrasena(contrasena)
if valida:
    print("Contraseña aceptada")
else:
    print("Contraseña no aceptada. Errores:")
    if errores:
        print(errores)

# report first-found positions (if any)
if pos_upper:
    print(f"Letra mayúscula encontrada en la posición {pos_upper}")
if pos_digit:
    print(f"Número encontrado en la posición {pos_digit}")
if pos_special:
    print(f"Carácter especial encontrado en la posición {pos_special}")
