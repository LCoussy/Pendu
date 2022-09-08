def affichage(x):
    nb = str(x)
    fichier = "ASCII"
    f = open(fichier + nb + ".txt","r")
    a = f.read()
    print(a)
    f.close
