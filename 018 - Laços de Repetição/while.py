# Usamos o while, porque ele roda um bloco de código enquanto a condição for verdadeira.

numero = 0

while numero < 5:
    print(numero)
    numero += 1

print() 

numeros = 22
while numeros < 30:
    numeros += 1
    if numeros == 30:
        print('Número atingiu o limite de 30!')
        break
    

print(numeros)


