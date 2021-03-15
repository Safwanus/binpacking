/*********************************************
 * OPL 20.1.0.0 Model
 * Author: Sarra
 * Creation Date: 27 févr. 2021 at 18:57:28
 *********************************************/

int nbObjet = 50; // Pour l'exemple, sinon int nbObjet = ...;


range objets = 1 .. nbObjet;

int volumeObjet[objets] = [ 100 , 99 , 98 , 96 , 94 , 90 , 89 , 88 , 88 , 86 , 84 , 81 , 81 , 80 , 79 , 79 , 78 , 76 , 72 , 72 , 72 , 68 , 68 , 65 , 63 , 63 , 63 , 62 , 62 , 57 , 57 , 55 , 48 , 48 , 47 , 45 , 44 , 44 , 41 , 39 , 36 , 33 , 31 , 30 , 28 , 26 , 25 , 24 , 22 , 20 ]; // int volume[objets] = ...;

int volumeBoites = 120; // int volumesBoites = ...;

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