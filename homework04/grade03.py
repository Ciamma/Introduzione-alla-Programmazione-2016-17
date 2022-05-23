#! /usr/bin/env python3 -B

from testlib import check, check_img_file, runtests

def test_program03_0():
    import program03
    program03.burna('img03_01_in.png', 'img03_01_out.png', 100, (250,200))
    check_img_file('img03_01_out.png', 'img03_01_check.png')
    return 2

def test_program03_1():
    import program03
    program03.burna('img03_01_in.png', 'img03_02_out.png', 100, (150,200), (350,200))
    check_img_file('img03_02_out.png', 'img03_02_check.png')
    return 2

def test_program03_2():
    import program03
    program03.burna('img03_01_in.png', 'img03_03_out.png', 50, (150,150), (350,150),(250,250))
    check_img_file('img03_03_out.png', 'img03_03_check.png')
    return 3
    
def test_program03_3():
    import program03
    program03.burna('img03_05_in.png', 'img03_05_out.png', 70, (200,200))
    check_img_file('img03_05_out.png', 'img03_05_check.png')
    return 3

def test_program03_4():
    import program03
    program03.burna('img03_04_in.png', 'img03_04_out.png', 50, (50,60), (170,60),(115,165))
    check_img_file('img03_04_out.png', 'img03_04_check.png')
    return 5
 
tests = [test_program03_0, test_program03_1, test_program03_2, test_program03_3, test_program03_4]

if __name__ == '__main__':
    runtests(tests,logfile='grade03.csv')
