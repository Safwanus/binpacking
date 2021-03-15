/*********************************************
 * OPL 20.1.0.0 Model
 * Author: Sarra
 * Creation Date: 27 févr. 2021 at 18:57:28
 *********************************************/

int nbObjet = 50; // Pour l'exemple, sinon int nbObjet = ...;


range objets = 1 .. nbObjet;

int volumeObjet[objets] = [ 99 , 99 , 96 , 96 , 92 , 92 , 91 , 88 , 87 , 86 , 85 , 76 , 74 , 72 , 69 , 67 , 67 , 62 , 61 , 56 , 52 , 51 , 49 , 46 , 44 , 42 , 40 , 40 , 33 , 33 , 30 , 30 , 29 , 28 , 28 , 27 , 25 , 24 , 23 , 22 , 21 , 20 , 17 , 14 , 13 , 11 , 10 , 7 , 7 , 3 ]; // int volume[objets] = ...;

int volumeBoites = 100; // int volumesBoites = ...;

dvar boolean y[objets];

dvar boolean x[objets][objets]; // la premiere colonne est les objets, et la deuxieme est les boites.


minimize
    sum(i in objets) y[i]; // Nb de boites utilisés
subject to {
   
   
    forall(i in objets)
        sum(j in objets) (volumeObjet[j]*x[i][j]) <= volumeBoites * y[i];
       
    forall(j in objets)
         sum(i in objets) x[i][j] == 1;
        
   
     
}