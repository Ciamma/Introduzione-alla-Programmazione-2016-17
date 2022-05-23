'''Definire una classe Punto, una classe Colore ed una classe Rettangolo secondo le seguenti specifiche.

La classe Punto rappresenta un punto. Deve implementare i seguenti metodi:

- Costruttore con argomenti (opzionali) x=0,y=0  che inizializza un punto di coordinate (x,y). Si assume che x e y sono interi non negativi.
- modifica_punto(x1,y1) modifica le coordinate dell'oggetto in (x1,y1)
- to_tuple() ritorna la tupla (x,y) delle coordinate dell'oggetto



La classe Colore deve implementare i seguenti metodi:

- Costruttore con argomenti (opzionali) r=0,g=0,b=0  che inizializza un colore  con la terna RGB (r,g,b). 
- modifica_colore(r1,g1,b1) modifica l'oggetto assegnandogli il  colore RGB (r1,g1,b1)
- miscela(c) restituisce una nuova istanza colore i cui valori sono una miscela dell'istanza corrente  con il colore c. 
  Nella miscela di due colori ogni canale RGB e' definito  da int((c1+c2)/2) dove c1 e c2 sono i valori dello stesso canale 
  RGB dei due colori di partenza.
- to_tuple() ritorna la tupla (r,g,b)  dell'oggetto colore.

La classe Rettangolo deve implementare i seguenti metodi:

- Costruttore con argomenti puntoInizio, larghezza, lunghezza e colore. puntoInizio e' un oggetto della classe Punto 
  e rappresenta il punto in alto a sinistra di un rettangolo di larghezza  parallela all'asse x e altezza parallela all'asse y.
  Di tale rettangolo  vengono dati  la larghezza e l'altezza  mediante i due  interi larghezza e altezza
  e il colore mediante un oggetto della classe Colore. Modificando, tramite i metodi visti sopra, gli oggetti puntoInizio e colore 
  deve modificarsi coerentemente anche l'oggetto rettangolo.


- inter(r) ritorna un' istanza del rettangolo che si ottiene  dall'intersezione dell'istanza attuale con il  rettangolo  r. 
  Il colore del nuovo rettangolo e' la miscela dei colori dei due rettangoli originali.
  Se i due rettangoli non si intersecano viene restituito None.
  Ad esempio dall'intersezione dei due  rettangoli A e B dove:
  A e' il rettangolo con punto di inzio (100,40), larghezza 70, lunghezza 40 e colore (200,200,200) e
  B e' il rettangolo con punto di inzio (120,90), larghezza 40, lunghezza 60 e colore (100,100,100)
  si ottiene il rettangolo con punto di inizio (120,90), larghezza 20, lunghezza 20 e colore (150,150,150)

- super(r) ritorna un'istanza del rettangolo di lunghezza minima e di altezza minima in grado di ricoprire l'area occupata 
  dall'oggetto e dal rettangolo  r. Il colore del nuovo rettangolo e' la miscela dei colori dei due rettangoli originali.

- foto(lista,fname_out) dove lista e' una lista contenente istanze di rettangolo e fname_out e' il nome di un file,  
  crea una immagine in formato PNG e la salva nel file fname_out. L'immagine ha le stesse dimensioni dell'istanza del rettangolo
  che invoca il metodo e fotografa la zona di spazio occupata dal rettangolo dopo che sul piano sono stati sistemati in sequenza 
  i rettangoli che compaiono in lista.

- il metodo speciale __str__ che per il rettangolo produce in una stringa  di testo su quattro righe le informazioni 
  sull'istanza ( vale a dire il punto di inizio, la larghezza, la lunghezza e il colore).
  Ad esempio per il rettangolo con punto di inzio (100,20), larghezza 60, lunghezza 90 e colore (0,250,0) deve restituire:
  'punto di inizio:(100,20)\nlarghezza:60\nlunghezza:90\ncolore(0,255,0)' 

Se necessario, si possono aggiungere altri metodi alle classi.

Per gli esempi vedere il file grade01.txt.

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non importare moduli che non sono nella libreria standard o che non sono forniti
nella cartella dell'homework; non modificare i moduli importati. Se questo file e' piu' grande di 100KB o il grader non termina entro 5 minuti, il punteggio
dell'esercizio e' zero.  
'''

import png

def operazione(c1, c2):
    return int((c1+c2)/2)

def check(AX,AY, BX,BY, BH,BW, AH,AW):
    S0X0, S0X1 = AX , AX + AW
    S0Y0, S0Y1 = AY, AY + AH
    S1X0, S1X1 = BX, BX + BW
    S1Y0, S1Y1 = BY, BY + BH
    X_int = (S0X0 >= S1X0 and S0X0 < S1X1) or (S1X0 >= S0X0 and S1X0 < S0X1)
    Y_int = (S0Y0 >= S1Y0 and S0Y0 < S1Y1) or (S1Y0 >= S0Y0 and S1Y0 < S0Y1)
    intersezione = X_int and Y_int
    return intersezione

def crea_foto(lunghezza,larghezza,colore):
    pixels = []
    for j in range(lunghezza):
        row = []
        for i in range(larghezza):
            color = (colore.r,colore.g,colore.b)
            row.append(color)
        pixels.append(row)
    return pixels

def save(filename,img):
    pyimg= png.from_array(img,'RGB')
    pyimg.save(filename)

def set_pixel(i,j,c, pixels,w,h):
    if(0 <= i < w and 0 <= j < h):
        pixels[j][i] = c

def draw_quad(x,y, w,h,c, foto,foto_w,foto_h):
    for j in range(y, y+h):
        for i in range(x, x+w):
            color = (c.r, c.g, c.b)
            set_pixel(i,j,color, foto,foto_w,foto_h)


class Punto:
    def __init__(self, x, y):
        if x >= 0 and y >= 0:
            self. x, self.y = x,y

    def modifica_punto(self, x1, y1):
        self.x,self.y = x1, y1

    def to_tuple(self):
        return (self.x, self.y)

class Colore:
    def __init__(self, r = 0, g = 0, b = 0):
        self.r, self.g, self.b = r, g, b

    def modifica_colore(self, B,g1,b1):
        self.r, self.g, self.b = B, g1, b1

    def miscela(self, c):
        self.r = operazione(self.r, c.r)
        self.g = operazione(self.g, c.g)
        self.b = operazione(self.b, c.b)
        return Colore(self.r,self.g,self.b)

    def to_tuple(self):
        return (self.r, self.g, self.b)

class Rettangolo:
    def __init__(self, p, larghezza, lunghezza, colore):
        self.p = p
        self.larghezza = larghezza
        self.lunghezza = lunghezza
        self.colore = colore

    def inter(self, r):
        esito = check(self.p.x,self.p.y, r.p.x,r.p.y,r.lunghezza,r.larghezza, self.lunghezza,self.larghezza)
        if esito == True:
            ist = 'si intersecano'
            larghezza = abs((self.p.x + self.larghezza) - r.p.x)
            lunghezza = abs((self.p.y + self.lunghezza) - r.p.y)
            colore = self.colore.miscela(r.colore)
            if self.p.x < r.p.x and self.p.y < r.p.y:
                punto = Punto(r.p.x,r.p.y)
            else:
                punto = Punto(self.p.x,self.p.y)
            ist = Rettangolo(punto,larghezza,lunghezza,colore)
        else:
            ist = 'non si intersecano'
            ist = None
        return ist

    def super(self, r):
        x = min(self.p.x, r.p.x)
        y = min(self.p.y, r.p.y)
        punto = Punto(x,y)
        colore = self.colore.miscela(r.colore)
        l = max(self.p.x, r.p.x)
        if l == self.p.x:
            larghezza = (l + self.larghezza) - punto.x
        else:
             larghezza = (l + r.larghezza) - punto.x
        ll = max(self.p.y, r.p.y)
        if ll == self.p.y:
            lunghezza = (ll + self.lunghezza) - punto.y
        else:
            lunghezza = (ll + r.lunghezza) - punto.y
        sup = Rettangolo(punto,larghezza,lunghezza,colore)
        return sup

    def foto(self, lista,fname_out):
        # dove lista e' una lista contenente istanze di rettangolo e fname_out e' il nome di un file,
        # crea una immagine in formato PNG e la salva nel file fname_out. L'immagine ha le stesse dimensioni dell'istanza del rettangolo
        # che invoca il metodo e fotografa la zona di spazio occupata dal rettangolo dopo che sul piano sono stati sistemati in sequenza
        # i rettangoli che compaiono in lista
        photo = crea_foto(self.lunghezza,self.larghezza,self.colore)
        for r in lista:
            rettangolini = draw_quad((r.p.x-self.p.x),(r.p.y-self.p.y), r.larghezza, r.lunghezza,r.colore, photo,self.larghezza,self.lunghezza)
        save(fname_out,photo)

    def __str__(self):
        return 'punto di inizio:{}\nlarghezza:{}\nlunghezza:{}\ncolore:{}'.format(self.p.to_tuple(),self.larghezza,self.lunghezza, self.colore.to_tuple())

if __name__ == '__main__':
    p1 = Punto(50,70)
    c1 = Colore(255,0,0)
    r1 = Rettangolo(p1,150,100,c1)

    p2 = Punto(100,40)
    c2 = Colore(0,255,0)
    r2 = Rettangolo(p2,40,70,c2)

    p3 = Punto(120,90)
    c3 = Colore(0,0,255)
    r3 = Rettangolo(p3,60,40,c3)

    p4 = Punto(30,140)
    c4 = Colore(255,255,0)
    r4 = Rettangolo(p4,50,20,c4)

    p5 = Punto(130,20)
    c5 = Colore(0,255,255)
    r5 = Rettangolo(p5,50,20,c5)

    lista=[r2,r3,r4,r5]
    r1.foto(lista,'prova.png')