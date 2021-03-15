/*********************************************
 * OPL 20.1.0.0 Model
 * Author: Sarra
 * Creation Date: 27 févr. 2021 at 18:57:28
 *********************************************/

int nbObjet = 9; // Pour l'exemple, sinon int nbObjet = ...;


range objets = 1 .. nbObjet;

int volumeObjet[objets] = [5, 7, 5, 2, 4, 2, 5, 1, 6]; // int volume[objets] = ...;

int volumeBoites = 10; // int volumesBoites = ...;

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