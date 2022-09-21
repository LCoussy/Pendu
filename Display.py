def printPendu(x):
    """Affichage du pendu

    Args:
        x (int): nombre de vie du joueur 

    Returns:
        string: l'affichage du pendu qu'il faut print
    """
    nb = str(x)
    fichier = "ASCII"
    f = open("LifeStage/{0}{1}.txt".format(fichier, nb),"r")
    a = f.read()
    f.close
    return a