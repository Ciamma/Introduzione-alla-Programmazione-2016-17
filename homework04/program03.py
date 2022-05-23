''' Scrivere una funzione burna(fimg, fimg_out, t, *pt) i cui argomenti hanno il
seguente significato:
- fimg: il percorso di un file che contiene un'immagine in formato PNG;
- fimg_out: una stringa contenente il percorso di un file;
- un intero positivo t
- *pt: sequenza variabile di argomenti ognuno dei quali e' una coppia (x, y) che da  le coordinate di un pixel dell'immagine.

La funzione legge l'immagine in fimg ed esegue una visita BFS sul grafo indotto dall'immagine,
in modo simile a quanto visto a lezione.
Le differenze con la BFS vista a lezione sono le seguenti:
1) il punto di partenza non e' un singolo pixel, ma ogni punto in *pt va considerato 
   un punto di partenza (e risulta quindi a distanza zero);
2) occorre considerare anche i pixel diagonali; pertanto  ogni pixel ha potenzialmente 8
   pixel adiacenti anziche' 4;
3) c'e' un arco tra ogni coppia di pixel adiacenti, indipendentemente dalla distanza dei loro colori.
   Il risultato di tale BFS va usato per creare una seconda immagine (da salvare in fimg_out)
   che è uguale all'immagine fimg, tranne che per le seguenti caratteristiche:
   3a) tutti i pixel che risultano a distanza inferiore a t (compresi quelli in *pt) dovranno 
      essere colorati con il colore dato dalla funzione bcolor(c, d), dove c e' il colore originale 
      del pixel e d la sua distanza calcolata dalla BFS; la funzione bcolor ritorna un colore 
      in cui ogni canale RGB è diminuito del doppio di d (se il valore risultante è negativo, 
      se ne prende il valore assoluto);
   3b) i pixel  a distanza t, t+1 e t+2 sono colorati con il  colore rosso (vale a dire (255,0,0)). 
   Pertanto, tutti i pixel che non rientrano nei 2 casi di cui sopra conservano il colore originario. 


Alcuni esempi:
- L'immagine 'img03_01_check.png' deve essere uguale a quella che la funzione 
  salva nel file 'img03_01_out.png' con la chiamata
  burna('img03_01_in.png', 'img03_01_out.png', 100, (250,200))
- L'immagine 'img03_02_check.png' deve essere uguale a quella che la funzione
  salva nel file 'img03_02_out.png' con la chiamata
  burna('img03_01_in.png', 'img03_02_out.png', 100, (150,200), (350,200))

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard o che non sono forniti
nella cartella dell'homework; non modificare i moduli importati. Se questo file
e' piu' grande di 100KB o il grader non termina entro 5 minuti, il punteggio
dell'esercizio e' zero.
'''

import png

def save(filename,img):
    pyimg= png.from_array(img,'RGB')
    pyimg.save(filename)

def load(filename):
    with open(filename,'rb') as f:
        iw, ih, png_img, a = png.Reader(file=f).asRGB8()
        img = []
        for png_row in png_img:
            row = []
            for i in range(0,len(png_row),3):
                row.append( (png_row[i+0],png_row[i+1],png_row[i+2]) )
            img.append( row )
    return img

def crea_foto(lunghezza,larghezza,colore):
    pixels = []
    for j in range(lunghezza):
        row = []
        for i in range(larghezza):
            row.append(colore)
        pixels.append(row)
    return pixels

def bcolor(c,d):
    r,g,b = 0,0,0
    r = abs(c[0] - (2*d))
    g = abs(c[1] - (2*d))
    b = abs(c[2] - (2*d))
    return (r,g,b)

def visit_tree_image(img,pt,end):
    visited = set()
    active = set()
    tree={}
    for e in pt:
        visited.add(e)
        active.add(e)
        tree[e] = 0
    while active:
        newactive = set()
        while active:
            i,j = active.pop()
            adj = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
            for di, dj in adj:
                ii, jj = i + di, j + dj
                if 0 <= ii < end[0] and 0 <= jj < end[1]:
                    if (ii, jj) not in visited:
                        visited.add((ii,jj))
                        newactive.add((ii,jj))
                        tree[(ii,jj)] = tree[(i,j)] + 1
        active = newactive
    return tree

def burna(fimg, fimg_out, t, *pt):
    img = load(fimg)
    imgf = crea_foto(len(img),len(img[0]),(0,0,0))
    end = (len(img[0]),len(img))
    tree = visit_tree_image(img, set(pt), end)
    for tupla, dist in tree.items():
        x,y = tupla
        if dist < t:
            imgf[y][x] = bcolor(img[y][x], dist)
        elif t <= dist <= t+2 :
            imgf[y][x] = (255,0,0)
        else:
            imgf[y][x] = img[y][x]
    save(fimg_out, imgf)