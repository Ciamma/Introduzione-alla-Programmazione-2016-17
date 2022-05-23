#! /usr/bin/env python3 -B

from testlib import check_img_file, runtests


def test_program03_0():
    import program03
    program03.doub('img03_01_in.png', 'img03_01_out.png')
    check_img_file("img03_01_out.png", "img03_01_check.png")
    return 3.0

def test_program03_1():
    import program03
    program03.doub('img03_02_in.png', 'img03_02_out.png')
    check_img_file("img03_02_out.png", "img03_02_check.png")
    return 3.0

def test_program03_2():
    import program03
    program03.doub('img03_03_in.png', 'img03_03_out.png')
    check_img_file("img03_03_out.png", "img03_03_check.png")
    return 3.0

def test_program03_3():
    import program03
    program03.doub('img03_04_in.png', 'img03_04_out.png')
    check_img_file("img03_04_out.png", "img03_04_check.png")
    return 3.0

def test_program03_4():
    import program03
    program03.doub('img03_05_in.png', 'img03_05_out.png')
    check_img_file("img03_05_out.png", "img03_05_check.png")
    return 3.0


tests = [test_program03_0, test_program03_1, test_program03_2, test_program03_3, test_program03_4]

if __name__ == '__main__':
    runtests(tests,logfile='grade03.csv')

