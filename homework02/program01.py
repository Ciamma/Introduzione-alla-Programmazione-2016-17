'''Scrivere una funzione com_url(u1, u2, enc,k) che legge le pagine agli
indirizzi URL u1 e u2, le decodifica tramite la codifica enc e ritorna la
lista  delle parole di lunghezza k che occorrono in entrambe le pagine e il numero delle loro
occorrenze in ciascuna delle pagine.
Piu' precisamente la lista ritornata contiene terne. La terna (word, occ1, occ2) appartiene alla
lista se la parola word  occorre in entrambe le pagine ed ha lunghezza k, occ1 e' il numero
di volte che la parola word occorre nella pagina  di indrizzo u1 e occ2 il numero di volte che
la parola word occorre  nella pagina di indirizzo u2.
La lista ritornata deve riportare le terne ordinate per numero totale di occorrenze decrescente e,
a parita' di occorrenze, le terne sono ordinate rispetto alla prima coordinata. 
Per parola si intende una qualsiasi sequenza di caratteri alfabetici consecutivi
di lunghezza massimale. Un carattere e' alfabetico se il metodo isalpha() ritorna True. Tutte le parole
devono essere ridotte in minuscole. 

Per gli esempi vedere il file grade01.txt

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard.
ATTENZIONE: Se il grader non termina entro 5 minuti il punteggio
dell'esercizio e' zero.
'''
    

from urllib.request import urlopen



def noalpha(s):
    noa = ''
    for c in s:
        if not c.isalpha() and c not in noa:
            noa += c
    return noa

def words(s):
    noa = noalpha(s)
    for c in noa:
        s = s.replace(c, ' ')
    return s.split()

def URL(url,enc):
    with urlopen(url) as page:
        testo = page.read()
        testo = testo.decode(enc)
    return words(testo.lower())

def ordine(parole):
    return parole[1]+parole[2]
def ordine_1(lettere):
    return lettere[0]


def com_url(u1, u2,enc, k):
    lista_parole = []
    parola = []
    page_1 = URL(u1,enc)
    page_2 = URL(u2,enc)
    for w in page_1:
        if len(w) == k and w in page_2:
            parola = [w, page_1.count(w), page_2.count(w)]
            parola = tuple(parola)
            if parola not in lista_parole:
                lista_parole.append(parola)
    Lista = (sorted(sorted(lista_parole, key = ordine_1), key = ordine, reverse = True))
    return Lista