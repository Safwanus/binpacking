/*********************************************
 * OPL 20.1.0.0 Model
 * Author: Sarra
 * Creation Date: 27 févr. 2021 at 18:57:28
 *********************************************/

int nbObjet = 60; // Pour l'exemple, sinon int nbObjet = ...;


range objets = 1 .. nbObjet;

int volumeObjet[objets] = [ 495 , 474 , 473 , 472 , 466 , 450 , 445 , 444 , 439 , 430 , 419 , 414 , 410 , 395 , 372 , 370 , 366 , 366 , 366 , 363 , 361 , 357 , 355 , 351 , 350 , 350 , 347 , 320 , 315 , 307 , 303 , 299 , 298 , 298 , 292 , 288 , 287 , 283 , 275 , 275 , 274 , 273 , 273 , 272 , 272 , 271 , 269 , 269 , 268 , 263 , 262 , 261 , 259 , 258 , 255 , 254 , 252 , 252 , 252 , 251 ]; // int volume[objets] = ...;

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