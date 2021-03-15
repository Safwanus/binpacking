/*********************************************
 * OPL 20.1.0.0 Model
 * Author: Sarra
 * Creation Date: 27 févr. 2021 at 18:57:28
 *********************************************/

int nbObjet = 60; // Pour l'exemple, sinon int nbObjet = ...;


range objets = 1 .. nbObjet;

int volumeObjet[objets] = [ 498 , 498 , 494 , 482 , 482 , 479 , 476 , 464 , 459 , 436 , 430 , 429 , 401 , 400 , 398 , 390 , 378 , 369 , 367 , 362 , 354 , 352 , 350 , 350 , 345 , 339 , 328 , 326 , 308 , 305 , 288 , 288 , 284 , 281 , 280 , 279 , 277 , 276 , 271 , 268 , 267 , 267 , 267 , 266 , 263 , 262 , 261 , 261 , 260 , 260 , 259 , 256 , 254 , 252 , 252 , 251 , 251 , 250 , 250 , 250 ]; // int volume[objets] = ...;

int volumeBoites = 1000; // int volumesBoites = ...;

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