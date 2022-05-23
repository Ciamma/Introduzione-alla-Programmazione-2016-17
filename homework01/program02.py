'''Scrivere una funzione modi(la, lb) che prende in input due liste contenenti
uno stesso numero di stringhe, modifica le liste confrontando le stringhe che
occorrono nella stessa posizione nelle due liste e cancella dalla lista la
maggiore delle due,  se  sono uguali, sono cancellate entrambe.
Vedere il file grade02.txt che contiene gli esempi usati dal grader.



AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard.
'''


def modi(la,lb):
    lettere = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','10']
    lc = []
    i = 0
    for i in range(len(la)):
        a = la[i]
        b = lb[i]
        #print(a,b)
        if a > b:
            lc.append(a)
        elif a < b:
            lc.append(b)
        else:
            lc.append(a)
            lc.append(b)
    for p in lc:
        if p in la: la.remove(p)
        else: lb.remove(p)
    print(la,lb)