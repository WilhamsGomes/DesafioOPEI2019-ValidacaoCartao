n = str(input("Informe o número do cartão: "))
arrayCartao = list(map(int, n)) #CONVERTENDO O VALOR RECEBIDO EM LISTA INT

for x in range(len(arrayCartao)):

    if (x % 2 == 1):
        
        verificador = arrayCartao[x]

        if(verificador > 9):
            aux = str(arrayCartao[x])
            numero1 = int(aux[0])
            numero2 = int(aux[1])
            arrayCartao[x] = (numero1 + numero2)
        
    if (x % 2 == 0):
        arrayCartao[x] = arrayCartao[x] * 2
        verificador = arrayCartao[x]
        
        if(verificador > 9):
            aux = str(arrayCartao[x])
            numero1 = int(aux[0])
            numero2 = int(aux[1])
            arrayCartao[x] = (numero1 + numero2)
        
    
somaCartao = sum(arrayCartao)
s = str
if (somaCartao % 10 == 0):
    s = "SIM"
    print (s)
else:
    s = "NAO"
    print(s)



