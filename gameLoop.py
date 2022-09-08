from VerifCaracters import verifAlphabet

verif = False

while verif == False:
    
    secretWord = input("Proposer un mot secret:")
    verif = verifAlphabet(secretWord)

#Le jeu commence !

listSecretWord = list(secretWord)
lenSecretWord = []

for i in range(len(secretWord)):
    lenSecretWord.append("_")

print("Le mot à trouver est le suivant\n{}".format(' '.join(lenSecretWord)))

