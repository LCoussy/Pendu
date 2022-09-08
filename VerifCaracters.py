specialCaractere = ["é","è","ç","à","ù","µ"]

def verifAlphabet(secretWord):
    for caractere in secretWord:
        if caractere.isalpha() == True and caractere not in specialCaractere:
            continue
        else :
            print("Un/Des caractères ne sont pas valides.")
            return False
    return True