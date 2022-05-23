#! /usr/bin/env python3 -B

from testlib import check, runtests


def test_program01_0():
    import program01
    res = program01.mesi([1,'10-10-2007', '2-3-1962','casa', '31-11-2007'])
    check(res, [ '*', 'ottobre', '*', '*', '*'])
    return 3


def test_program01_1():
    import program01
    res = program01.mesi(['*','02-06-2019', '2-06-2006','Python', '30-02-1982', '25-02-1982'])
    check(res, [ '*', 'giugno','*', '*', '*', 'febbraio'])
    return 3


def test_program01_2():
    import program01
    res = program01.mesi(['5/6/1991','5-7-1991','7-6-1990-3', 'esercizio', '06-06-19a1'])
    check(res, ['*','*','*','*','*'])
    return 3


def test_program01_3():
    import program01
    res = program01.mesi([['07-07-2011'], '07-08-2011', '1', 1022])
    check(res, ['*','agosto','*','*'])
    return 3


def test_program01_4():
    import program01
    res = program01.mesi(['for i=1 to 10', '02-01-1981', 3.14, '28-04-1913', [], '3.14'])
    check(res, ['*','gennaio','*','aprile','*','*'])
    return 3



tests = [test_program01_0, test_program01_1, test_program01_2, test_program01_3, test_program01_4]

if __name__ == '__main__':
    runtests(tests,logfile='grade01.csv')

