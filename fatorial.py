num = int(input('Digite um número: '))
contador = 1
fatorial = num
while contador < num :
    fatorial = fatorial * (num-contador)
    contador+=1
print(fatorial)
