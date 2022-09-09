specialCaractere = ["é","è","ç","à","ù","µ"]

def verifAlphabet(secretWord):
    for caractere in secretWord:
        if caractere.isalpha() == True and caractere not in specialCaractere:
            continue
        else :
            return False
    return True