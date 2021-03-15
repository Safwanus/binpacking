/*********************************************
 * OPL 20.1.0.0 Model
 * Author: Sarra
 * Creation Date: 27 févr. 2021 at 18:57:28
 *********************************************/

int nbObjet = 120; // Pour l'exemple, sinon int nbObjet = ...;


range objets = 1 .. nbObjet;

int volumeObjet[objets] = [ 98 , 98 , 98 , 96 , 96 , 94 , 93 , 93 , 92 , 91 , 91 , 90 , 87 , 86 , 85 , 85 , 84 , 84 , 84 , 84 , 84 , 83 , 83 , 82 , 82 , 81 , 80 , 80 , 80 , 79 , 79 , 78 , 78 , 78 , 78 , 76 , 74 , 74 , 73 , 73 , 73 , 73 , 72 , 71 , 70 , 70 , 70 , 69 , 69 , 69 , 67 , 66 , 64 , 62 , 62 , 60 , 60 , 59 , 58 , 58 , 58 , 57 , 57 , 57 , 57 , 55 , 55 , 55 , 50 , 49 , 49 , 49 , 47 , 46 , 46 , 45 , 45 , 44 , 44 , 43 , 43 , 43 , 43 , 42 , 42 , 42 , 42 , 42 , 41 , 41 , 41 , 39 , 39 , 38 , 38 , 38 , 37 , 36 , 36 , 36 , 35 , 33 , 33 , 33 , 32 , 32 , 30 , 30 , 30 , 29 , 28 , 27 , 27 , 26 , 25 , 25 , 24 , 23 , 23 , 20 ]; // int volume[objets] = ...;

int volumeBoites = 150; // int volumesBoites = ...;

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