#entrada: lendo a palavra
p = input()

#calculando o tamanho
size = len(p)

alfabeto = "abcdefghijklmnopqrstuvxz"
vogais = "aeiou"

saida = ''

# realizando o processamento
for x in range(size):
    #se for vogal é ela mesma e vai para a próxima letra
    if(vogais.find(p[x]) >= 0):
        saida = saida + p[x]
        continue
        
    # é consoante então tem que incluir ele
    saida = saida + p[x]
    
    #localiza a consoante no alfabeto
    index = alfabeto.find(p[x])
    
    #localiza a vogal mais próxima
    i=index
    j=index
    
    volta = False
    while(i > 0):
        i -= 1
        #se for consoante busca o anterior
        if(vogais.find(alfabeto[i]) >= 0):
            volta = True
            break;
            
    frente = False
    while(j < len(alfabeto)-1):
        j += 1
        #se for consoante busca a próxima letra
        if(vogais.find(alfabeto[j]) >= 0):
            frente = True
            break;
           
    #verifica se encontrou alguma vogal tanto na volta como na frente
    if(volta and frente):
        #verifica qual é a menor distância
        if(index -i <= j - index):
            #menor é a volta
            saida = saida + alfabeto[i]
        else:
            #menor a a frente
            saida = saida + alfabeto[j]
            
    #só encontrou vogal na volta
    elif(volta):
        saida = saida + alfabeto[i]
        
    #só encontrou vogal na frente
    elif(frente):
        saida = saida + alfabeto[j]

    #localiza a consoante mais próxima
    k=index
    while(k < len(alfabeto)-1):
        k += 1
        #se for consoante busca a próxima letra
        if(vogais.find(alfabeto[k]) < 0):
           break;

        # inclui a próxima consoante    
    saida = saida + alfabeto[k]
           
# saída: imprimindo o resultado
print(saida)

