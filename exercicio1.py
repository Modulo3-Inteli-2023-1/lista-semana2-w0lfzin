#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def conta_palavras_unicas(frase):
    palavras = frase.lower().split()
    
    palavras_unicas = set(palavras)
    
    return len(palavras_unicas)

frase = "Essa frase é um teste, essa frase possui palavras repetidas"
quantidade = conta_palavras_unicas(frase)
print("Quantidade de palavras únicas:", quantidade)






# Teste a sua função aqui (caso ache necessário)











