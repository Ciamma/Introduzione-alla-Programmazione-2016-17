#! /usr/bin/env python3 -B


from testlib import check, check_img_file, runtests

def test_program01_0():
    import program01
    p1 = program01.Punto(50,70)
    check(p1.to_tuple(),(50,70))
    p1.modifica_punto(0,0)
    check(p1.to_tuple(),(0,0))
    return 1

def test_program01_1():
    import program01
    c1 = program01.Colore(255,0,0)
    check(c1.to_tuple(),(255,0,0))
    c1.modifica_colore(0,0,0)
    check(c1.to_tuple(),(0,0,0))
    return 1

def test_program01_2():
    import program01
    c1 = program01.Colore(10,15,10)
    check(c1.to_tuple(),(10,15,10))
    c2 = program01.Colore(20,5,200)
    check(c2.to_tuple(),(20,5,200))
    check(c1.miscela(c2).to_tuple(),(15,10,105))
    return 1


    
def test_program01_3():
    import program01
    p1 = program01.Punto(50,70)
    c1 = program01.Colore(10,15,10)
    r1 = program01.Rettangolo(p1,40,70,c1)
    testo=r1.__str__()
    check(testo,'punto di inizio:(50, 70)\nlarghezza:40\nlunghezza:70\ncolore:(10, 15, 10)' )
    return 1

def test_program01_4():
    import program01
    p1 = program01.Punto(50,70)
    c1 = program01.Colore(10,15,10)
    r1 = program01.Rettangolo(p1,40,70,c1)
    p1.modifica_punto(0,0)
    c1.modifica_colore(0,0,0)
    testo=r1.__str__()
    check(testo,'punto di inizio:(0, 0)\nlarghezza:40\nlunghezza:70\ncolore:(0, 0, 0)' )
    return 2

def test_program01_5():
    import program01
    p2 = program01.Punto(100,40)
    c2 = program01.Colore(200,200,200)
    r2 = program01.Rettangolo(p2,40,70,c2)
    pa = program01.Punto(120,90)
    ca = program01.Colore(100,100,100)
    ra = program01.Rettangolo(pa,60,40,ca)
    r6 = r2.inter(ra)
    testo=r6.__str__()
    check(testo,'punto di inizio:(120, 90)\nlarghezza:20\nlunghezza:20\ncolore:(150, 150, 150)' )
    return 2

def test_program01_6():
    import program01
    p2 = program01.Punto(100,40)
    c2 = program01.Colore(200,200,200)
    r2 = program01.Rettangolo(p2,40,70,c2)
    pa = program01.Punto(30,140)
    ca = program01.Colore(100,100,100)
    ra = program01.Rettangolo(pa,50,20,ca)
    r6 = r2.inter(ra)
    check(r6,None )
    return 2


def test_program01_7():
    import program01
    p2 = program01.Punto(100,40)
    c2 = program01.Colore(0,250,0)
    r2 = program01.Rettangolo(p2,40,70,c2)
    p5 = program01.Punto(130,20)
    c5 = program01.Colore(0,200,250)
    r5 = program01.Rettangolo(p5,30,30,c5)
    r6 = r2.super(r5)
    testo=r6.__str__()
    check(testo,'punto di inizio:(100, 20)\nlarghezza:60\nlunghezza:90\ncolore:(0, 225, 125)' )
    return 2

def test_program01_8():
    import program01
    p1 = program01.Punto(50,70)
    c1 = program01.Colore(255,0,0)
    r1 = program01.Rettangolo(p1,150,100,c1)

    p2 = program01.Punto(100,40)
    c2 = program01.Colore(0,255,0)
    r2 = program01.Rettangolo(p2,40,70,c2)

    p3 = program01.Punto(120,90)
    c3 = program01.Colore(0,0,255)
    r3 = program01.Rettangolo(p3,60,40,c3)

    p4 = program01.Punto(30,140)
    c4 = program01.Colore(255,255,0)
    r4 = program01.Rettangolo(p4,50,20,c4)

    p5 = program01.Punto(130,20)
    c5 = program01.Colore(0,255,255)
    r5 = program01.Rettangolo(p5,50,20,c5)

    lista=[r2,r3,r4,r5]

    r1.foto(lista,'img01.png')
    check_img_file("img01.png", "img01_check.png")
    return 3



tests = [test_program01_0,test_program01_1,test_program01_2, test_program01_3, test_program01_4, test_program01_5, test_program01_6 ,test_program01_7 ,test_program01_8]


if __name__ == '__main__':
    runtests(tests,logfile='grade01.csv')

