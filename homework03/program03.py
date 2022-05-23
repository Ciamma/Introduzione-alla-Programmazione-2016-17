'''Implementare la funzione statistiche(htmlfile, k1, k2) che preso in input 
il percorso htmlfile di un file in HTML, costruisce l'albero di parsing del file HTML htmlfile e 
 restituisce una tupla di 5  elementi:
 
 1) il primo elemento della tupla riporta il numero di nodi dell'albero di parsing aventi tag chiuso
 2) il secondo elemento della tupla riporta il numero di nodi dell'albero di parsing con tag che hanno almeno k1 attributi
 3) il terzo elemento della tupla riporta il numero di nodi dell'albero che hanno almeno k2 figli
 4) il quarto elemento della tupla rappresenta il numero massimo di figli per i nodi dell'albero
 5) il quinto elemento della tupla e' l'insieme dei tag che compaiono tra i nodi dell'albero.


Nel costruire l'albero di parsing utilizzare la classe MyHTMLParser vista a lezione.


AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard o che non sono forniti
nella cartella dell'homework; non modificare i moduli importati. Se questo file
e' piu' grande di 100KB o il grader non termina entro 5 minuti, il punteggio
dell'esercizio e' zero.
'''

from  html.parser import HTMLParser

class HTMLNode(object):
    def __init__(self, tag, attr, content, closed=True):
        self.tag = tag          # dizionario degli attributi
        self.attr = attr        # testo per nodi _text_ o lista dei figli
        self.content = content  # True se il nodo ha la chiusura
        self.closed = closed    # per distinguere i nodi testo


class MyHTMLParser(HTMLParser):
    def __init__(self):
        '''Crea un parser per la class HTMLNode'''
        # inizializza la class base super()
        super().__init__()
        self.root = None
        self.stack = []
    def handle_starttag(self, tag, attrs):
        '''Metodo invocato per tag aperti'''
        closed = tag not in ['img','br']
        node = HTMLNode(tag,dict(attrs),[],closed)
        if not self.root: self.root = node
        if self.stack: self.stack[-1].content.append(node)
        if closed: self.stack.append(node)
    def handle_endtag(self, tag):
        '''Metodo invocato per tag chiusi'''
        if self.stack and self.stack[-1].tag == tag:
            self.stack[-1].opentag = False
            self.stack = self.stack[:-1]
    def handle_data(self, data):
        '''Metodo invocato per il testo'''
        if not self.stack: return
        self.stack[-1].content.append( HTMLNode('_text_',{},data))
    def handle_comment(self, data): pass
    def handle_entityref(self, name):
        '''Metodo invocato per caratteri speciali'''
        if name in name2codepoint: c = unichr(name2codepoint[name])
        else: c = '&'+name
        if not self.stack: return
        self.stack[-1].content.append(HTMLNode('_text_',{},c))
    def handle_charref(self, name):
        '''Metodo invocato per caratteri speciali'''
        if name.startswith('x'): c = unichr(int(name[1:], 16))
        else: c = unichr(int(name))
        if not self.stack: return
        self.stack[-1].content.append(HTMLNode('_text_',{},c))
    def handle_decl(self, data): pass
        


def statistiche(fhtml, k1, k2):
    '''Implementare la funzione qui'''
    
    