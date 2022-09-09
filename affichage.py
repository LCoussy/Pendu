def printPendu(x):
    nb = str(x)
    fichier = "ASCII"
    f = open("LifeStage/" + fichier + nb + ".txt","r")
    a = f.read()
    f.close
    return a
