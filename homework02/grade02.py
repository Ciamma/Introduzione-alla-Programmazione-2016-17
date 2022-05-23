#! /usr/bin/env python3 -B

from testlib import check, runtests

def test_program02_1():
    import program02
    ret = program02.post('file02_01_in.txt', 0,1)
    check(ret,({u'immutabili': (1, 1), u'stringe': (1, 1), u'scusami': (1, 1), u'facevi': (1, 1),
                u'dovrebbe': (1, 1), u'ritorna': (1, 1), u'stringhe': (1, 1), u'replace': (4, 5),
                u'lst': (1, 2), u'qualsiasi': (1, 1), u'comunque': (1, 1), u'trovare': (1, 1),
                u'lettera': (1, 1), u'assegnarla': (1, 1), u'isalpha': (1, 1), u'servono': (1, 1),
                u'caratteri': (1, 1), u'if': (1, 1), u'ps': (1, 1), u'singoli': (1, 1), u'faccio': (1, 2),
                u'singolo': (1, 1), u'possibile': (1, 1), u'pensare': (1, 1), u'darti': (1, 1),
                u'creare': (1, 1), u'due': (1, 1), u'voglio': (1, 1), u'modificare': (1, 1),
                u'eliminata': (1, 1), u'grazie': (1, 1), u'eliminare': (1, 1), u'signola': (1, 2),
                u'indizio': (1, 1), u'utilizzare': (1, 1), u'bisogna': (1, 2), u'messaggio': (1, 1),
                u'modo': (1, 1), u'scorro': (1, 1), u'sostituirla': (1, 1), u'scorso': (1, 1),
                u'solo': (1, 1), u'credo': (1, 1), u'viene': (1, 1), u'parte': (1, 1), u'emento': (1, 1),
                u'modificarla': (1, 1), u'prover\xf2': (1, 1), u'ignora': (1, 1), u'interno': (1, 1),
                u'righe': (1, 1), u'not': (1, 1), u'nuova': (1, 2), u'seconda': (1, 1), u'lista': (1, 3),
                u'problema': (1, 1), u'elemento': (1, 1), u'modifiche': (1, 1), u'perch\xe8': (1, 1),
                u'metodo': (1, 1), u'codice': (1, 1), u'funziona': (1, 1), u'punteggiatura': (1, 1),
                u'carattere': (1, 1), u'modifica': (1, 1), u'stringa': (3, 8), u'spazi': (1, 1),
                u'variabile': (1, 1), u'place': (1, 1), u'generale': (1, 1), u'male': (1, 1),
                u'capito': (1, 1), u'loop': (1, 1), u'concetto': (1, 1)}, 
[(u'stringa', 8), (u'replace', 5), (u'lista', 3), (u'bisogna', 2), (u'faccio', 2), (u'lst', 2),
 (u'nuova', 2), (u'signola', 2)]))
    return 3.0


def test_program02_2():
    import program02
    ret = program02.post('file02_02_in.txt', 3,2)
    check(ret, ({u'ciao': (5, 5), u'return': (4, 4), u'codice': (4, 4), u'spazio': (6, 7),
                 u'funzione': (3, 4), u'space': (5, 7), u'print': (6, 8), u'solo': (4, 4),
                 u'len': (2, 4), u'k': (8, 15), u'variabile': (4, 5), u'grazie': (6, 6),
                 u'def': (4, 4), u'numero': (3, 4), u'newstr': (1, 5), u'stringa': (5, 10)}, 
[(u'k', 15), (u'stringa', 10), (u'print', 8), (u'space', 7), (u'spazio', 7), (u'grazie', 6), (u'ciao', 5),
 (u'newstr', 5), (u'variabile', 5), (u'codice', 4), (u'def', 4), (u'funzione', 4), (u'len', 4),
 (u'numero', 4), (u'return', 4), (u'solo', 4), (u'ciclo', 3), (u'faccio', 3), (u'lettera', 3),
 (u'spazi', 3), (u'valore', 3)]))
    return 3.0


def test_program02_3():
    import program02
    ret = program02.post('file02_03_in.txt', 10,12)
    check(ret, ({u'canopy': (10, 13), u'grade': (11, 13), u'py': (9, 11)}, 
[(u'canopy', 13), (u'grade', 13)]))
    return 3.0


def test_program02_4():
    import program02
    ret = program02.post('file02_04_in.txt', 10,12)
    check(ret, ({u'program': (5, 13), u'funzione': (7, 11), u'lst': (12, 22), u'grade': (16, 25),
                 u'lista': (15, 21), u'test': (6, 15)}, 
[(u'grade', 25), (u'lst', 22), (u'lista', 21), (u'test', 15), (u'program', 13)]))
    return 3.0
    
def test_program02_5():
    import program02
    ret = program02.post('file02_05_in.txt', 12,14)
    check(ret, ({u'canopy': (10, 13), u'grade': (11, 13)}, 
[]))
    return 3.0



tests = [test_program02_1, test_program02_2, test_program02_3, test_program02_4, test_program02_5]

if __name__ == '__main__':
    runtests(tests,logfile='grade02.csv')

