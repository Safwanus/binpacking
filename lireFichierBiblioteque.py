


def retournInstance(path):
    file = open(path, "r")

    nbObjets = int(file.readline())
    tailleBoite = int(file.readline())
    tailleObjets = []

    lignes = file.readlines()
    for ligne in lignes:
        tailleObjets.append(int(ligne))

    file.close()
    return nbObjets, tailleBoite, tailleObjets




