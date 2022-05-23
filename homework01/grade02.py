#! /usr/bin/env python3 -B

from testlib import check, runtests


def test_program02_0():
    import program02
    args = [['a0', 'b1', 'a2', 'b3', 'a4', 'b5'], ['b0', 'a1', 'b2', 'a3', 'b4', 'b5']]
    ret= program02.modi(*args)
    check(args[0], ['a0','a2','a4'])
    check(args[1], ['a1','a3'])
    check(ret, None)
    return 3.0

def test_program02_1():
    import program02
    test_ret = False
    test_arg = True
    args = [['1', '2', '3', '4', '5', '6'], ['4', '5', '6', '1', '2', '3']]
    ret= program02.modi(*args)
    check(args[0], ['1','2','3'])
    check(args[1], ['1','2','3'])
    check(ret, None)
    return 3.0


def test_program02_2():
    import program02
    args = [['bear', 'tiger', 'wolf', 'whale', 'elephant'], ['swan', 'cat', 'dog', 'duck', 'rabbit']]
    ret = program02.modi(*args)
    check(args[0], ['bear','elephant'])
    check(args[1], ['cat','dog','duck'])
    check(ret, None)
    return 3.0


def test_program02_3():
    import program02
    args = [['Taylor', 'Alyssa', 'Allison', 'Grace', 'Sarah'], ['Victoria', 'Audrey', 'Ashley', 'Lillian', 'Sofia']]
    ret = program02.modi(*args)
    check(args[0], ['Taylor', 'Alyssa', 'Allison', 'Grace', 'Sarah'])
    check(args[1], [])
    check(ret, None)
    return 3.0


def test_program02_4():
    import program02
    args = [['Axy', 'xyA', 'yxA', 'yxA'],['axy', 'xya', 'xay', 'yax']]
    ret = program02.modi(*args)
    check(args[0], ['Axy', 'xyA'])
    check(args[1], ['xay', 'yax'])
    check(ret, None)
    return 3.0

tests = [test_program02_0, test_program02_1, test_program02_2, test_program02_3, test_program02_4]


if __name__ == '__main__':
    runtests(tests,logfile='grade02.csv')

