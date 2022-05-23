#! /usr/bin/env python3 -B

from testlib import check, runtests


def test_program01_0():
    import program01
    ret = program01.com_url('http://151.100.17.236/~melatti/fondamenti20162017/fondamenti14/notes.2.html', 'http://151.100.17.236/~melatti/fondamenti20162017/fondamenti14/notes.3.html', 'utf8',10)
    check(ret,[(u'fondamenti', 4, 4), (u'istruzioni', 4, 3), (u'operazioni', 2, 3), (u'stylesheet', 2, 2), (u'permettono', 2, 1), (u'googlecode', 1, 1), (u'inlinemath', 1, 1), (u'javascript', 1, 1), (u'parentnode', 1, 1), (u'tantissime', 1, 1)])
    return 3.0

def test_program01_1():
    import program01
    ret = program01.com_url('http://151.100.17.236/~melatti/fondamenti20162017/fondamenti14/notes.2.html', 'http://151.100.17.236/~melatti/fondamenti20162017/fondamenti14/notes.4.html', 'utf8',10)
    check(ret,[(u'istruzioni', 4, 14), (u'fondamenti', 4, 4), (u'istruzione', 1, 7), (u'linguaggio', 3, 1), (u'stylesheet', 2, 2), (u'altrimenti', 2, 1), (u'esecuzione', 2, 1), (u'permettono', 2, 1), (u'googlecode', 1, 1), (u'importante', 1, 1), (u'inlinemath', 1, 1), (u'javascript', 1, 1), (u'operazione', 1, 1), (u'ovviamente', 1, 1), (u'parentnode', 1, 1), (u'precedenza', 1, 1), (u'successivo', 1, 1)])
    return 3.0



def test_program01_2():
    import program01
    ret = program01.com_url('http://151.100.17.236/~melatti/fondamenti20162017/fondamenti14/notes.2.html', 'http://151.100.17.236/~melatti/fondamenti20162017/fondamenti14/notes.3.html', 'utf8',2)
    check(ret,[(u'gt', 162, 120), (u'di', 61, 45), (u'un', 65, 22), (u'in', 53, 32), (u'la', 37, 24), (u'il', 39, 19), (u'em', 18, 16), (u'le', 18, 13), (u'si', 12, 15), (u'se', 12, 12), (u'ad', 11, 8), (u'py', 7, 8), (u'lt', 7, 7), (u'li', 6, 6), (u'al', 9, 2), (u'ma', 8, 1), (u'da', 3, 5), (u'js', 4, 4), (u'ha', 3, 4), (u'ga', 3, 3), (u'fa', 2, 3), (u'it', 2, 2), (u'ol', 2, 2), (u'if', 2, 1), (u'of', 2, 1), (u'at', 1, 1), (u'ie', 1, 1), (u'ua', 1, 1)])
    return 3.0


def test_program01_3():
    import program01
    ret = program01.com_url('http://151.100.17.236/~melatti/fondamenti20162017/fondamenti14/notes.4.html', 'http://151.100.17.236/~melatti/fondamenti20162017/fondamenti14/notes.5.html', 'utf8',7)
    check(ret,[(u'ritorna', 16, 16), (u'stringa', 7, 13), (u'possono', 4, 13), (u'esempio', 6, 7), (u'mathjax', 4, 4), (u'lettere', 2, 4), (u'article', 2, 2), (u'testare', 3, 1), (u'uniroma', 2, 2), (u'abbiamo', 1, 2), (u'charset', 1, 1), (u'content', 1, 1), (u'diverso', 1, 1), (u'doctype', 1, 1), (u'fiscale', 1, 1), (u'infatti', 1, 1), (u'initial', 1, 1), (u'lezioni', 1, 1), (u'osservi', 1, 1), (u'saranno', 1, 1), (u'secondo', 1, 1)])
    return 3.0

def test_program01_4():
    import program01
    ret = program01.com_url('http://151.100.17.236/~melatti/fondamenti20162017/fondamenti14/notes.5.html', 'http://151.100.17.236/~melatti/fondamenti20162017/fondamenti14/notes.6.html', 'utf8',1)
    check(ret,[(u'p', 70, 90), (u'a', 39, 70), (u's', 18, 84), (u'\xe8', 27, 45), (u'e', 30, 39), (u'i', 23, 29), (u'x', 40, 3), (u'h', 21, 10), (u'c', 10, 19), (u'l', 20, 7), (u'd', 11, 10), (u'o', 6, 11), (u't', 1, 15), (u'f', 14, 1), (u'r', 8, 7), (u'g', 10, 2), (u'k', 10, 2), (u'n', 1, 11), (u'b', 8, 1), (u'm', 4, 4), (u'v', 2, 4), (u'q', 2, 2)])
    return 3.0




tests = [test_program01_0, test_program01_1, test_program01_2, test_program01_3, test_program01_4]

if __name__ == '__main__':
    runtests(tests,logfile='grade01.csv')
