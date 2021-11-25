turnos=1
texto="frank"
unicode=[]
arreglo=[]
cifrado=[]
desunicode=[]

for caracter in texto:
    arreglo.append(caracter)
for letra in arreglo:
    unicode.append(ord(letra))
for  cifra in unicode:
    cifrado.append(cifra+turnos)
for desuni in cifrado:
    desunicode.append(chr(desuni))
# for i in range(0,len(desunicode)):
print(desunicode)
print(''.join(desunicode))