from VerifCaracters import verifAlphabet
from Display import printPendu

def gameLoop():

    End = False
    verif = False
    lifeNum = 7
    letterNum = 0
    coupNum = 0
    retry = ""
    usesLetters = []

    while verif == False:

        secretWord = input("Proposer un mot secret:")
        verif = verifAlphabet(secretWord)
        if verif == False:
            print("Un/Des caractères ne sont pas valides.")

    #Le jeu commence !

    listSecretWord = list(secretWord)
    underSecretWord = []

    for i in range(len(secretWord)):
        underSecretWord.append("_")

    print("Le mot à trouver est le suivant\n{0}\nVous avez {1} vies".format(' '.join(underSecretWord),lifeNum))

    while End == False:
        if not(usesLetters) == False:
            print("Vous avez déjà utilisez ces lettres :\n{0}".format(', '.join(usesLetters)))

        letter = input("Proposer une lettre ou un mot:")
        
        if len(letter) == 1 and verifAlphabet(letter) == True:
            usesLetters.append(letter)
        coupNum += 1
        if letter in listSecretWord:
            for a in range(len(secretWord)):
                if secretWord[a] == letter:
                    letterNum +=1
                    underSecretWord[a] = letter

            print("la lettre est dans le mot, il y en a {0}\n{1}".format(letterNum, ' '.join(underSecretWord)))

        elif letter not in listSecretWord and verifAlphabet(letter) == True:
            if len(letter) != len(secretWord) and len(letter) != 1:
                print("Vous avez entré trop/pas assez de lettres")
            elif letter == secretWord:
                underSecretWord = listSecretWord
            elif len(letter) == len(secretWord) and letter != secretWord:
                lifeNum -= 1
                print("Ceci n'est pas le mot secret!\n{0}\nVous avez désormais {1} vies\n{2}".format(' '.join(underSecretWord),lifeNum,printPendu(lifeNum)))
            else:
                lifeNum -= 1

                print("La lettre n'est pas dans le mot.\n{0}\nVous avez {1} vies\n{2}".format(' '.join(underSecretWord),lifeNum,printPendu(lifeNum)))

        elif verifAlphabet(letter) == False:
            lifeNum -= 1

            print("Ceci n'est pas un caractère valide!\n{0}\nVous avez désormais {1} vies\n{2}".format(' '.join(underSecretWord),lifeNum,printPendu(lifeNum)))

        letterNum = 0

        if underSecretWord == listSecretWord:
            print("vous avez gagné en {0} coup !".format(coupNum))
            End = True

        elif lifeNum == 0:
            print("\nVous avez perdu\nLe mot était {0}".format(secretWord))
            End = True
        
    while retry != "non" or retry != "oui":
        retry = input("Voulez-vous recommencer ?")
        if retry != "non" and retry != "oui":
            print("Ce n'est pas une réponse valable, veuillez me répondre par oui ou non.")
        elif retry == "oui":
            print("D'accord, je vous lance une nouvelle partie !")
            return True
        elif retry == "non":
            print("D'accord, j'espère que ça vous a plu ! Bonne journée")
            return False

firstParti = gameLoop()

while firstParti == True:
    otherParti = gameLoop()
    if otherParti == False:
        firstParti = False