/*********************************************
 * OPL 20.1.0.0 Model
 * Author: Sarra
 * Creation Date: 27 févr. 2021 at 18:57:28
 *********************************************/

int nbObjet = 120; // Pour l'exemple, sinon int nbObjet = ...;


range objets = 1 .. nbObjet;

int volumeObjet[objets] = [ 100 , 100 , 98 , 97 , 97 , 96 , 94 , 92 , 92 , 91 , 91 , 90 , 90 , 90 , 88 , 85 , 84 , 84 , 84 , 83 , 81 , 81 , 80 , 80 , 80 , 80 , 79 , 79 , 79 , 76 , 76 , 75 , 75 , 74 , 73 , 70 , 69 , 69 , 68 , 68 , 67 , 67 , 67 , 67 , 66 , 66 , 66 , 65 , 64 , 64 , 64 , 64 , 64 , 62 , 62 , 61 , 61 , 60 , 59 , 59 , 57 , 53 , 53 , 51 , 51 , 50 , 50 , 48 , 48 , 48 , 47 , 46 , 46 , 46 , 45 , 45 , 44 , 42 , 42 , 41 , 41 , 40 , 38 , 38 , 38 , 37 , 37 , 37 , 37 , 36 , 36 , 35 , 35 , 34 , 34 , 33 , 32 , 32 , 32 , 31 , 31 , 30 , 29 , 29 , 29 , 29 , 28 , 28 , 27 , 26 , 26 , 25 , 24 , 24 , 23 , 23 , 22 , 21 , 21 , 20 ]; // int volume[objets] = ...;

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