
from lireFichierBiblioteque import *
import time
from random import seed
from random import randint





def afficheTab(tabTaillesObjs, tailleBoite):
    print("Taille des boites : ", tailleBoite)
    print("Taille des objets : [ ", end = '')
    for i in range(len(tabTaillesObjs)):
        if(i == (len(tabTaillesObjs)-1)):
            print(tabTaillesObjs[i], end='')
        else :
            print(tabTaillesObjs[i],", ", end='')
    print(" ]")


def genereListeTailleObjets(nbObjets, tailleMax):
    seed(1)
    tailleObjets = []
    for i in range(nbObjets):
        value = randint(1, tailleMax)
        tailleObjets.append(value)
    return tailleObjets


def nextFit( tabTaillesObjs, tailleBoite):

    print("\n\n\n\n\t#_____________________________________________________________#\n")

    print("\t################ Algorithme glouton Next-Fit ##################")
    print("\t#_____________________________________________________________#\n\n")

    tailleBoite2 = tailleBoite
    print("\nInstance :\n ")
    afficheTab(tailleObjets, tailleBoite)
    boites = []
    boite = []

    nbBoites = 1
    if(len(tabTaillesObjs) == 0):
        nbBoites = 0

    start_time = time.time()
    for tObj in (tabTaillesObjs):
        if(tObj <= tailleBoite):
            boite.append(tObj)
            tailleBoite = tailleBoite - tObj
        else :
            boites.append(boite)
            boite = []
            nbBoites = nbBoites + 1
            tailleBoite = tailleBoite2 - tObj
            boite.append(tObj)

    tempsDExecution = time.time() - start_time
    if(len(boite) != 0):
        boites.append(boite)

    print("\nLe nombre de boîtes nécessaires en utilisant l'algorithme de Next Fit est : ", nbBoites, "\n")
    print("Voici la composition des boites", boites)
    print("\nLe temps d'execution est de ", tempsDExecution)


def retournerNextFit( tabTaillesObjs, tailleBoite):
    tailleBoite2 = tailleBoite
    boites = []
    boite = []

    nbBoites = 1
    if(len(tabTaillesObjs) == 0):
        nbBoites = 0

    start_time = time.time()
    for tObj in (tabTaillesObjs):
        if(tObj <= tailleBoite):
            boite.append(tObj)
            tailleBoite = tailleBoite - tObj
        else :
            boites.append(boite)
            boite = []
            nbBoites = nbBoites + 1
            tailleBoite = tailleBoite2 - tObj
            boite.append(tObj)

    tempsDExecution = time.time() - start_time
    if(len(boite) != 0):
        boites.append(boite)
    
    return nbBoites, boites, tempsDExecution







def firstFit( tabTaillesObjs, tailleBoite):

    print("\n\n\n\n\t#_____________________________________________________________#\n")

    print("\t################ Algorithme glouton First-Fit #################")
    print("\t#_____________________________________________________________#\n\n")

    print("\nInstance :\n ")
    afficheTab(tailleObjets, tailleBoite)
    boites = []
    boite = []


    if(len(tabTaillesObjs) == 0):
        nbBoites = 0

    start_time = time.time()
    for tObj in (tabTaillesObjs):
        traite = 0
        for b in boites :
            if( tObj <= (tailleBoite - sum(b)) ) :
                b.append(tObj)
                traite = 1
                break
        if(traite == 0):
            boite = []
            boite.append(tObj)
            boites.append(boite)
    tempsDExecution = time.time() - start_time

    nbBoites = len(boites)    
    print("\nLe nombre de boîtes nécessaires en utilisant l'algorithme de First Fit est : ", nbBoites, "\n")
    print("Voici la composition des boites", boites, "\n")
    print("Le temps d'execution est de ", tempsDExecution)

  

def retournerFirstFit( tabTaillesObjs, tailleBoite):
    boites = []
    boite = []

    nbBoites = 1
    if(len(tabTaillesObjs) == 0):
        nbBoites = 0
    start_time = time.time()
    for tObj in (tabTaillesObjs):
        traite = 0
        for b in boites :
            if( tObj <= (tailleBoite - sum(b)) ) :
                b.append(tObj)
                traite = 1
                break
        if(traite == 0):
            boite = []
            boite.append(tObj)
            boites.append(boite)
    tempsDExecution = time.time() - start_time
    nbBoites = len(boites)    
    return nbBoites, boites, tempsDExecution

 

def firstFitDecreasing( tabTaillesObjs, tailleBoite):

    print("\n\n\n\n\t#_____________________________________________________________#\n")

    print("\t########### Algorithme glouton First-Fit Decreasing ###########")
    print("\t#_____________________________________________________________#\n\n")

    print("\nInstance :\n ")
    afficheTab(tailleObjets, tailleBoite)
    boites = []

    start_time = time.time()
    #trier  la liste des tailles dansl’ordre décroissant
    tabTaillesObjsTrie = sorted(tabTaillesObjs, reverse = True)

    #on lance l'algorithme First Fit
    nbBoites, boites, t = retournerFirstFit(tabTaillesObjsTrie, tailleBoite)
    tempsDExecution = time.time() - start_time
    
    print("\nLe nombre de boîtes nécessaires en utilisant l'algorithme de First-Fit Decreasing est : ", nbBoites, "\n")
    print("Voici la composition des boites", boites, "\n")
    print("Le temps d'execution est de ", tempsDExecution)



def retournerFirstFitDecreasing( tabTaillesObjs, tailleBoite):
    boites = []

    start_time = time.time()
    tabTaillesObjsTrie = sorted(tabTaillesObjs, reverse = True)

    nbBoites, boites, t = retournerFirstFit(tabTaillesObjsTrie, tailleBoite)
    tempsDExecution = time.time() - start_time

    return nbBoites, boites, tempsDExecution





def worstFit( tabTaillesObjs, tailleBoite):

    print("\n\n\n\n\t#_____________________________________________________________#\n")

    print("\t################ Algorithme glouton Worst-Fit #################")
    print("\t#_____________________________________________________________#\n\n")

    print("\nInstance :\n ")
    afficheTab(tailleObjets, tailleBoite)
    boites = []
    boite = []

    nbBoites = 1
    if(len(tabTaillesObjs) == 0):
        nbBoites = 0

    start_time = time.time()
    for tObj in (tabTaillesObjs):
        espaceRestant = []

        for b in boites :
            if( tObj <= (tailleBoite - sum(b)) ) :
                espaceRestant.append(tailleBoite - sum(b))
            else:
                espaceRestant.append(0)
        if(len(espaceRestant) == 0 ):
            boite = []
            boite.append(tObj)
            boites.append(boite)
        else :
            maxEspaceRestant = max(espaceRestant)
            if(maxEspaceRestant == 0 ):
                boite = []
                boite.append(tObj)
                boites.append(boite)
            else :
                indiceMaxEspaceRestant = espaceRestant.index(maxEspaceRestant)
                boites[indiceMaxEspaceRestant].append(tObj)  
    tempsDExecution = time.time() - start_time
    nbBoites = len(boites)    
    print("\nLe nombre de boîtes nécessaires en utilisant l'algorithme de First Fit est : ", nbBoites, "\n")
    print("Voici la composition des boites", boites, "\n")
    print("Le temps d'execution est de ", tempsDExecution, "\n")




def retournerWorstFit( tabTaillesObjs, tailleBoite):

    boites = []
    boite = []

    nbBoites = 1
    if(len(tabTaillesObjs) == 0):
        nbBoites = 0
    start_time = time.time()
    for tObj in (tabTaillesObjs):
        espaceRestant = []

        for b in boites :
            if( tObj <= (tailleBoite - sum(b)) ) :
                espaceRestant.append(tailleBoite - sum(b))
            else:
                espaceRestant.append(0)
        if(len(espaceRestant) == 0 ):
            boite = []
            boite.append(tObj)
            boites.append(boite)
        else :
            maxEspaceRestant = max(espaceRestant)
            if(maxEspaceRestant == 0 ):
                boite = []
                boite.append(tObj)
                boites.append(boite)
            else :
                indiceMaxEspaceRestant = espaceRestant.index(maxEspaceRestant)
                boites[indiceMaxEspaceRestant].append(tObj)  
    tempsDExecution = time.time() - start_time
    nbBoites = len(boites)    
    return nbBoites, boites, tempsDExecution





def worstFitDecreasing( tabTaillesObjs, tailleBoite):

    print("\n\n\n\n\t#_____________________________________________________________#\n")

    print("\t########### Algorithme glouton Worst-Fit Decreasing ###########")
    print("\t#_____________________________________________________________#\n\n")

    print("\nInstance :\n ")
    afficheTab(tailleObjets, tailleBoite)
    boites = []
    
    start_time = time.time()

    tabTaillesObjsTrie = sorted(tabTaillesObjs, reverse = True)

    nbBoites, boites, t = retournerWorstFit(tabTaillesObjsTrie, tailleBoite)
    
    tempsDExecution = time.time() - start_time
    print("\nLe nombre de boîtes nécessaires en utilisant l'algorithme de First-Fit Decreasing est : ", nbBoites, "\n")
    print("Voici la composition des boites", boites, "\n")
    print("Le temps d'execution est de ", tempsDExecution, "\n")

def retournerWorstFitDecreasing( tabTaillesObjs, tailleBoite):
    boites = []
    
    start_time = time.time()

    tabTaillesObjsTrie = sorted(tabTaillesObjs, reverse = True)

    nbBoites, boites, t = retournerWorstFit(tabTaillesObjsTrie, tailleBoite)
    
    tempsDExecution = time.time() - start_time

    return nbBoites, boites, tempsDExecution





def bestFit( tabTaillesObjs, tailleBoite):

    print("\n\n\n\n\t#_____________________________________________________________#\n")

    print("\t################ Algorithme glouton Best-Fit #################")
    print("\t#_____________________________________________________________#\n\n")

    print("\nInstance :\n ")
    afficheTab(tailleObjets, tailleBoite)
    boites = []
    boite = []

    nbBoites = 1
    if(len(tabTaillesObjs) == 0):
        nbBoites = 0

    start_time = time.time()
    for tObj in (tabTaillesObjs):
        espaceRestant = []
        for b in boites :
            if( tObj <= (tailleBoite - sum(b)) ) :
                espaceRestant.append(tailleBoite - sum(b))
            else:
                espaceRestant.append(tailleBoite)
        if(len(espaceRestant) == 0 ):
            boite = []
            boite.append(tObj)
            boites.append(boite)
        else :
            minEspaceRestant = min(espaceRestant)
            if(minEspaceRestant == tailleBoite ):
                boite = []
                boite.append(tObj)
                boites.append(boite)
            else :
                indiceMinEspaceRestant = espaceRestant.index(minEspaceRestant)
                boites[indiceMinEspaceRestant].append(tObj)  
    tempsDExecution = time.time() - start_time
    nbBoites = len(boites)    
    print("\nLe nombre de boîtes nécessaires en utilisant l'algorithme de First Fit est : ", nbBoites, "\n")
    print("Voici la composition des boites", boites, "\n")
    print("Le temps d'execution est de ", tempsDExecution, "\n")




def retournerBestFit( tabTaillesObjs, tailleBoite):

    boites = []
    boite = []
    nbBoites = 1
    if(len(tabTaillesObjs) == 0):
        nbBoites = 0

    start_time = time.time()
    for tObj in (tabTaillesObjs):
        espaceRestant = []
        for b in boites :
            if( tObj <= (tailleBoite - sum(b)) ) :
                espaceRestant.append(tailleBoite - sum(b))
            else:
                espaceRestant.append(tailleBoite)
        if(len(espaceRestant) == 0 ):
            boite = []
            boite.append(tObj)
            boites.append(boite)
        else :
            minEspaceRestant = min(espaceRestant)
            if(minEspaceRestant == tailleBoite ):
                boite = []
                boite.append(tObj)
                boites.append(boite)
            else :
                indiceMinEspaceRestant = espaceRestant.index(minEspaceRestant)
                boites[indiceMinEspaceRestant].append(tObj)  
    
    tempsDExecution = time.time() - start_time
    nbBoites = len(boites) 
    return nbBoites, boites, tempsDExecution



def bestFitDecreasing( tabTaillesObjs, tailleBoite):

    print("\n\n\n\n\t#_____________________________________________________________#\n")

    print("\t########### Algorithme glouton Best-Fit Decreasing ###########")
    print("\t#_____________________________________________________________#\n\n")

    print("\nInstance :\n ")
    afficheTab(tailleObjets, tailleBoite)
    boites = []

    start_time = time.time()
    tabTaillesObjsTrie = sorted(tabTaillesObjs, reverse = True)

    nbBoites, boites, t = retournerBestFit(tabTaillesObjsTrie, tailleBoite)
    tempsDExecution = time.time() - start_time

    print("\nLe nombre de boîtes nécessaires en utilisant l'algorithme de First-Fit Decreasing est : ", nbBoites, "\n")
    print("Voici la composition des boites", boites, "\n")
    print("Le temps d'execution est de ", tempsDExecution, "\n")



def retournerBestFitDecreasing( tabTaillesObjs, tailleBoite):
    boites = []

    start_time = time.time()
    tabTaillesObjsTrie = sorted(tabTaillesObjs, reverse = True)

    nbBoites, boites, t = retournerBestFit(tabTaillesObjsTrie, tailleBoite)
    tempsDExecution = time.time() - start_time

    return nbBoites, boites, tempsDExecution







def comparaisonEntreHeuristiques(tabTaillesObjs, tailleBoite):

    print("\n\n")
    print("\t\t\t ________________________________________________\n")
    print("\t\t\t Comparaison en utilisant différents Heuristiques \t\t\t")
    print("\t\t\t ________________________________________________\n")

    print("\nInstance :\n ")
    print("Nombre d'objets : ", len(tabTaillesObjs))
    afficheTab(tailleObjets, tailleBoite)
    print("\n_______________________________________________________________________________________\n")

    print("\tHeuristique\t\tNombre de boites\t\ttemps d'execution\t\t")
    print("_______________________________________________________________________________________\n")

    nbBoiteNecessaire, boites, tempsDExecution = retournerNextFit(tabTaillesObjs, tailleBoite)
    print("\tNext-Fit :\t\t\t", nbBoiteNecessaire, "\t\t\t", tempsDExecution)

    nbBoiteNecessaire, boites, tempsDExecution = retournerFirstFit(tabTaillesObjs, tailleBoite)
    print("\tFirst-Fit :\t\t\t", nbBoiteNecessaire, "\t\t\t", tempsDExecution)

    nbBoiteNecessaire, boites, tempsDExecution = retournerFirstFitDecreasing(tabTaillesObjs, tailleBoite)
    print("\tFirst-Fit Decreasing :\t\t", nbBoiteNecessaire, "\t\t\t", tempsDExecution)

    nbBoiteNecessaire, boites, tempsDExecution = retournerWorstFit(tabTaillesObjs, tailleBoite)
    print("\tWorst-Fit :\t\t\t", nbBoiteNecessaire, "\t\t\t", tempsDExecution)

    nbBoiteNecessaire, boites, tempsDExecution = retournerWorstFitDecreasing(tabTaillesObjs, tailleBoite)
    print("\tWorst-Fit Decreasing :\t\t", nbBoiteNecessaire, "\t\t\t", tempsDExecution)

    nbBoiteNecessaire, boites, tempsDExecution = retournerBestFit(tabTaillesObjs, tailleBoite)
    print("\tBest-Fit :\t\t\t", nbBoiteNecessaire, "\t\t\t", tempsDExecution)

    nbBoiteNecessaire, boites, tempsDExecution = retournerBestFitDecreasing(tabTaillesObjs, tailleBoite)
    print("\tBest-Fit Decreasing :\t\t", nbBoiteNecessaire, "\t\t\t", tempsDExecution)

    print("________________________________________________________________________________________\n\n")






tailleBoite = 10
tailleObjets = [3, 4, 4, 3, 3, 2, 1]

nextFit(tailleObjets, tailleBoite)
firstFit(tailleObjets, tailleBoite)
firstFitDecreasing(tailleObjets, tailleBoite)
worstFit(tailleObjets, tailleBoite)
worstFitDecreasing(tailleObjets, tailleBoite)
bestFit(tailleObjets, tailleBoite)
bestFitDecreasing(tailleObjets, tailleBoite)





tailleBoite = 150
tailleObjets = [100, 22, 25, 51, 95, 58, 97, 30, 79, 23, 53, 80, 20, 65, 64, 21, 26, 100, 81, 98, 70, 85, 92, 97, 86, 71, 91, 29, 63, 34, 67, 23, 33, 89, 94, 47, 100, 37, 40, 58, 73, 39, 49, 79, 54, 57, 98, 69, 67, 49, 38, 34, 96, 27, 92, 82, 69, 45, 69, 20, 75, 97, 51, 70, 29, 91, 98, 77, 48, 45, 43, 61, 36, 82, 89, 94, 26, 35, 58, 58, 57, 46, 44, 91, 49, 52, 65, 42, 33, 60, 37, 57, 91, 52, 95, 84, 72, 75, 89, 81, 67, 74, 87, 60, 32, 76, 85, 59, 62, 39, 64, 52, 88, 45, 29, 88, 85, 54, 40, 57 ]

nextFit(tailleObjets, tailleBoite)
firstFit(tailleObjets, tailleBoite)
firstFitDecreasing(tailleObjets, tailleBoite)
worstFit(tailleObjets, tailleBoite)
worstFitDecreasing(tailleObjets, tailleBoite)
bestFit(tailleObjets, tailleBoite)
bestFitDecreasing(tailleObjets, tailleBoite)




tailleBoite = 10
tailleObjets = [2, 5, 4, 7, 1, 3, 8]

nextFit(tailleObjets, tailleBoite)
firstFit(tailleObjets, tailleBoite)
firstFitDecreasing(tailleObjets, tailleBoite)
worstFit(tailleObjets, tailleBoite)
worstFitDecreasing(tailleObjets, tailleBoite)
bestFit(tailleObjets, tailleBoite)
bestFitDecreasing(tailleObjets, tailleBoite)


tailleBoite = 10
tailleObjets = [5, 7, 5, 2, 4, 2, 5, 1, 6]

nextFit(tailleObjets, tailleBoite)
firstFit(tailleObjets, tailleBoite)
firstFitDecreasing(tailleObjets, tailleBoite)
worstFit(tailleObjets, tailleBoite)
worstFitDecreasing(tailleObjets, tailleBoite)
bestFit(tailleObjets, tailleBoite)
bestFitDecreasing(tailleObjets, tailleBoite)




tailleBoite = 10
tailleObjets = [2, 2, 3, 3, 6, 7]

nextFit(tailleObjets, tailleBoite)
firstFit(tailleObjets, tailleBoite)
firstFitDecreasing(tailleObjets, tailleBoite)
worstFit(tailleObjets, tailleBoite)
worstFitDecreasing(tailleObjets, tailleBoite)
bestFit(tailleObjets, tailleBoite)
bestFitDecreasing(tailleObjets, tailleBoite)


 

tailleBoite = 10
tailleObjets = [8, 5, 7, 6, 2, 4, 1]

nextFit(tailleObjets, tailleBoite)
firstFit(tailleObjets, tailleBoite)
firstFitDecreasing(tailleObjets, tailleBoite)
worstFit(tailleObjets, tailleBoite)
worstFitDecreasing(tailleObjets, tailleBoite)
bestFit(tailleObjets, tailleBoite)
bestFitDecreasing(tailleObjets, tailleBoite)




tailleBoite = 10
tailleObjets = [4, 4, 3, 3, 3, 2, 1]

nextFit(tailleObjets, tailleBoite)
firstFit(tailleObjets, tailleBoite)
firstFitDecreasing(tailleObjets, tailleBoite)
worstFit(tailleObjets, tailleBoite)
worstFitDecreasing(tailleObjets, tailleBoite)
bestFit(tailleObjets, tailleBoite)
bestFitDecreasing(tailleObjets, tailleBoite)

comparaisonEntreHeuristiques(tailleObjets, tailleBoite)



tailleBoite = 10
tailleObjets = [8, 5, 7, 6, 2, 4, 1]
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)



path = "./biblioteque/Falkenauer/Falkenauer_T/Falkenauer_t60_00.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)

#Instance 2 :

path = "./biblioteque/Falkenauer/Falkenauer_T/Falkenauer_t60_01.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Falkenauer/Falkenauer_T/Falkenauer_t60_02.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Falkenauer/Falkenauer_T/Falkenauer_t60_03.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Falkenauer/Falkenauer_T/Falkenauer_t60_04.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)



path = "./biblioteque/Falkenauer/Falkenauer_T/Falkenauer_t60_05.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Falkenauer/Falkenauer_T/Falkenauer_t501_19.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)



path = "./biblioteque/Falkenauer/Falkenauer_T/Falkenauer_t501_18.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Falkenauer/Falkenauer_T/Falkenauer_t501_17.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Falkenauer/Falkenauer_T/Falkenauer_t501_16.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)






path = "./biblioteque/Falkenauer/Falkenauer_U/Falkenauer_u120_00.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)



path = "./biblioteque/Falkenauer/Falkenauer_U/Falkenauer_u120_01.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Falkenauer/Falkenauer_U/Falkenauer_u120_02.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)



path = "./biblioteque/Falkenauer/Falkenauer_U/Falkenauer_u500_09.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Falkenauer/Falkenauer_U/Falkenauer_u1000_02.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Falkenauer/Falkenauer_U/Falkenauer_u1000_14.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Falkenauer/Falkenauer_U/Falkenauer_u1000_17.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Falkenauer/Falkenauer_U/Falkenauer_u1000_18.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Falkenauer/Falkenauer_U/Falkenauer_u1000_19.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)




path = "./biblioteque/Scholl/Scholl_1/N1C1W1_A.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Scholl/Scholl_1/N1C1W2_R.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Scholl/Scholl_1/N1C2W2_O.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Scholl/Scholl_1/N1C2W4_H.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)



path = "./biblioteque/Scholl/Scholl_1/N4C3W4_T.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)





path = "./biblioteque/Scholl/Scholl_2/N4W4B2R7.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Scholl/Scholl_2/N4W4B2R8.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Scholl/Scholl_2/N4W4B3R3.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Scholl/Scholl_2/N4W4B3R5.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)



path = "./biblioteque/Scholl/Scholl_2/N4W4B3R6.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)






path = "./biblioteque/Randomly_Generated/BPP_1000_1000_0.2_0.8_5.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Randomly_Generated/BPP_1000_1000_0.2_0.8_6.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Randomly_Generated/BPP_1000_1000_0.2_0.8_7.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Randomly_Generated/BPP_1000_1000_0.2_0.8_8.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)



path = "./biblioteque/Randomly_Generated/BPP_1000_1000_0.2_0.8_9.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)



path = "./biblioteque/Irnich_BPP/csAA125_1.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Irnich_BPP/csBB500_17.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Irnich_BPP/csBB500_18.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)


path = "./biblioteque/Irnich_BPP/csBB500_19.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)



path = "./biblioteque/Irnich_BPP/csBB500_20.txt"
nbObjets, tailleBoite, tailleObjets = retournInstance(path)
comparaisonEntreHeuristiques(tailleObjets, tailleBoite)

