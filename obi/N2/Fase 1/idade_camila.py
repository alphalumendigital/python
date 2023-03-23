# ler três linhas, três números

n1 = int(input())
n2 = int(input())
n3 = int(input())

if(n1 >= 5 and n1 <= 100 and n2 >= 5 and n2 <= 100 and n3 >= 5 and n3 <= 100):
    lista = [ n1, n2, n3 ]

    lista.sort()

    print(lista[1])
