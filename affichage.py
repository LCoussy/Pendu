def affichage(x):
    nb = str(x)
    fichier = "ASCII"
    f = open("LifeStage/" + fichier + nb + ".txt","r")
    a = f.read()
    print(a)
    f.close
