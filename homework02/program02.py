'''I post di un forum sono raccolti in alcuni file che hanno il seguente
formato. Un file contiene uno o piu' post. L'inizio di un post e' marcato da una
linea che contiene solamente la stringa "<POST>". Il contenuto del post e'
nelle linee successive fino alla linea che marca il prossimo post o la fine
del file (si veda il file "file02_01_in.txt"). E' assicurato che la stringa
"<POST>" non e' contenuta in nessun post.
Scrivere una funzione post(fposts, k, t) che prende in input  il
percorso di un file fposts, che ha il formato suddetto e due  interi
positivi k e t, e restituisce una coppia (dizionario, lista).
Il dizionario ha per chiavi le parole che compaiono  nei post del file piu'
di k volte e non compaiono nel file "file02_stopwords.txt". Alla parola w del
dizionario e' associata la coppia di interi (x,y) dove x e' il numero di
differenti post
in cui la parola w appare e y il numero totale di occorrenze di w tra i post
del file.
La lista  contiene tutte le coppie (word, nocc) dove word e'
una parola che compare  nei post del file nocc volte con nocc
maggiore di t e non compare nel file "file02_stopwords.txt".
Le coppie (word, nocc) appaiono
nella lista ordinate per numero decrescente di occorrenze tra i post del
file e, a parita' di occorrenze, per ordine lessicografico crescente. 

Per parola intendiamo come al solito una qualsiasi sequenza di caratteri
alfabetici di lunghezza massimale. I caratteri alfabetici sono quelli per cui
ritorna True il metodo isalpha(). Tutte le parole devono essere ridotte alle
minuscole. Tutti i file devono essere decodificati con la codifica utf-8.

Per gli esempi vedere il file grade02.txt

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard.
ATTENZIONE: Se il grader non termina entro 5 minuti il punteggio
dell'esercizio e' zero.
'''
        

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

def ordine(parole): return parole[1]
def ordine_1(lettere): return lettere[0]

def ricerca_parole_x(w,lst):
    c = 0
    for p in lst:
        if w in p:
            c += 1
    return c

def post(fposts,k,t):
    diz = {}
    Lista = []
    lista_post = []
    Lista_parole = []
    with open('file02_stopwords.txt',encoding = 'utf-8-sig') as f:
        stop = words(f.read().lower())
    with open(fposts, encoding = 'utf-8-sig') as f:
        txt = f.read().lower()
    posts = txt.split('<post')
    txt_word = words(txt)
    for p in posts:
        lpw = p.find('>')
        if lpw != -1:
            ws = words(p.lower())
            lista_post.append(ws)
            for w in ws:
                if w not in stop and w != 'post':
                    Parole = []
                    y = txt_word.count(w)
                    x = ricerca_parole_x(w, lista_post)
                    Parole += w,x,y
                    if Parole not in Lista_parole:
                        Lista_parole.append(Parole)
    for p in Lista_parole:
        if p[2] > k:
            diz[p[0]] = (p[1],p[2])
        if p[2] > t:
            Lista.append((p[0],p[2]))
    lista = list(set(Lista))
    lista = sorted(sorted(lista, key = ordine_1,reverse = False), key = ordine,reverse = True)
    return((diz,list(lista)))