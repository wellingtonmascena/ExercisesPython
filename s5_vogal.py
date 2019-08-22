#Data: 04/06/2018
#Autor: Wellington Mascena
#Descrição Semana05 - ex3: Retorna se é vogal

def vogal(v):
    '''
    Entrada deve ser um caracter entre aspas.
    Saída será True para vogal e False para qualquer outro caracter não vogal.
    '''
    ehVogal = False
    
    #Testando se é vogal.
    if(v == "A" or v == "a" ):
        ehVogal = True
        
    if(v == "E" or v == "e" ):
        ehVogal = True
        
    if(v == "I" or v == "i" ):
        ehVogal = True
        
    if(v == "O" or v == "o" ):
        ehVogal = True
        
    if(v == "U" or v == "u" ):
        ehVogal = True

    return ehVogal
