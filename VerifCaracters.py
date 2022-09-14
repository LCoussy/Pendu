def verifAlphabet(x):
    x = x.replace("é","e")
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
    x = x.lower()
    for caractere in x:
        if caractere.isalpha() == True:
            continue
        else :
            return False
    return x