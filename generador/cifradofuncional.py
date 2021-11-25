
def encrypt(message,posicion):
    # join pasa a string los datos internos
        return ''.join(list(map(lambda x: chr(ord(x)+posicion),message))) 
    # ''.join(self.message)
print(encrypt("abc",1))     