'''Scrivere una funzione parole(a,b,txt) che ritorna una lista che all'indice i
ha una stringa contenente tutte le parole presenti  nella linea i della stringa
di input txt di lunghezza  almeno a ed al piu' b.
Per parola si intende una sequenza di caratteri alfabetici (maiuscoli o minuscoli)
di lunghezza massimale. Nella stringa in posisione i della lista di output, le
parole sono separate da un singolo spazio e devono apparire nello stesso
ordine con cui appaiono nella linea i di txt. Se la linea non ha  parole di
lunghezza tra a e b, la stringa corrispondente nella lista di output e' la stringa
vuota.
Il file grade03.txt contiene gli esempi usati dal grader.

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard.
'''

def noalpha(s):
    '''Ritorna una stringa contenente tutti i caratteri non
    alfabetici contenuti in s, senza ripetizioni'''
    noa = ''
    for c in s:
        if not (c in noa or c.isalpha()):
            noa += c
    return noa

def words(s):
    '''Ritorna la lista delle parole contenute nella stringa s'''
    noa = noalpha(s)
    for c in noa:
        s = s.replace(c, ' ')
    return s.split()

def parole(a,b,txt):
    List = []
    righe = txt.splitlines()
    for r in righe:
        ww = words(r)
        parola = ''
        for w in ww:
            if a <= len(w) <= b:
                if parola == '':
                    parola = w
                else:
                    parola = parola + ' ' + w
        List.append(parola)
    return List