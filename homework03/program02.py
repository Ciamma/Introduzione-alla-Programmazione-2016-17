'''Partendo da una parola e da una stringa di caratteri e' possibile, a volte, formarne altre sostituendo 
una lettera della parola con un'altra lettera lessicograficamente superiore presa all'interno della stringa di caratteri.
Ad esempio, partendo dalla parola "case" e dalla stringa di caratteri "ro" possiamo mutare  la
"a" con la "o"  ottenendo "cose", o anche  la "e" con la "o" ottenendo "caso", mutando poi la "c" con la "r" nella parola
"caso" otteniamo  "raso" e da questa mutando la "a" con la "o" otteniamo "roso". Possiamo dunque considerare tutte
le parole che si ottengono sostituendo una lettera della parola con una lettera
lessicograficamente successiva presente nella stringa di caratteri,  ripetere la
stessa operazione a partire da quest'ultime e cosi' via ottenendo un albero di
parole.

Ad esempio, ecco l'albero che si ottiene utilizzando la stringa di caratteri "ro", partendo dalla parola "case"
e considerando  solo parole presenti nel file file02_01_in.txt:

case
  cose
    rose
      roso
    coso
      roso
  caso
    raso
      roso
    coso
      roso
  rase
    rose
      roso
    raso
      roso
  

Definire una classe TNode che rappresenta un nodo di un albero di parole. La
classe deve implementare i metodi di seguito specificati. Per albero si intende
l'albero che ha per radice l'oggetto su cui e' invocato il metodo.

- Costruttore, con argomento w, crea un nodo relativo alla parola w,
  inizialmente senza figli.

- degree() ritorna un insieme (tipo set) di tuple definito come segue: per ogni nodo n dell'albero avente 
  parola w, l'insieme deve contenere la tupla (w, k), dove k e' il numero di figli di n.

- count(i) ritorna il numero di nodi a distanza i dalla radice.

- height(i) ritorna l'insieme (tipo set) dei nodi a distanza i dalla radice. 

- leaves() ritorna un insieme (tipo set) di tuple definito come segue: per ogni distinta 
  parola w contenuta in una foglia dell'albero, l'insieme deve contenere la tupla (w, k), 
  dove k e' il numero di foglie contenenti w.

- path(w1, w2) ritorna un insieme (tipo set)  che contiene tutte le tuple di
  parole che corrispondono a cammini  nell'albero che iniziano con un nodo con la
  parola w1 e terminano con un nodo con la parola w2.

Scrivere infine la funzione gen_wtree(wfile, word, caratteri) che prende in input il
percorso di un file wfile, una parola word e una stringa di caratteri e genera l'albero  con radice la
parola word e ritorna il nodo radice (di tipo TNode). Il file wfile contiene
le parole lecite, cioe', l'albero generato contiene solamente parole presenti
nel file wfile. Inoltre, come si vede anche dall'esempio di "case", nessun nodo
dell'albero deve avere due figli con la stessa parola. E' garantito che il file
contiene solamente caratteri ascii e che ogni linea contiene solamente una
parola con caratteri alfabetici minuscoli. Lo stesso vale per gli argomenti della funzione word e caratteri.

Ecco alcuni esempi:

tree = gen_wtree('file02_01_in.txt', 'case', 'rso')

tree.degree() ritorna set([('rase', 2), ('raso', 1), ('coso', 1), ('roso', 0), ('cose', 2), ('case', 3), ('caso', 2), ('rose', 1)])

tree.count(0)  ritorna 1
tree.count(2)  ritorna 5
tree.count(4)  ritorna 0


tree.height(1)  ritorna  set(['cose', 'rase', 'caso'])
tree.height(2)  ritorna  set(['coso', 'rose', 'raso'])
tree.height(3)  ritorna  set(['roso'])
tree.height(4)  ritorna  set([])

tree.leaves()  ritorna set([('roso', 6)])

tree.path('rase', 'roso')  ritorna set([('rase', 'rose', 'roso'), ('rase', 'raso', 'roso')])
tree.path('cose', 'raso')  ritorna  set([])
tree.path('case', 'roso')  ritorna set([('case', 'caso', 'coso', 'roso'), ('case', 'rase', 'rose', 'roso'), ('case', 'cose', 'rose', 'roso'),
                                        ('case', 'rase', 'raso', 'roso'), ('case', 'cose', 'coso', 'roso'), ('case', 'caso', 'raso', 'roso')])


Ovviamente, si possono aggiungere altri metodi alla classe e si possono
definire altre funzioni.

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard o che non sono forniti
nella cartella dell'homework. Se questo file e' piu' grande di 100KB o il grader 
non termina entro 5 minuti, il punteggio dell'esercizio e' zero.  
'''



def lettura_file(g):
    with open(g) as f:
        testo = f.read()
    text = testo.splitlines()
    text = set(text)
    return text

class TNode(object):

    def __init__(self, w):
        self._w = w
        self._children = []

    def add_children(self, node):
        self._children.append(node)

    def get_children(self):
        return self._children

    def get_number_child(self):
        return len(self._children)

    def degreeRic(self,li):
        li.append((str(self._w), len(self._children)))
        for child in self._children:
            child.degreeRic(li)

    def degree(self):
        l = []
        l.append((repr(self), self.get_number_child()))
        for child in self._children:
            child.degreeRic(l)
        return set(l)

    def countRic(self,i, level):
        c = 0
        if level == i-1:
            c += self.get_number_child()
        else:
            for child in self.get_children():
                c += child.countRic(i, level +1)
        return c

    def count(self, i):
        count = 0
        level = 0
        if level == i:
            count += 1
        elif level == i-1:
            count += self.get_number_child()
        else:
            for child in self.get_children():
                count += child.countRic(i, level +1)
        return count

    def heightRic(self, i,level,lis):
        if level == i-1:
            for child in self.get_children():
                lis.append(repr(child))
        else:
            for child in self.get_children():
                child.heightRic(i,level+1,lis)
        return lis

    def height(self, i):
        f = []
        level = 0
        if level == i:
            f.append(repr(self))
        elif level == i-1:
            for child in self.get_children():
                f.append(repr(child))
        else:
            for child in self.get_children():
                child.heightRic(i,level+1,f)
        return set(f)

    def leavesRic(self):
        lista = []
        if self.get_number_child() == 0 :
            lista.append(repr(self))
        for child in self.get_children():
                lista += (child.leavesRic())
        return lista

    def leaves(self):
        g = []
        lit = self.leavesRic()
        for e in lit:
            s = (e, lit.count(e))
            if s not in g:
                g.append(s)
        return set(g)

    def pathRic(self, w):
        l = []
        if repr(self) == w:
            l.append((w,))
        for child in self.get_children():
            for p in child.pathRic(w):
                l.append((repr(self),)+p)
        return set(l)

    def path(self, w1, w2):
        cammini = self.pathRic(w2)
        g = []
        h = []
        for c in cammini:
            if w1 in c:
                g.append(c[c.index(w1):])
        return set(g)

    def __str__(self):
        return 'TNode("'+self._w+'")'
    def __repr__(self):
        return self._w

def permutation(testo,wo,c,lw):
    lista = []
    for f in c:
        for n in range(len(wo)):
            if f<=wo[n]: continue
            if n == 0:
                parola = f + wo[1:]
                if parola in testo and parola != wo and parola not in lw :
                    lista.append(parola)
            elif 1 <= n <= len(wo)-2:
                parola = wo[0:n] + f + wo[n+1:]
                if parola in testo and parola != wo and parola and parola not in lw :
                    lista.append(parola)
            else:
                parola = wo[:n] + f
                if parola in testo and parola != wo and parola and parola not in lw :
                    lista.append(parola)
    return lista

def gen_tree_ricorsivo(testo,word,c,lw,prof = 0):
    root = TNode(word)
    lw.append(word)
    children = permutation(testo,word,c,lw)
    for child in children:
        nodo = gen_tree_ricorsivo(testo, child,c,lw, prof+1)
        root.add_children(nodo)
    for child in children:
        if child in lw:
            lw.remove(child)
    return root

def gen_wtree(wfile, word,carattere):
    testo = lettura_file(wfile)
    lw = []
    return gen_tree_ricorsivo(testo, word,carattere,lw)