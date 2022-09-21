from VerifCaracters import verifAlphabet, replaceCaractere #Import de la verification des lettres/mots
from Display import printPendu #Import de l'affichage du pendu
import os #Import du librairie de référence
import time

def gameLoop():
    #Définition de variables pour plus tard
    End = False # variable de boucle tant que partie pas finie
    v = False # variable de boucle tant que verification d'un mot non fini
    lifeNum = 7 # compteur de vie (qui décrémente)
    letterNum = 0 #compteur du nombre de lettre
    coupNum = 0 #compteur du nombre de coup
    retry = "" #chaine de caractère (input) pour la question de relancer une partie
    usesLetters = []
    secretWord = input("Proposer un mot secret:")
    
    while v == False: #boucle de verification du mot secret pour être conforme aux conditions
        verif = verifAlphabet(secretWord) #verifie d'abord les chiffres, etc puis entre dans la boucle si non
        while verif ==False:
            print("Un/Des caractères ne sont pas valides.")
            secretWord = input("Proposer un mot secret:")
            verif = verifAlphabet(secretWord)

        propositionSecretWord = replaceCaractere(secretWord) #appel de fonction : remplaceCaractere
        if propositionSecretWord != secretWord: #condition si le mot contient des caractères spéciaux tels que èéàù etc et propose un mot plus conforme
            answerSecretWord = input("Votre mot \"{0}\" n'est pas conforme, preferez-vous celui ci : {1} (oui ou non)".format(secretWord,propositionSecretWord))
            while answerSecretWord != "non" and answerSecretWord != "oui":
                answerSecretWord = input("Votre mot \"{0}\" n'est pas conforme, preferez-vous celui ci : {1} (oui ou non)".format(secretWord,propositionSecretWord))
            if answerSecretWord == "oui":
                secretWord = propositionSecretWord
                v=True
            elif answerSecretWord == "non": # si non on recommence la boucle depuis le début
                secretWord = input("Proposer un mot secret:")
        else: 
            v=True
    time.sleep(3)
    os.system('cls')
    #print(secretWord)
    
    listSecretWord = list(secretWord) #creer une liste avec les caractères de secretWord pour le plaçage des lettres
    underSecretWord = [] #creer une liste vide qu'on remplira d'underscore pour l'affichage du mot

    for i in range(len(secretWord)):
        underSecretWord.append("_")
    
    #Le jeu commence !
        
    while End == False: #boucle de jeu
        print("Le mot à trouver est le suivant\n{0}\nVous avez {1} vies".format(' '.join(underSecretWord),lifeNum))
        if usesLetters != []: #si la liste des lettres utilisés n'est pas vide (pour éviter d'afficher une liste vide pour rien)
            print("Vous avez déjà utilisez ces lettres :\n{0}".format(', '.join(usesLetters)))
        v = False
        while v == False:
            letter = input("Proposer une lettre ou un mot:")
            verif = verifAlphabet(letter) #verifie d'abord les chiffres, etc puis entre dans la boucle si non
            while verif ==False: #si la verification n'est pas bonne, on enlève une vie et on recommence jusqu'à avoir un bon caractère
                lifeNum -= 1
                print("Un/Des caractères ne sont pas valides.\n{0}\nVous avez désormais {1} vies\n{2}".format(' '.join(underSecretWord),lifeNum,printPendu(lifeNum)))
                letter = input("Proposer une lettre ou un mot:")
                verif = verifAlphabet(letter)
            propositionletter = replaceCaractere(letter) #appel de fonction : remplaceCaractere
            if propositionletter != letter: #condition si le mot contient des caractères spéciaux tels que èéàù etc et propose un mot plus conforme
                answerletter = input("Votre lettre/mot \"{0}\" n'est pas conforme, preferez-vous celui ci : {1} (oui ou non)".format(letter,propositionletter))
                while answerletter != "non" and answerletter != "oui":
                    answerletter = input("Votre lettre/mot \"{0}\" n'est pas conforme, preferez-vous celui ci : {1} (oui ou non)".format(letter,propositionletter))
                if answerletter == "oui":
                    letter = propositionletter
                    v=True
                elif answerletter == "non": # si non on recommence la boucle depuis le début
                    letter = input("Proposer une lettre ou un mot:")
            else: 
                v=True
        coupNum += 1 #incrémentation du compteur de coups
        print("____________________________________________________________________________________________________\n____________________________________________________________________________________________________\n")
        if letter in listSecretWord: #si la lettre est dans le mot, remplace l'underscore correspondant par la lettre
            for a in range(len(secretWord)):
                if secretWord[a] == letter:
                    letterNum +=1
                    underSecretWord[a] = letter

            print("la lettre est dans le mot, il y en a {0}\n{1}".format(letterNum, ' '.join(underSecretWord))) # donc print ce message

        elif letter not in listSecretWord: #sinon si la lettre n'est pas dans la liste du mot
            if len(letter) != len(secretWord) and len(letter) != 1: #si la taille de "lettre" est différente de 1 (pour une lettre) et de la taille du mot secret
                print("Vous avez entré trop/pas assez de lettres")
            elif len(letter) == len(secretWord): #sinon si les tailles des lettres et mots correspondent
                if letter == secretWord:#si la "lettre" est en fait le mot secret alors on remplit tout les underscores par les lettres
                    underSecretWord = listSecretWord
                elif letter != secretWord:#si la "lettre" n'est en fait pas le mot secret alors on perd une vie
                    lifeNum -= 1
                    print("Ceci n'est pas le mot secret!\n{0}\nVous avez désormais {1} vies\n{2}".format(' '.join(underSecretWord),lifeNum,printPendu(lifeNum)))                
            else: #sinon (=si la lettre n'est tout simplement pas dans le mot) on perd une vie
                lifeNum -= 1

                print("La lettre n'est pas dans le mot.\n{0}\nVous avez {1} vies\n{2}".format(' '.join(underSecretWord),lifeNum,printPendu(lifeNum)))

        letterNum = 0 #remise à zero du compteur de nombre d'apparition de la lettre pour la prochaine instance de la boucle
        usesLetters.append(letter) # ajout de la lettre à la liste des lettres utilisées 
        print("\n----------------------------------------------------------------------------------------------------\n")
        if underSecretWord == listSecretWord: # si on a gagné on sort la boucle tant que
            print("vous avez gagné en {0} coup !".format(coupNum))
            End = True

        elif lifeNum == 0: # si le nombre de vie tombe à zero, alors on a perdu et on sort de la boucle tant que
            print("\nVous avez perdu\nLe mot était {0}".format(secretWord))
            End = True

    while retry != "non" or retry != "oui": # boucle tant que  pour savoir s'il faut relancer une partie
        retry = input("Voulez-vous recommencer ?")
        if retry != "non" and retry != "oui":
            print("Ce n'est pas une réponse valable, veuillez me répondre par oui ou non.")
        elif retry == "oui":
            print("D'accord, je vous lance une nouvelle partie !")
            time.sleep(3)
            os.system('cls')
            return True
        elif retry == "non":
            print("D'accord, j'espère que ça vous a plu ! Bonne journée")
            time.sleep(3)
            os.system('cls')
            return False

firstParti = gameLoop() #lancement de la première partie pour amorcer la boucle while suivante dans le cas où  retry == "oui"
#appel de la fonction pour une première partie
while firstParti == True: #boucle de retry pour la fonction
    otherParti = gameLoop() #on lance la nouvelle partie à chaque instance de la boucle
    if otherParti == False: # condition pour vérifier si la valeur de "retry" a changé entre temps
        firstParti = False # auquel cas on sort de la boucle ce qui met fin à l'execution du programme