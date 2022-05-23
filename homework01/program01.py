'''Scrivere una funzione mesi(lst) che ritorna una lista di lunghezza uguale a
quella della lista in input lst e che, per ogni i, se nella posizione i della
lista lst vi e' una stringa che codifica una data, allora in quella posizione la
nuova lista ha la stringa  corrispondente al nome del mese indicato nella data,
altrimenti ha il carattere '*'.
Una stringa che codifica una data  e' del tipo gg-mm-aaaa dove gg codifica il
giorno, mm  il mese e aaaa l'anno. Si puo' assumere che non sono presenti date
di anni bisestili.
Vedere il file grade01.txt che contiene gli esempi usati dal grader.

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard.
'''


def check_date(giorno,mese):
    if giorno <= 1: return False
    if mese == 2:
        return giorno <= 28
    elif mese in [4,6,9,11]:
        return giorno <= 30
    elif mese in [1,3,5,7,8,10,12]:
        return giorno <= 31
    else:
        return False

def verifica_numeri(num):
    ch = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','-','/']
    for n in num:
        if n in ch:
            return False
    return True

def mesi(lst):
    mesi = ['*','gennaio','febbraio','marzo','aprile','maggio','giugno','luglio','agosto','settembre','ottobre','novembre','dicembre']
    List = []
    for i in lst:
        if type(i) == str and len(i) == 10:
            giorno = i[0:2]
            mese = i[3:5]
            anno = i[6:10]
            if verifica_numeri(giorno) ==True and verifica_numeri(mese) == True and verifica_numeri(anno) == True:
                if check_date(int(giorno),int(mese)) == True:
                    List.append(mesi[int(mese)])
                else:
                    List.append(mesi[0])
            else:
                List.append(mesi[0])
        else:
            List.append(mesi[0])
    return List
   
