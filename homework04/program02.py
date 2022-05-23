'''
Abbiamo un puzzle meccanico formato da 9 tessere, numerate da 1 a 9, incasellate in un quadrato 3x3.
La  configurazione standard e' la seguente:

-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------

La meccanica del puzzle permette di fare due soli tipi di mosse:
1)  rotazione di una posizione a destra o a sinistra di una delle tre righe.
    Ad esempio, se alla configurazione standard applichiamo la rotazione  a destra della seconda riga otteniamo:

    -------------
    | 1 | 2 | 3 |
    -------------
    | 6 | 4 | 5 |
    -------------
    | 7 | 8 | 9 |
    -------------
    
2)  rotazione di una posizione in alto o in basso di una delle tre colonne.
    Ad esempio, se alla configurazione standard applichiamo la rotazione in basso della prima colonna otteniamo:

    -------------
    | 7 | 2 | 3 |
    -------------
    | 1 | 5 | 6 |
    -------------
    | 4 | 8 | 9 |
    -------------


Sia i il  numero  1,2 o 3. Indichiamo le 12 possibili mosse con i seguenti caratteri:
'Ri': la riga i viene  ruotata a destra;
'Li': la riga i viene ruotata a sinistra
'Ui': la colonna i viene ruotata in alto
'Di': la colonna i viene ruotata in basso

Ad esempio, se alla configurazione iniziale applichiamo la sequenza di mosse: 'R3','U1','L1','L1' otteniamo 
la configurazione

-------------
| 3 | 4 | 2 |
-------------
| 9 | 5 | 6 |
-------------
| 1 | 7 | 8 |
-------------


Vogliamo scrivere un programma che data una configurazione trova una sequenza di
mosse ottimale (cioe' di lunghezza minima) che la riporta nella configurazione
standard. Rappresentiamo ogni configurazione con una tupla di 9 interi che
riporta i contenuti delle caselle per righe. Ad esempio, la configurazione sopra
e' rappresentata con (3,4,2,9,5,6,1,7,8) e la configurazione standard con
(1,2,3,4,5,6,7,8,9). Per risolvere il problema possiamo considerare un grafo i
cui nodi sono tutte le possibili configurazioni (che sono 9!) e tra due nodi
c'e' un arco se e' possibile passare dall'uno all'altro tramite una mossa (si
osservi che le mosse sono simmetriche, cioe' invertibili). Per determinare una
sequenza ottimale per una configurazione basta quindi trovare un cammino di
lunghezza minima in tale grafo che collega la configurazione data a quella
standard.
Scrivere due funzioni. La prima, puzzle_tree(), deve ritornare l'albero di visita della BFS
effettuata sul grafo descritto in precedenza, a partire dalla configurazione standard:
come descritto a lezione, tale albero dev'essere rappresentato con un dizionario che ad
ogni nodo assegna il nodo genitore nella visita BFS.
La seconda funzione, puzzle_sol(tree, cnf), preso in input un albero tree come
quello descritto sopra e una configurazione cnf, deve ritornare una lista che
contiene la sequenza di mosse che corrisponde al cammino in tree che va dalla
configurazione cnf alla radice. Se cnf non appartiene a tree, la funzione deve
ritornare None. La funzione non deve fare controlli su tree; pertanto  si assume che
l'argomento tree sia un dizionario rappresentante un albero come sopra detto. Ad esempio,
puzzle_sol(tree, (3,5,2,4,8,6,7,1,9)) deve ritornare ['D2', 'L1']. La sequenza di
mosse ottimale potrebbe non essere unica, ad esempio,
puzzle_sol(tree, (3,1,2,4,5,6,8,9,7)) potrebbe ritornare la lista
['L1','R3'] oppure ['R3','L1']. E' sufficiente che la sequenza sia ottimale, non
importa quale tra quelle ottimali e' ritornata, stesso discorso per l'albero
ritornato da puzzle_tree().

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard o non sono forniti
nella cartella dell'homework o non sono esplicitamente autorizzati.
ATTENZIONE: Se questo file e' piu' grande di 100KB o il grader non termina entro 5 minuti,
il punteggio dell'esercizio e' zero.  
'''




class _GraphNode:
    def __init__(self, name, adj, info):
        self.name = name
        self.adj = set(adj)
        self.info = info

class Graph:
    def __init__(self):
        self._nodes = {}
    def addNode(self, name, info=None):
        if name  in self._nodes: return
        self._nodes[name] = _GraphNode(name, set(), info)
    def addEdge(self, name1, name2):
        if not (name1 in self._nodes and name2 in self._nodes): return
        self._nodes[name1].adj.add(name2)
        self._nodes[name2].adj.add(name1)
    def adjacents(self, name):
        if name in self._nodes:
            return list(self._nodes[name].adj)
        return None
    def nodes(self):
        return list(self._nodes.keys())
    def edges(self):
        edges = set()
        for name, node in self._nodes.items():
            for adj in node.adj:
                if (adj, name) in edges: continue
                edges.add((name,adj))
        return list(edges)
    def nodeInfo(self, name):
        if name in self._nodes: return self._nodes[name].info
        return None

def mosse(elemento):
    diz = {}
    lista = list(elemento)
    r1 = (elemento[2], elemento[0], elemento[1],) + elemento[3:]
    r2 = elemento[:3] + (elemento[5], elemento[3], elemento[4],) + elemento[6:]
    r3 = elemento[:6] + (elemento[8], elemento[6], elemento[7])
    diz['R1'],diz['R2'],diz['R3'] = r1,r2,r3
    l1 = (elemento[1], elemento[2], elemento[0],) + elemento[3:]
    l2 = elemento[:3] + (elemento[4], elemento[5], elemento[3],) + elemento[6:]
    l3 = elemento[:6] + (elemento[7], elemento[8], elemento[6])
    diz['L1'],diz['L2'],diz['L3'] = l1,l2,l3
    u1= (elemento[3],) + elemento[1:3] + (elemento[6],) + elemento[4:6] + (elemento[0],) + elemento[7:9]
    u2= (elemento[0], elemento[4], elemento[2], elemento[3], elemento[7], elemento[5],elemento[6],elemento[1],elemento[8])
    u3= elemento[:2] + (elemento[5],) + elemento[3:5] + (elemento[8],) + elemento[6:8] + (elemento[2],)
    diz['U1'],diz['U2'],diz['U3'] = u1,u2,u3
    d1= (elemento[6],) + elemento[1:3] + (elemento[0],) + elemento[4:6] + (elemento[3],) + elemento[7:9]
    d2= (elemento[0], elemento[7], elemento[2], elemento[3], elemento[1], elemento[5],elemento[6],elemento[4],elemento[8])
    d3= elemento[:2] + (elemento[8],) + elemento[3:5] + (elemento[2],) + elemento[6:8] + (elemento[5],)
    diz['D1'],diz['D2'],diz['D3'] = d1,d2,d3
    return diz

def puzzle_tree():
    grafo= Graph()
    grafo.addNode((1,2,3,4,5,6,7,8,9))
    visited = set([(1,2,3,4,5,6,7,8,9)])
    active = set([(1,2,3,4,5,6,7,8,9)])
    dizionario={}
    dizionario[(1,2,3,4,5,6,7,8,9)]=None
    moves=1
    while active:
        newactive = set()
        lista=[]
        while active:
            u = active.pop()
            for m,v in (mosse(u)).items():
                if v not in visited:
                    visited.add(v)
                    grafo.addNode(v)
                    newactive.add(v)
                    dizionario[v]=u
                grafo.addEdge(u,v)
        active = newactive
    return dizionario

def visit_path(tree, name):
    root = None
    for u, gen in tree.items():
        if gen == None:
            root = u
            break
    if name in tree:
        path = [name]
        while name!= root:
            name = tree[name]
            path.insert(0,name)
        return path

def puzzle_sol(tree,cnf):
    if cnf not in tree:
        return None
    l = visit_path (tree,cnf)
    l = l[::-1]
    p = []
    for i in range(len(l)-1):
        for m,t in (mosse(l[i])).items():
            if t == l[i+1]:
                p.append(m)
    return p