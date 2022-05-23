'''Abbiamo dei  file in formato json che contengono  liste di film in cui ogni film e' 
un dizionario.  Il dizionario  ha una chiave  'actors' il cui valore e' la lista dei nomi 
degli attori (nel seguito per 'nome' si intende nome, cognome ed eventualmente middle name) 
che hanno recitato nel film ed  una chiave 'title' con il titolo del film,  per il formato 
preciso vedere il file 'file01_01_in.json'.

Scrivere una funzione actor_graph(filename, k) che preso in input il nome di un
file json del tipo appena descritto  crea un grafo di tipo Graph (lo stesso tipo
visto a lezione e riportato sotto da cui abbiamo semplicemente eliminato il parametro colors 
per il grafo e il parametro pos per i nodi del grafo)
i cui nodi sono gli attori che hanno recitato in almeno k dei film elencati nel file e 
due attori sono connessi se c'e' almeno un film in cui hanno recitato insieme.
Ogni nodo ha il nome uguale al nome dell'attore e deve contenere nell'info
un set contenente tutti i film in cui l'attore ha recitato.

Ecco un esempio:

g = actor_graph('file01_01_in.json',2)

g.nodes() --> ['Christian Bale', 'Tom Hardy', 'Ken Watanabe', 'Marion Cotillard',
               'Joseph Gordon-Levitt', 'Michael Caine', 'Samuel L. Jackson', 
               'Ron Rifkin', 'Kevin Spacey']

g.edges() --> [('Tom Hardy', 'Michael Caine'), ('Tom Hardy', 'Ken Watanabe'), 
			   ('Christian Bale', 'Marion Cotillard'),('Ken Watanabe', 'Marion Cotillard'), 
			   ('Ken Watanabe', 'Michael Caine'), ('Marion Cotillard', 'Michael Caine'), 
			   ('Samuel L. Jackson', 'Ron Rifkin'), ('Samuel L. Jackson', 'Kevin Spacey'),
               ('Christian Bale', 'Michael Caine'), ('Ken Watanabe', 'Joseph Gordon-Levitt'), 
               ('Tom Hardy', 'Joseph Gordon-Levitt'),('Joseph Gordon-Levitt', 'Michael Caine'), 
               ('Christian Bale', 'Joseph Gordon-Levitt'),('Marion Cotillard', 'Joseph Gordon-Levitt'),
               ('Christian Bale', 'Tom Hardy'), ('Tom Hardy', 'Marion Cotillard'), 
               ('Ron Rifkin', 'Kevin Spacey')]


g.nodeInfo('Michael Caine') --> {'Inception', 'The Dark Knight Rises', 'The Prestige'}

set(g.adjacents('Michael Caine')) --> {'Christian Bale', 'Tom Hardy', 'Joseph Gordon-Levitt', 
									  'Marion Cotillard', 'Ken Watanabe'}

g.nodeInfo('Tom Hardy') --> {'Inception', 'The Dark Knight Rises'}

set(g.adjacents('Tom Hardy')) --> {'Christian Bale', 'Marion Cotillard', 
                                   'Michael Caine', 'Joseph Gordon-Levitt', 'Ken Watanabe'}

g.nodeInfo('Kevin Spacey') --> {'L.A. Confidential', 'The Negotiator'}

set(g.adjacents('Kevin Spacey')) --> {'Samuel L. Jackson', 'Ron Rifkin'}

g.nodeInfo('Ron Rifkin') --> {'L.A. Confidential', 'The Negotiator'}

set(g.adjacents('Ron Rifkin')) --> {'Samuel L. Jackson', 'Kevin Spacey'}

g.nodeInfo('Marion Cotillard') --> {'Inception', 'The Dark Knight Rises'}

set(g.adjacents('Marion Cotillard')) --> {'Christian Bale', 'Tom Hardy', 
                                          'Michael Caine', 'Joseph Gordon-Levitt', 'Ken Watanabe'} 
           
                              
AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard o non sono forniti
nella cartella dell'homework o non sono esplicitamente autorizzati.
ATTENZIONE: Se questo file e' piu' grande di 100KB o il grader non termina entro 5 minuti,
il punteggio dell'esercizio e' zero.  
'''

class _GraphNode:
    '''Rappresenta un nodo del grafo. Da usarsi solo all'interno di Graph.'''
    def __init__(self, name, adj, info):
        self.name = name
        self.adj = set(adj)
        self.info = info

class Graph:
    '''Rappresenta un grafo'''
    def __init__(self):
        '''Inizializza un grafo vuoto.'''
        self._nodes = {}
    def addNode(self, name, info=None):
        '''Aggiunge un nodo name, se non esiste'''
        if name  in self._nodes: return
        self._nodes[name] = _GraphNode(name, set(), info)
    def addEdge(self, name1, name2):
        '''Aggiunge un arco che collega i nodi name1 e name2'''
        if not (name1 in self._nodes and name2 in self._nodes): return 
        self._nodes[name1].adj.add(name2)
        self._nodes[name2].adj.add(name1)
    def adjacents(self, name):
        '''Ritorna una lista dei nomi dei nodi adiacenti al nodo name,
        se il nodo non esiste, ritorna None'''
        if name in self._nodes:
            return list(self._nodes[name].adj)
        return None
    def nodes(self):
        '''Ritorna una lista dei nomi dei nodi del grafo'''
        return list(self._nodes.keys())
    def edges(self):
        '''Ritorna una lista degli archi  del grafo'''
        edges = set()
        for name, node in self._nodes.items():
            for adj in node.adj:
                if (adj, name) in edges: continue
                edges.add((name,adj))
        return list(edges)
    def nodeInfo(self, name):
        '''Ritorna l'info del nodo name, se il nodo non esiste, ritorna None'''
        if name in self._nodes: return self._nodes[name].info
        return None


import json

def actor_graph(filename,k):
    grafo = Graph()
    attori = set()
    with open(filename) as f:
        f = json.load(f)
    for e in f:
        for c,v in e.items():
            if type(v) == list:
                for i in v:
                    attori.add(i)
    for e in attori:
        count = 0
        l = set()
        for d in f:
            for c,v in d.items():
                if type(v) == list:
                    if e in v:
                        count += 1
                        l.add(d['title'])
        if count >= k:
            grafo.addNode(e,l)
    for node in grafo.nodes():
        for i in grafo.nodeInfo(node):
            for e in grafo.nodes():
                if i in grafo.nodeInfo(e) and node != e:
                    grafo.addEdge(node,e)
    return grafo