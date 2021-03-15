/*********************************************
 * OPL 20.1.0.0 Model
 * Author: Sarra
 * Creation Date: 27 févr. 2021 at 18:57:28
 *********************************************/

int nbObjet = 60; // Pour l'exemple, sinon int nbObjet = ...;


range objets = 1 .. nbObjet;

int volumeObjet[objets] = [ 495 , 493 , 485 , 478 , 477 , 462 , 461 , 459 , 456 , 451 , 429 , 426 , 414 , 405 , 391 , 378 , 375 , 371 , 369 , 368 , 367 , 361 , 357 , 354 , 347 , 345 , 332 , 316 , 298 , 297 , 293 , 293 , 281 , 281 , 278 , 278 , 277 , 277 , 275 , 273 , 270 , 268 , 265 , 265 , 263 , 263 , 262 , 261 , 261 , 258 , 258 , 257 , 256 , 255 , 255 , 254 , 254 , 252 , 250 , 250 ]; // int volume[objets] = ...;

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