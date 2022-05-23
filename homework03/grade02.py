#! /usr/bin/env python3 -B

from testlib import check, runtests
import program02

WFILE = 'file02_01_in.txt'

err_degree = (lambda w, caratteri, pe, p: 'ERRORE: su parola {} e caratteri {} degree() restituisce \n {} != \n {}'.format(repr(w), repr(caratteri), repr(pe), repr(p)))
err_count = (lambda w, caratteri, i, ce, c: 'ERRORE: su parola {} e caratteri {} count({}) restituisce {}, mentre il valore deve essere {}'.format(repr(w),repr(caratteri),repr(i), repr(ce), repr(c)))
err_height = (lambda w,caratteri, i, he, h: 'ERRORE: su parola {} e caratteri {}  height({}) restituisce \n{} != \n {}'.format(repr(w),repr(caratteri), repr(i), repr(he), repr(h)))
err_leaves = (lambda w, caratteri, le, l: 'ERRORE: su parola {} e caratteri {}  leaves() restituisce \n {} != \n {}'.format(repr(w), repr(caratteri), repr(le), repr(l)))
err_path = (lambda w, caratteri, w1, w2, pe, p: 'ERRORE: su parola {} e caratteri {} path({}, {}) restituisce \n{}\n!=\n{}'.format(repr(w), repr(caratteri), repr(w1), repr(w2), repr(pe), repr(p)))

def test_degree(tests):
    for w, caratteri, p in tests:
        tree = program02.gen_wtree(WFILE, w, caratteri)
        pp = tree.degree()
        assert pp == p, err_degree(w, caratteri, pp, p)
def test_count(tests):
    for w, caratteri, i, c in tests:
        tree = program02.gen_wtree(WFILE, w,caratteri)
        cc = tree.count(i)
        assert cc == c, err_count(w, caratteri, i, cc, c)
def test_height(tests):
    for w, caratteri, i, h in tests:
        tree = program02.gen_wtree(WFILE, w,caratteri)
        hh = tree.height(i)
        assert hh == h, err_height(w, caratteri, i, hh, h)
def test_leaves(tests):
    for w, caratteri, l in tests:
        tree = program02.gen_wtree(WFILE, w,caratteri)
        ll = tree.leaves()
        assert ll == l, err_leaves(w, caratteri,  ll, l)

def test_path(tests):
    for w, caratteri, w1, w2, p in tests:
        tree = program02.gen_wtree(WFILE, w, caratteri)
        pp = tree.path(w1, w2)
        assert pp == p, err_path(w, caratteri, w1, w2, pp, p)


def test_program_0():
    test_degree([
        ('case', 'rso', set([('rase', 2), ('raso', 1), ('coso', 1), ('roso', 0), ('cose', 2), ('case', 3), ('caso', 2), ('rose', 1)])),
        ('mania', 'raot',set([('morir', 0), ('moria', 3), ('maria', 4), ('tatto', 0), ('mania', 2), ('tonto', 1), ('ratto', 2), ('rotta', 1), ('motto', 1), ('marra', 2),
                              ('motta', 2), ('mario', 0), ('morta', 3), ('tonta', 2), ('manta', 5), ('marta', 2), ('tanta', 2), ('matta', 3), ('monta', 4),
                              ('ratta', 2), ('manto', 3), ('morra', 2), ('monto', 3), ('torta', 1), ('torto', 0), ('morto', 2), ('rotto', 0), ('morro', 1),
                              ('tanto', 2), ('matto', 3)]))
        ])
    return 1

def test_program_1():
    test_count([
        ('case', 'rso',0,1),('case', 'rso',2,6),('case', 'rso',4,0), ('mania', 'raot',1,2),('mania', 'raot',4,50)
        ])
    return 1

def test_program_2():
    test_height([
        ('case', 'rso',1, set(['cose', 'rase', 'caso'])),('case', 'rso',2, set(['coso', 'rose', 'raso'])), ('case', 'rso',3, set(['roso'])),('case', 'rso',4, set([])),
        ('mania', 'raot',1, set(['manta', 'maria'])), ('mania', 'raot',2, set(['moria', 'monta', 'manto', 'mario', 'marra', 'matta', 'marta', 'tanta'])),
        ('mania', 'raot',3, set(['morra', 'monto', 'tonta', 'ratta', 'morir', 'motta', 'matta', 'tanto', 'marta', 'morta', 'matto'])),
        ('mania', 'raot',4,set(['ratto', 'morro', 'tatto', 'ratta', 'morto', 'matta', 'tonto', 'matto', 'motta', 'morta', 'torta', 'motto', 'rotta']))
        ])
    return 1

def test_program_3():
    test_leaves([
        ('case', 'rso',set([('roso', 6)])), ('mania', 'raot',set([('morir', 1), ('torto', 26), ('mario', 1), ('tatto', 16), ('rotto', 55)]))
        ])
    return 1

def test_program_4():
    test_path([
        ('case', 'rso', 'rase', 'roso',set([('rase', 'rose', 'roso'), ('rase', 'raso', 'roso')])),('case', 'rso', 'cose', 'raso',set([])),
        ('case', 'rso', 'case', 'roso',set([('case', 'caso', 'coso', 'roso'), ('case', 'rase', 'rose', 'roso'), ('case', 'cose', 'rose', 'roso'),
                                        ('case', 'rase', 'raso', 'roso'), ('case', 'cose', 'coso', 'roso'), ('case', 'caso', 'raso', 'roso')])),
        ('mania', 'raot', 'marta', 'rotta', set([('marta', 'matta', 'ratta', 'rotta'), ('marta', 'morta', 'motta', 'rotta'), ('marta', 'matta', 'motta', 'rotta')])),
        ('mania', 'raot', 'maria', 'tatto', set([('maria', 'marta', 'matta', 'matto', 'ratto', 'tatto'), ('maria', 'marra', 'marta', 'matta', 'matto', 'tatto'),
                                            ('maria', 'marta', 'matta', 'ratta', 'ratto', 'tatto'), ('maria', 'marra', 'marta', 'matta', 'matto', 'ratto', 'tatto'),
                                            ('maria', 'marta', 'matta', 'matto', 'tatto'), ('maria', 'marra', 'marta', 'matta', 'ratta', 'ratto', 'tatto')]))
       ])
    return 1

def test_program_5():
   test_degree([
        ('alba', 'bcdefgilopst', set([('atei', 2), ('ossa', 2), ('glia', 2), ('etti', 1), ('alba', 9), ('elle', 2), ('alce', 7), ('osti', 0), ('oslo', 1), ('olio', 0),
                                      ('alef', 0), ('alfa', 4), ('alga', 4), ('atto', 2), ('opti', 2), ('etto', 1), ('alto', 1), ('albo', 4), ('assi', 4), ('olla', 2),
                                      ('alpi', 1), ('aldo', 3), ('atti', 2), ('alee', 6), ('else', 1), ('issa', 2), ('alia', 5), ('ella', 3), ('alci', 2), ('alle', 6),
                                      ('olle', 0), ('asta', 3), ('algo', 2), ('opto', 1), ('asce', 4), ('oste', 1), ('esce', 3), ('olia', 2), ('ateo', 1), ('otto', 0),
                                      ('aloe', 2), ('opta', 2), ('atea', 4), ('alpe', 2), ('alea', 8), ('alti', 3), ('ossi', 2), ('essi', 2), ('atta', 3), ('glie', 0),
                                      ('alte', 4), ('alta', 5), ('atte', 2), ('esse', 2), ('esso', 2), ('osso', 0), ('asso', 3), ('asco', 3), ('isso', 1), ('albi', 4),
                                      ('asti', 2), ('atee', 3), ('esci', 2), ('aste', 3), ('allo', 1), ('elsa', 2), ('asia', 1), ('essa', 5), ('esco', 2), ('osco', 2),
                                      ('asse', 4), ('opla', 1), ('alla', 5), ('albe', 8)]))
      ])
   return 1

def test_program_6():
    test_count([('alba', 'bcdefgilopst',2,47), ('alba', 'bcdefgilopst',6,1698)])
    return 1

def test_program_7():
    test_height([
        ('alba', 'bcdefgilopst', 2, set(['albi', 'alpe', 'glia', 'alfa', 'atea', 'albo', 'alci', 'olla', 'ella', 'alce', 'alta', 'alef', 'alto', 'alle', 'alga', 'alla',
                                         'alti', 'aloe', 'allo', 'alia', 'alte', 'asia', 'aldo', 'algo', 'atta', 'asta', 'alee', 'alpi', 'olia']))
      ])
    return 2

def test_program_8():
    test_leaves([
         ('alba', 'bcdefgilopst',set([('osso', 548), ('alef', 4), ('olio', 16), ('olle', 106), ('osti', 797), ('glie', 8), ('otto', 5438)]))
        ])
    return 3


def test_program_9():
    test_path([
    ('alba', 'bcdefgilopst', 'alpe', 'osti',set([('alpe', 'alte', 'aste', 'asti', 'osti'), ('alpe', 'alte', 'aste', 'oste', 'osti'),
                                                 ('alpe', 'alte', 'alti', 'asti', 'osti'), ('alpe', 'alpi', 'alti', 'asti', 'osti')])),
    ('alba', 'bcdefgilopst', 'alba', 'alef', set([('alba', 'albe', 'alee', 'alef'), ('alba', 'alea', 'alef'), ('alba', 'alea', 'alee', 'alef'),
                                                  ('alba', 'albe', 'alce', 'alee', 'alef')])),
    ('alba', 'bcdefgilopst', 'albi', 'otto', set([('albi', 'alci', 'alti', 'atti', 'atto', 'otto'), ('albi', 'alti', 'asti', 'atti', 'atto', 'etto', 'otto'),
                                                 ('albi', 'albo', 'aldo', 'algo', 'alto', 'atto', 'otto'), ('albi', 'alti', 'asti', 'atti', 'atto', 'otto'),
                                                 ('albi', 'alpi', 'alti', 'alto', 'atto', 'etto', 'otto'), ('albi', 'alpi', 'alti', 'atti', 'atto', 'etto', 'otto'),
                                                 ('albi', 'alti', 'atti', 'atto', 'etto', 'otto'), ('albi', 'alci', 'alpi', 'alti', 'alto', 'atto', 'otto'),
                                                 ('albi', 'alci', 'alpi', 'alti', 'atti', 'atto', 'etto', 'otto'), ('albi', 'alpi', 'alti', 'asti', 'atti', 'atto', 'otto'),
                                                 ('albi', 'alpi', 'alti', 'atti', 'atto', 'otto'), ('albi', 'alci', 'alti', 'alto', 'atto', 'etto', 'otto'),
                                                 ('albi', 'alti', 'atti', 'atto', 'otto'), ('albi', 'albo', 'aldo', 'alto', 'atto', 'etto', 'otto'),
                                                 ('albi', 'alci', 'alti', 'atti', 'etti', 'etto', 'otto'),
                                                 ('albi', 'albo', 'aldo', 'algo', 'allo', 'alto', 'atto', 'etto', 'otto'),
                                                 ('albi', 'alpi', 'alti', 'atti', 'etti', 'etto', 'otto'), ('albi', 'alpi', 'alti', 'asti', 'atti', 'atto', 'etto', 'otto'),
                                                 ('albi', 'albo', 'allo', 'alto', 'atto', 'etto', 'otto'), ('albi', 'alci', 'alti', 'atti', 'atto', 'etto', 'otto'),
                                                 ('albi', 'alci', 'alpi', 'alti', 'asti', 'atti', 'atto', 'etto', 'otto'),
                                                 ('albi', 'alci', 'alti', 'asti', 'atti', 'atto', 'otto'), ('albi', 'albo', 'allo', 'alto', 'atto', 'otto'),
                                                 ('albi', 'alpi', 'alti', 'alto', 'atto', 'otto'), ('albi', 'alci', 'alpi', 'alti', 'alto', 'atto', 'etto', 'otto'),
                                                 ('albi', 'alti', 'alto', 'atto', 'otto'), ('albi', 'alci', 'alpi', 'alti', 'atti', 'atto', 'otto'),
                                                 ('albi', 'alpi', 'alti', 'asti', 'atti', 'etti', 'etto', 'otto'), ('albi', 'alti', 'alto', 'atto', 'etto', 'otto'),
                                                 ('albi', 'alci', 'alpi', 'alti', 'asti', 'atti', 'etti', 'etto', 'otto'), ('albi', 'albo', 'aldo', 'alto', 'atto', 'otto'),
                                                 ('albi', 'alci', 'alti', 'alto', 'atto', 'otto'), ('albi', 'albo', 'alto', 'atto', 'etto', 'otto'),
                                                 ('albi', 'alci', 'alti', 'asti', 'atti', 'etti', 'etto', 'otto'),
                                                 ('albi', 'albo', 'aldo', 'allo', 'alto', 'atto', 'etto', 'otto'), ('albi', 'albo', 'algo', 'alto', 'atto', 'otto'),
                                                 ('albi', 'alci', 'alpi', 'alti', 'atti', 'etti', 'etto', 'otto'),
                                                 ('albi', 'albo', 'aldo', 'algo', 'allo', 'alto', 'atto', 'otto'),
                                                 ('albi', 'albo', 'algo', 'allo', 'alto', 'atto', 'etto', 'otto'), ('albi', 'albo', 'aldo', 'allo', 'alto', 'atto', 'otto'),
                                                 ('albi', 'alti', 'asti', 'atti', 'etti', 'etto', 'otto'), ('albi', 'albo', 'aldo', 'algo', 'alto', 'atto', 'etto', 'otto'),
                                                 ('albi', 'albo', 'alto', 'atto', 'otto'), ('albi', 'alci', 'alpi', 'alti', 'asti', 'atti', 'atto', 'otto'),
                                                 ('albi', 'alci', 'alti', 'asti', 'atti', 'atto', 'etto', 'otto'), ('albi', 'albo', 'algo', 'alto', 'atto', 'etto', 'otto'),
                                                 ('albi', 'alti', 'atti', 'etti', 'etto', 'otto'), ('albi', 'albo', 'algo', 'allo', 'alto', 'atto', 'otto')]))
    ])
    return 3

#tests = [test_program_0]	
tests = [test_program_0,test_program_1,test_program_2,test_program_3,test_program_4, test_program_5, test_program_6, test_program_7, test_program_8, test_program_9]

if __name__ == '__main__':
    runtests(tests,logfile='grade02.csv')

