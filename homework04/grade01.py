#! /usr/bin/env python3 -B

from testlib import check, run, runtests

def check_node(fn, u):
    assert isinstance(u, str), "Grafo {}: un nodo non e' di tipo str ".format(repr(fn))
def check_adj(fn, u, adj):
    assert isinstance(adj, list), "Grafo {}: il valore ritornato da adjacents({}) non e' di tipo list".format(repr(fn),repr(u))
    return adj
def check_info(fn, u, info):
    assert isinstance(info, set), "Grafo {}: il valore ritornato da nodeInfo({}) non e' di tipo set".format(repr(fn),repr(u))
    return info
def check_graph(fn, g):
    try:
        nodes = g.nodes()
        assert isinstance(nodes, list), "Grafo {}: il valore ritornato da nodes() non e' di tipo list".format(repr(fn))
        assert len(nodes) > 0, "Grafo {}: il grafo e' vuoto".format(repr(fn))
        u = nodes[0]
        check_node(fn, u)
        check_adj(fn, u, g.adjacents(u))
        check_info(fn, u, g.nodeInfo(u))
    except:
        assert False, "Il grafo {} non e' di tipo Graph".format(repr(fn))
def edges(fn, g):
    ne = 0
    for u in g.nodes():
        check_node(fn, u)
        ne += len(check_adj(fn, u, g.adjacents(u)))
    return ne/2
def check_ne(fn, g, n, e):
    nn = len(g.nodes())
    assert n == nn, "Grafo {}: numero nodi errato, {} invece di {}".format(repr(fn), nn, n)
    ne = edges(fn, g)
    assert e == ne, "Grafo {}: numero archi errato, {} invece di {}".format(repr(fn), ne, e)
def check_adjs(fn, g, u, info, adj):
    i = g.nodeInfo(u)
    assert info == i, "Grafo {}: info del nodo {} errato,\n  {} invece di\n  {}".format(repr(fn),repr(u), repr(i), repr(info))
    a = g.adjacents(u)
    assert adj == (set(a) if isinstance(a, list) else a), "Grafo {}: adiacenti del nodo {} errati,\n  {} invece di\n  {}".format(repr(fn),repr(u),repr(a),repr(adj))

def test(fname, k, n, e,  adjs):
    import program01
    g = program01.actor_graph(fname,k)
    check_graph(fname, g)
    check_ne(fname, g, n, e)
    for u in adjs:
        check_adjs(fname, g, u, adjs[u][0], adjs[u][1])


    
    
def test_program01_0():
    test('file01_01_in.json', 2, 9, 17,  {
        'Michael Caine':(set([u'The Prestige', u'The Dark Knight Rises', u'Inception']),
                         set([u'Marion Cotillard', u'Tom Hardy', u'Ken Watanabe', u'Joseph Gordon-Levitt', u'Christian Bale'])
                         ),
        'Tom Hardy': (set([u'Inception', u'The Dark Knight Rises']),
                      set([u'Marion Cotillard', u'Michael Caine', u'Ken Watanabe', u'Joseph Gordon-Levitt',u'Christian Bale'])
                      ),
        'Kevin Spacey': (set([u'The Negotiator', u'L.A. Confidential']),
                         set([u'Samuel L. Jackson', u'Ron Rifkin'])
                         ),
        'Ron Rifkin': (set([u'The Negotiator', u'L.A. Confidential']),
                       set([u'Kevin Spacey', u'Samuel L. Jackson'])
                       ),
        'Marion Cotillard': (set([u'Inception', u'The Dark Knight Rises']),
                             set([u'Michael Caine', u'Tom Hardy', u'Ken Watanabe', u'Joseph Gordon-Levitt', u'Christian Bale'])
                         )})
    return 2

def test_program01_1():
    test('file01_02_in.json',3, 17, 9,  {
        'Sean Connery': (set([u'The Rock', u'The Hunt for Red October', u'Goldfinger']),
                         set([u'Michael Biehn', u'Stellan Skarsg\xe5rd'])
                         ),
        'Joe Pesci': (set([u'Once Upon a Time in America', u'Casino', u'Home Alone']),
                      set([u'Robert De Niro'])
                      ),
        'Robert De Niro': (set([u'Ronin', u'Casino', u'Once Upon a Time in America']),
                           set([u'Stellan Skarsg\xe5rd', u'Joe Pesci'])
                           ),
        'Kevin Spacey': (set([u'The Negotiator', u'L.A. Confidential', u'Moon']),
                         set([])
                         ),
        'Brian Cox': (set([u'Braveheart', u'Rise of the Planet of the Apes', u'The Bourne Supremacy']),
                      set([])
                        )})
    return 3

def test_program01_2():
    test('file01_00_in.json', 3, 129, 568,  {
        'Diedrich Bader':({'Bolt', 'Ice Age', 'Office Space'},
                         set(['Jack Black', 'Stephen Root', 'Jennifer Aniston', 'John C. McGinley', 'Ajay Naidu'])
                         ),
        'Martin Sheen':({'Apocalypse Now', 'The Departed', 'Gandhi'},
                         set(['Matt Damon', 'Ben Kingsley', 'Leonardo DiCaprio', 'Harrison Ford', 'Jack Nicholson', 'Geraldine James', 'Kevin Corrigan'])
                         ),
		'Rodger Bumpass':({'Sen to Chihiro no kamikakushi', 'The Iron Giant', 'Tarzan'},
                         set(['Wayne Knight', 'John Ratzenberger', 'Minnie Driver', 'Jack Angel', 'Bob Bergen', 'Jennifer Aniston'])
                         ),                         
                                        
        				})
    return 3

def test_program01_3():
    test('file01_03_in.json', 2, 280, 1288, {
        'Robert De Niro' :(set([u'The Deer Hunter', u'Sleepers', u'Stardust', u'Meet the Parents']),
                           set([u'Brad Renfro', u'James Rebhorn', u'Billy Crudup', u'Brad Pitt', u'Meryl Streep', u'Terry Kinney', u'Owen Wilson', u'Ben Stiller', u'John Cazale',
                                u'Kevin Bacon', u'Bruno Kirby', u'Christopher Walken', u'Dustin Hoffman', u'Thomas McCarthy', u'Ron Eldard'])
                           )})
    return 3

def test_program01_4():
    test('file01_04_in.json', 3, 194, 1009, {
        'Robert De Niro' :(set([u'Brazil', u'Once Upon a Time in America', u'Jackie Brown', u'Heat', u'Stardust', u'Taxi Driver', u'The Untouchables', u'Goodfellas']),
                           set([u'Al Pacino', u'Natalie Portman', u'Michael Keaton', u'Albert Brooks', u'Samuel L. Jackson', u'Michael Palin', u'Sean Connery',
                                u'Katherine Helmond', u'Jodie Foster', u'Joe Pesci', u'Kevin Costner', u'Ian Holm', u'Patricia Clarkson', u'Ted Levine', u'Ray Liotta'])
            )})
    return 4
  
tests = [test_program01_0, test_program01_1, test_program01_2, test_program01_3, test_program01_4]

if __name__ == '__main__':
    runtests(tests,logfile='grade01.csv')