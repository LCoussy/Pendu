from VerifCaracters import verifAlphabet
from affichage import printPendu
#from ErrorGestion import 

End = False
verif = False
lifeNum = 7
letterNum = 0
coupNum = 0

while verif == False:
    
    secretWord = input("Proposer un mot secret:")
    verif = verifAlphabet(secretWord)

#Le jeu commence !

listSecretWord = list(secretWord)
underSecretWord = []

for i in range(len(secretWord)):
    underSecretWord.append("_")

print("Le mot à trouver est le suivant\n{0}\nVous avez {1} vies".format(' '.join(underSecretWord),lifeNum))

#print(lenSecretWord)

while End == False:
    letter = input("Proposer une lettre:")
    coupNum += 1
    if letter in listSecretWord:
        for a in range(len(secretWord)):
            if secretWord[a] == letter:
                letterNum +=1
                underSecretWord[a] = letter

        print("la lettre est dans le mot, il y en a {0}\n{1}".format(letterNum, ' '.join(underSecretWord)))
        
    elif letter not in listSecretWord and verifAlphabet(letter) == True:
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
        print("{0}\nVous avez perdu\nLe mot était {1}".format(printPendu(lifeNum), secretWord))
        End = True
        
        

retry = input("Voulez-vous recommencer ?")
