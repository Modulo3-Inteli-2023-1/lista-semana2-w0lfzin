#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    freq_count1 = {}
    freq_count2 = {}
    
    for char in str1:
        freq_count1[char] = freq_count1.get(char, 0) + 1
    
    for char in str2:
        freq_count2[char] = freq_count2.get(char, 0) + 1
    
    return freq_count1 == freq_count2







# Teste a sua função aqui (caso ache necessário)











