#! /usr/bin/env python3 -B

from testlib import check, runtests


def checktree(tree, size, root,  sample):
    assert isinstance(tree, dict), "Tree errato: deve essere di tipo dict"
    assert len(tree) == size, "Tree errato: il numero chiavi deve essere {} invece e' {}".format(size, len(tree))
    r = None
    for k, v in tree.items():
        assert isinstance(k, tuple), "Tree errato: una chiave non e' di tipo tuple"
        assert len(k) == 9, "Tree errato: la lunghezza di una chiave deve essere {} invece e' {}".format(9, len(k))
        if v == None:
            assert r == None, "Tree errato: ci sono almeno due radici"
            assert k == root, "Tree errato: la radice deve essere {} invece e' {}".format(root, k)
            r = k
        else:
            assert isinstance(v, tuple), "Tree errato: il valore associato a {} non e' di tipo tuple".format(k)
            assert len(v) == 9, "Tree errato: la lunghezza di un valore deve essere {} invece e' {}".format(9, len(v))
            assert v in tree, "Tree errato: tutti valori devono essere anche chiavi"
    for d, nodes in sample.items():
        for u in nodes:
            assert u in tree, "configurazione {} non e' presente".format(u)
            dd = 0
            v = u
            while tree[v] != None:
                v = tree[v]
                dd += 1
                assert dd <= d, "Tree errato: configurazione {} deve essere a distanza {} invece e' a distanza maggiore".format(u, d)
            assert dd == d, "la distanza di configurazione {} e' errata".format(u)



def checksol(cnf, n, sol):
    assert isinstance(sol, list), " La soluzione prodotta per la configurazione {} deve essere di tipo list".format(repr(cnf))
    a=['R1','R2','R3','L1','L2','L3','U1','U2','U3','D1','D2','D3']
    a=set(a)
    b=set(sol)
    assert b.issubset(a), " La soluzione {} prodotta per la configurazione {} e' errata. La mosse devono essere in {}".format(repr(sol),repr(cnf),repr(a))
    con=list(cnf)
    for m in sol:
        if m=='R1':c=con[2];con[2]=con[1];con[1]=con[0];con[0]=c
        elif m=='R2':c=con[5];con[5]=con[4];con[4]=con[3];con[3]=c
        elif m=='R3':c=con[8];con[8]=con[7];con[7]=con[6];con[6]=c
        elif m=='L1':c=con[0];con[0]=con[1];con[1]=con[2];con[2]=c
        elif m=='L2':c=con[3];con[3]=con[4];con[4]=con[5];con[5]=c
        elif m=='L3':c=con[6];con[6]=con[7];con[7]=con[8];con[8]=c
        elif m=='U1':c=con[0];con[0]=con[3];con[3]=con[6];con[6]=c
        elif m=='U2':c=con[1];con[1]=con[4];con[4]=con[7];con[7]=c
        elif m=='U3':c=con[2];con[2]=con[5];con[5]=con[8];con[8]=c
        elif m=='D1':c=con[6];con[6]=con[3];con[3]=con[0];con[0]=c
        elif m=='D2':c=con[7];con[7]=con[4];con[4]=con[1];con[1]=c
        elif m=='D3':c=con[8];con[8]=con[5];con[5]=con[2];con[2]=c
    assert con==[1,2,3,4,5,6,7,8,9], " La soluzione {} prodotta per la configurazione {} e' errata: non ritorna alla configurazione iniziale ma a {}".format(repr(sol),repr(cnf), repr(con))
    assert len(sol) == n, " La soluzione {} prodotta per la configurazione {} e' errata. La mosse devono essere {} invece sono {}".format(repr(sol),repr(cnf),n, len(sol))
           

TREE = None

SAMPLETREE = {0: [(1, 2, 3, 4, 5, 6, 7, 8, 9)],
 1: [(7, 2, 3, 1, 5, 6, 4, 8, 9), (2, 3, 1, 4, 5, 6, 7, 8, 9), (1, 2, 3, 4, 5, 6, 9, 7, 8), (1, 2, 6, 4, 5, 9, 7, 8, 3), (1, 8, 3, 4, 2, 6, 7, 5, 9), (1, 2, 9, 4, 5, 3, 7, 8, 6), (1, 2, 3, 5, 6, 4, 7, 8, 9), (1, 2, 3, 6, 4, 5, 7, 8, 9), (4, 2, 3, 7, 5, 6, 1, 8, 9), (1, 2, 3, 4, 5, 6, 8, 9, 7)],
 2: [(6, 1, 2, 4, 5, 9, 7, 8, 3), (1, 5, 3, 8, 6, 4, 7, 2, 9), (5, 2, 3, 7, 6, 4, 1, 8, 9), (4, 2, 3, 9, 5, 6, 1, 7, 8), (1, 2, 9, 3, 4, 5, 7, 8, 6), (1, 2, 8, 4, 5, 3, 9, 7, 6), (1, 5, 3, 6, 4, 8, 7, 2, 9), (4, 5, 3, 7, 8, 6, 1, 2, 9), (3, 1, 9, 4, 5, 2, 7, 8, 6), (7, 1, 2, 3, 5, 6, 4, 8, 9)],
 3: [(2, 3, 1, 6, 4, 5, 8, 9, 7), (9, 7, 3, 1, 2, 6, 4, 5, 8), (3, 1, 8, 2, 6, 4, 7, 5, 9), (7, 2, 9, 6, 1, 3, 4, 8, 5), (8, 3, 9, 4, 2, 1, 7, 5, 6), (9, 2, 3, 5, 6, 1, 4, 7, 8), (5, 2, 3, 8, 6, 4, 1, 9, 7), (8, 2, 3, 1, 6, 4, 5, 9, 7), (2, 3, 6, 7, 4, 5, 1, 8, 9), (7, 9, 1, 2, 5, 3, 4, 8, 6)],
 4: [(7, 6, 2, 1, 4, 5, 3, 8, 9), (4, 2, 8, 3, 5, 6, 1, 7, 9), (7, 3, 1, 4, 5, 2, 8, 9, 6), (1, 7, 2, 4, 5, 9, 6, 8, 3), (2, 5, 1, 6, 4, 9, 3, 7, 8), (4, 1, 3, 7, 5, 2, 8, 9, 6), (7, 3, 1, 6, 4, 2, 9, 5, 8), (8, 3, 5, 6, 2, 9, 7, 4, 1), (4, 2, 6, 5, 7, 8, 1, 9, 3), (6, 3, 7, 1, 5, 9, 4, 8, 2)],
 5: [(9, 2, 5, 1, 4, 8, 7, 3, 6), (4, 9, 2, 1, 5, 3, 7, 8, 6), (8, 5, 2, 4, 9, 6, 7, 1, 3), (5, 8, 6, 7, 2, 4, 3, 1, 9), (7, 5, 3, 6, 4, 1, 9, 8, 2), (2, 8, 6, 1, 5, 9, 4, 7, 3), (9, 5, 3, 8, 6, 7, 1, 4, 2), (7, 9, 5, 4, 1, 3, 2, 8, 6), (7, 1, 3, 6, 5, 2, 8, 9, 4), (3, 9, 7, 5, 1, 2, 8, 6, 4)],
 6: [(2, 8, 9, 1, 6, 5, 7, 3, 4), (1, 7, 2, 5, 3, 9, 6, 8, 4), (1, 6, 8, 3, 5, 4, 9, 7, 2), (9, 2, 4, 7, 6, 5, 8, 1, 3), (3, 1, 2, 9, 8, 4, 5, 7, 6), (3, 2, 8, 5, 1, 6, 9, 7, 4), (5, 1, 2, 4, 7, 8, 6, 3, 9), (3, 5, 7, 1, 2, 6, 8, 9, 4), (8, 3, 4, 5, 6, 2, 9, 1, 7), (6, 7, 1, 4, 9, 3, 5, 2, 8)],
 7: [(4, 7, 8, 1, 6, 5, 3, 9, 2), (7, 8, 5, 1, 9, 4, 3, 6, 2), (5, 9, 7, 3, 1, 2, 8, 4, 6), (5, 9, 7, 6, 1, 4, 3, 8, 2), (4, 6, 8, 2, 5, 1, 7, 3, 9), (7, 6, 4, 9, 1, 2, 5, 3, 8), (2, 6, 4, 1, 3, 8, 7, 5, 9), (5, 4, 7, 2, 6, 8, 1, 3, 9), (3, 4, 8, 6, 5, 7, 2, 9, 1), (8, 5, 7, 9, 6, 1, 3, 2, 4)],
 8: [(9, 6, 4, 2, 3, 1, 7, 8, 5), (6, 4, 5, 1, 3, 2, 8, 9, 7), (8, 3, 1, 9, 7, 5, 2, 4, 6), (6, 2, 8, 3, 7, 1, 5, 4, 9), (8, 6, 7, 3, 4, 5, 9, 2, 1), (4, 9, 8, 6, 1, 7, 5, 3, 2), (3, 9, 5, 2, 7, 8, 1, 6, 4), (5, 1, 6, 8, 7, 9, 2, 4, 3), (6, 9, 7, 8, 5, 2, 3, 1, 4), (8, 4, 3, 9, 7, 2, 5, 6, 1)]}

SAMPLESOL = {0: [(1, 2, 3, 4, 5, 6, 7, 8, 9)],
 1: [ (1, 2, 9, 4, 5, 3, 7, 8, 6), (1, 2, 3, 5, 6, 4, 7, 8, 9), (1, 2, 3, 6, 4, 5, 7, 8, 9), (4, 2, 3, 7, 5, 6, 1, 8, 9), (1, 2, 3, 4, 5, 6, 8, 9, 7)],
 2: [ (1, 2, 8, 4, 5, 3, 9, 7, 6), (1, 5, 3, 6, 4, 8, 7, 2, 9), (4, 5, 3, 7, 8, 6, 1, 2, 9), (3, 1, 9, 4, 5, 2, 7, 8, 6), (7, 1, 2, 3, 5, 6, 4, 8, 9)],
 3: [ (9, 2, 3, 5, 6, 1, 4, 7, 8), (5, 2, 3, 8, 6, 4, 1, 9, 7), (8, 2, 3, 1, 6, 4, 5, 9, 7), (2, 3, 6, 7, 4, 5, 1, 8, 9), (7, 9, 1, 2, 5, 3, 4, 8, 6)],
 4: [ (4, 1, 3, 7, 5, 2, 8, 9, 6), (7, 3, 1, 6, 4, 2, 9, 5, 8), (8, 3, 5, 6, 2, 9, 7, 4, 1), (4, 2, 6, 5, 7, 8, 1, 9, 3), (6, 3, 7, 1, 5, 9, 4, 8, 2)],
 5: [ (2, 8, 6, 1, 5, 9, 4, 7, 3), (9, 5, 3, 8, 6, 7, 1, 4, 2), (7, 9, 5, 4, 1, 3, 2, 8, 6), (7, 1, 3, 6, 5, 2, 8, 9, 4), (3, 9, 7, 5, 1, 2, 8, 6, 4)],
 6: [ (3, 2, 8, 5, 1, 6, 9, 7, 4), (5, 1, 2, 4, 7, 8, 6, 3, 9), (3, 5, 7, 1, 2, 6, 8, 9, 4), (8, 3, 4, 5, 6, 2, 9, 1, 7), (6, 7, 1, 4, 9, 3, 5, 2, 8)],
 7: [ (7, 6, 4, 9, 1, 2, 5, 3, 8), (2, 6, 4, 1, 3, 8, 7, 5, 9), (5, 4, 7, 2, 6, 8, 1, 3, 9), (3, 4, 8, 6, 5, 7, 2, 9, 1), (8, 5, 7, 9, 6, 1, 3, 2, 4)],
 8: [ (4, 9, 8, 6, 1, 7, 5, 3, 2), (3, 9, 5, 2, 7, 8, 1, 6, 4), (5, 1, 6, 8, 7, 9, 2, 4, 3), (6, 9, 7, 8, 5, 2, 3, 1, 4), (8, 4, 3, 9, 7, 2, 5, 6, 1)]}





def test_program02_0():
    global TREE
    import program02
    t = program02.puzzle_tree()
    checktree( t, 181440, (1, 2, 3, 4, 5, 6, 7, 8, 9),  SAMPLETREE)
    TREE = t
    return 7

def test_program02_1():
    import program02
    assert TREE != None, "Tree non valido"
    for d, confs in SAMPLESOL.items():
        for cnf in confs:
            sol = program02.puzzle_sol(TREE, cnf)
            checksol(cnf, d, sol)
    return 8

tests = [test_program02_0, test_program02_1]

if __name__ == '__main__':
    runtests(tests,logfile='grade02.csv')

