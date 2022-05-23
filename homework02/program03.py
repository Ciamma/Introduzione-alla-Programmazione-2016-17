'''Il vicinato in diagonale di un pixel p di un'immagine e' costituito dai
 pixel adiacenti a p  per diagonale. Se p e' un pixel di bordo, il vicinato
in diagonale non comprende i pixel non contenuti nell'immagine.

Chiamiamo doub la seguente trasformazione di un'immagine:
ogni pixel viene sostituito da un quadrato di 4 pixel (In questo modo
la nuova immagine avra' lunghezza e larghezza doppie rispetto all'immagine
originale). I colori
dei  4  pixel di ciascun  quadrato introdotto sono definiti come segue.
Il colore del pixel  in alto a sinistra e' uguale al colore del pixel che
e' stato sostituito dal  quadrato di pixel.
Il colore del pixel in basso a destra e' uguale  alla media dei colori del suo
vicinato in diagonale. Infine, i restanti  due pixel del quadrato hanno colore
nero. 

La media dei colori si ottiene facendo la media su ognuno dei tre canali RGB.
Ad esempio, la media del canale RED e' data da int(round(sum_r/float(n))
dove sum_r e' la somma delle intensita' di red dei pixel del vicinato e n
e' il numero di pixel del vicinato.

Scrivere una funzione doub(fname_in, fname_out) che presa in input un'immagine
in formato PNG nel file fname_in applica  la trasformazione doub all'immagine e
salva l'immagine ottenuta nel file fname_out. 

Per gli esempi vedere il file grade03.txt

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard.
ATTENZIONE: Se il grader non termina entro 5 minuti il punteggio
dell'esercizio e' zero.'''



import png


def doub(fname_in, fname_out):
    '''Implementare qui la funzione'''



