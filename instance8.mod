/*********************************************
 * OPL 20.1.0.0 Model
 * Author: Sarra
 * Creation Date: 27 f�vr. 2021 at 18:57:28
 *********************************************/

int nbObjet = 7; // Pour l'exemple, sinon int nbObjet = ...;


range objets = 1 .. nbObjet;

int volumeObjet[objets] = [8, 5, 7, 6, 2, 4, 1]; // int volume[objets] = ...;

int volumeBoites = 10; // int volumesBoites = ...;

dvar boolean y[objets];

dvar boolean x[objets][objets]; // la premiere colonne est les objets, et la deuxieme est les boites.


minimize
    sum(i in objets) y[i]; // Nb de boites utilis�s
subject to {
   
   
    forall(i in objets)
        sum(j in objets) (volumeObjet[j]*x[i][j]) <= volumeBoites * y[i];
       
    forall(j in objets)
         sum(i in objets) x[i][j] == 1;
        
   
     
}