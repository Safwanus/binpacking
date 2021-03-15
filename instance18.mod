/*********************************************
 * OPL 20.1.0.0 Model
 * Author: Sarra
 * Creation Date: 27 févr. 2021 at 18:57:28
 *********************************************/

int nbObjet = 50; // Pour l'exemple, sinon int nbObjet = ...;


range objets = 1 .. nbObjet;

int volumeObjet[objets] = [ 98 , 97 , 97 , 97 , 94 , 91 , 89 , 85 , 84 , 82 , 81 , 80 , 79 , 79 , 75 , 73 , 70 , 69 , 69 , 69 , 68 , 68 , 68 , 66 , 61 , 55 , 54 , 52 , 52 , 51 , 51 , 49 , 49 , 48 , 47 , 47 , 47 , 45 , 44 , 37 , 37 , 36 , 35 , 34 , 34 , 30 , 29 , 29 , 27 , 24 ]; // int volume[objets] = ...;

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