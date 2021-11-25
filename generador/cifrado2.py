class crypt:
    def __init__(self,message,posicion):
        self.message= list(message)
        self.posicion=posicion
    
    def encrypt(self):
    # join pasa a string los datos internos
        return ''.join(list(map(lambda x: chr(ord(x)+self.posicion),self.message))) 
    # ''.join(self.message)
        



messageCrypt=crypt("hola",1)


print(messageCrypt.encrypt()) 
