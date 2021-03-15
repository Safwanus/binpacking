/*********************************************
 * OPL 20.1.0.0 Model
 * Author: Sarra
 * Creation Date: 27 f�vr. 2021 at 18:57:28
 *********************************************/

int nbObjet = 120; // Pour l'exemple, sinon int nbObjet = ...;


range objets = 1 .. nbObjet;

int volumeObjet[objets] = [ 100 , 100 , 99 , 99 , 98 , 98 , 98 , 98 , 98 , 97 , 97 , 97 , 95 , 95 , 95 , 94 , 92 , 90 , 90 , 88 , 88 , 85 , 82 , 81 , 81 , 81 , 80 , 80 , 80 , 79 , 79 , 78 , 78 , 76 , 75 , 75 , 74 , 72 , 72 , 71 , 70 , 70 , 70 , 68 , 67 , 67 , 67 , 67 , 66 , 66 , 65 , 65 , 64 , 62 , 61 , 61 , 60 , 60 , 60 , 59 , 58 , 57 , 57 , 57 , 55 , 55 , 53 , 53 , 53 , 53 , 53 , 53 , 52 , 52 , 50 , 49 , 49 , 48 , 48 , 47 , 47 , 47 , 46 , 46 , 45 , 45 , 45 , 44 , 43 , 43 , 43 , 41 , 39 , 39 , 39 , 38 , 38 , 37 , 36 , 36 , 36 , 35 , 33 , 32 , 30 , 30 , 29 , 29 , 27 , 27 , 27 , 25 , 24 , 23 , 23 , 22 , 22 , 22 , 20 , 20 ]; // int volume[objets] = ...;

int volumeBoites = 150; // int volumesBoites = ...;

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