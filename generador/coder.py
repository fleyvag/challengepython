shift = 1 # definiendo el recuento de turnos

text = "s"

cifrado = ""

for c in text:

    # comprobar si el carácter es una letra mayúscula
    # if c.isupper ():

        # encuentra la posición en 0-25
        c_unicode = ord (c)

        c_index = ord (c) - ord ("A")

        # realizar el turno
        new_index = (c_index + shift)% 26

        # convertir a un nuevo personaje
        new_unicode = new_index + ord ("A")

        nuevo_carácter = chr (new_unicode)

        # añadir a una cadena cifrada
        cifrado = cifrado + nuevo_carácter

    # else:

    #     # dado que el carácter no está en mayúsculas, déjelo como está
    #     cifrado += c
        
print ("Texto sin formato:", text)

print ("Texto cifrado:", cifrado)