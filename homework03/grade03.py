#! /usr/bin/env python3 -B

from testlib import check, runtests


def test_program03_0():
    import program03
    ts = program03.statistiche('file03_01.html', 2, 2)
    check(ts, (31, 9, 13, 11, 
    {'strong', 'br', 'span', 'caption', 'th', 'em', 'p', 'td', 'tr', 'a', 'img', 'table', 'code', 'h1', 'html', 'body'}))
    ts = program03.statistiche('file03_01.html', 3, 0)
    check(ts, (31, 2, 33, 11, 
    {'strong', 'br', 'span', 'caption', 'th', 'em', 'p', 'td', 'tr', 'a', 'img', 'table', 'code', 'h1', 'html', 'body'}))
    return 5

def test_program03_1():
    import program03
    ts = program03.statistiche('file03_02.html', 2, 2)
    check(ts, (3863, 1384, 911, 306, 
    		  {'sup', 'pre', 'br', 'dt', 'tt', 'li', 'th', 'script', 'div', 'td', 'tr', 'button',
    		  'a', 'img', 'code', 'ol', 'abbr', 'input', 'body', 'meta', 'dd', 'strong', 'h4', 'link', 
    		  'i', 'form', 'span', 'b', 'ul', 'h3', 'caption', 'small', 'p', 'dl', 'h2', 'style', 
    		  'table', 'h5', 'title', 'head', 'h1', 'html', 'label'}))
    ts = program03.statistiche('file03_02.html', 5, 6)
    check(ts, (3863, 8, 181, 306, 
    		  {'sup', 'pre', 'br', 'dt', 'tt', 'li', 'th', 'script', 'div', 'td', 'tr', 'button', 
    		  'a', 'img', 'code', 'ol', 'abbr', 'input', 'body', 'meta', 'dd', 'strong', 'h4', 'link',
    		  'i', 'form', 'span', 'b', 'ul', 'h3', 'caption', 'small', 'p', 'dl', 'h2', 'style', 
    		  'table', 'h5', 'title', 'head', 'h1', 'html', 'label'}))
    return 5

def test_program03_2():
    import program03
    ts = program03.statistiche('file03_03.html', 2, 3)
    check(ts, (3002, 1212, 582, 193, 
    		  {'sup', 'br', 'li', 'th', 'script', 'div', 'td', 'tr', 'button', 'a', 'img', 'ol', 'input',
    	       'body', 'meta', 'strong', 'h4', 'link', 'i', 'form', 'span', 'b', 'ul', 'small', 'p', 'h2', 
               'style', 'table', 'h5', 'title', 'head', 'h1', 'blockquote', 'html', 'label'}))
    ts = program03.statistiche('file03_03.html', 6, 8)
    check(ts, (3002, 4, 83, 193, 
    		  {'sup', 'br', 'li', 'th', 'script', 'div', 'td', 'tr', 'button', 'a', 'img', 'ol', 'input', 
    		  'body', 'meta', 'strong', 'h4', 'link', 'i', 'form', 'span', 'b', 'ul', 'small', 'p', 'h2', 
              'style', 'table', 'h5', 'title', 'head', 'h1', 'blockquote', 'html', 'label'}))
    return 5



tests = [test_program03_0, test_program03_1, test_program03_2]

if __name__ == '__main__':
    runtests(tests,logfile='grade03.csv')

