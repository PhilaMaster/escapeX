Escape X è un gioco il cui obiettivo è quello di superare 10 (X) livelli.
Lo scopo di ogni livello è arrivare al punto di uscita, prima dello scadere del
tempo, senza toccare mura, e senza essere uccisi dai mostri.

Il codice è strutturato in modo da creare dei livelli a partire da matrici di caratteri,
(in realtà liste di stringhe), del tipo :

livello = [  # 2
    "WWWWWWWWWWWWWWWWWW",
    "W    EE         EW",
    "W   EE       E  2W",
    "WWWWWWWWPPWWWWWWWW",
    "W 1              W",
    "W       KK       W",
    "W           1    W",
    "WH      WW      HW",
    "W  1             W",
    "W               1W",
    "WWWWWWWWWWWWWWWWWW",
    "                  ",
]
(Questo ad esempio è proprio il livello 2 del gioco, superate il primo livello per
vederne la corrispondenza)
A ogni lettera sono attribuite delle proprietà specifiche secondo la seguente legenda:

LEGENDA
W = Wall/Muro
E = Exit/Uscita
K = Key/Chiave
I = Invisible/Muro invisibile
P = Porta/Porta
H = Horizontal/Mostro che si muove in orizzontale
V = Vertical/  Mostro che si muove in verticale
1 = Stellina livello 1, +50 punti
2 = Stellina livello 2, +500 punti

Giocare è molto semplice, per muoversi basta usare i tasti WASD, i punti verranno assegnati
nel modo seguente:
Aprire una porta : +25 punti 
Prendere una stellina livello 1 : +50 punti
Prendere una stellina livello 2 : +500 punti
Ogni secondo rimanente alla fine di ogni livello: +25 punti
Ogni morte : -100 punti
(i punti guadagnati nel corso di un livello, in caso di morte, verranno comunque annullati)

Insomma, il fine del gioco è di arrivare all'ultimo livello col maggior punteggio possibile,
(quindi anche nel minor tempo), questo è tutto, buona fortuna!