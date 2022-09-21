def verifAlphabet(x):
    '''
    x : string
    verifie les caractères pour être conforme (juste lettres minuscules)
    '''
    for caractere in x:
        if caractere.isalpha() == True: #verifie si le caractère examiné est conforme
            continue
        else :
            return False
    return True

def replaceCaractere(x):
    '''
    x : string
    remplace tous les caractères spéciaux par leur homologue normal en lettre minuscule.
    '''
    x = x.lower() # passage en lettre minuscule
    x = x.replace("é","e") #remplacement des caractères spéciaux
    x = x.replace("è","e")
    x = x.replace("ë","e")
    x = x.replace("ê","e")
    x = x.replace("à","a")
    x = x.replace("ã","a")
    x = x.replace("â","a")
    x = x.replace("ä","a")
    x = x.replace("ç","c")
    x = x.replace("ù","u")
    x = x.replace("û","u")
    x = x.replace("ü","u")
    x = x.replace("ÿ","y")
    x = x.replace("ô","o")
    x = x.replace("ö","o")
    x = x.replace("î","i")
    x = x.replace("ï","i")
    x = x.replace("õ","o")
    x = x.replace("ì","i")
    x = x.replace("ñ","n")
    x = x.replace("µ","u")
    return x