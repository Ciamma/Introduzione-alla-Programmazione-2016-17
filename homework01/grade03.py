#! /usr/bin/env python3 -B

from testlib import check, runtests

def test_program03_0():
    import program03
    args = ['All in the golden afternoon\nFull leisurely we glide;\nFor both our oars, with little skill,\nBy little arms are plied,\nWhile little hands make vain pretence\nOur wanderings to guide.']
    ret = program03.parole(6,8,*args)
    check(ret, ['golden', '', 'little', 'little', 'little pretence', ''])
    return 3.0


def test_program03_1():
    import program03
    args = ['Ah, cruel Three! In such an hour,\nBeneath such dreamy weather,\nTo beg a tale of breath too weak\nTo stir the tiniest feather!\nYet what can one poor voice avail\nAgainst three tongues together?\n\nImperious Prima flashes forth\nHer edict "to begin it"--\nIn gentler tone Secunda hopes\n"There will be nonsense in it!"--\nWhile Tertia interrupts the tale\nNot _more_ than once a minute.\n\nAnon, to sudden silence won,\nIn fancy they pursue\nThe dream-child moving through a land\nOf wonders wild and new,\nIn friendly chat with bird or beast--\nAnd half believe it true.']
    ret = program03.parole(4,4,*args)
    check(ret, ['such hour', 'such', 'tale weak', 'stir', 'what poor', '', '', '', '', 'tone', 'will', 'tale', 'more than once', '', 'Anon', 'they', 'land', 'wild', 'chat with bird', 'half true'])
    return 3.0


def test_program03_2():
    import program03
    args = ['Alice did not at all like the tone of this remark, and thought it would\nbe as well to introduce some other subject of conversation. While she\nwas trying to fix on one, the cook took the cauldron of soup off the\nfire, and at once set to work throwing everything within her reach at\nthe Duchess and the baby--the fire-irons came first; then followed a\nshower of saucepans, plates, and dishes. The Duchess took no notice of\nthem even when they hit her; and the baby was howling so much already,\nthat it was quite impossible to say whether the blows hurt it or not.']
    ret = program03.parole(1,3,*args)
    check(ret, ['did not at all the of and it', 'be as to of she', 'was to fix on one the the of off the', 'and at set to her at', 'the and the the a', 'of and The no of', 'hit her and the was so', 'it was to say the it or not'])
    return 3.0


def test_program03_3():
    import program03
    args = ['Alice was rather doubtful whether she ought not to lie down on her face\nlike the three gardeners, but she could not remember ever having heard\nof such a rule at processions; "and besides, what would be the use of a\nprocession," thought she, "if people had to lie down upon their faces,\nso that they couldn\'t see it?" So she stood still where she was, and\nwaited.\n\nWhen the procession came opposite to Alice, they all stopped and looked\nat her, and the Queen said severely, "Who is this?" She said it to the\nKnave of Hearts, who only bowed and smiled in reply.\n\n"Idiot!" said the Queen, tossing her head impatiently; and turning to\nAlice, she went on, "What\'s your name, child?"\n\n"My name is Alice, so please your Majesty," said Alice very politely;\nbut she added, to herself, "Why, they\'re only a pack of cards, after\nall. I needn\'t be afraid of them!"\n\n"And who are _these_?" said the Queen, pointing to the three gardeners who \nwere lying round the rose-tree; for, you see, as they were lying on their \nfaces, and the pattern on their backs was the same as the rest of the pack,\nshe could not tell whether they were gardeners, \nor soldiers, or courtiers, or three of her own children.\n\n"How should _I_ know?" said Alice, surprised at her own courage. "It\'s\nno business of _mine_."\n\nThe Queen turned crimson with fury, and, after glaring at her for a\nmoment like a wild beast, screamed "Off with her head! Off----"\n\n"Nonsense!" said Alice, very loudly and decidedly, and the Queen was\nsilent.']
    ret = program03.parole(9,9,*args)
    check(ret, ['', 'gardeners', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'gardeners', '', '', 'gardeners', 'courtiers', '', 'surprised', '', '', '', '', '', 'decidedly', ''])
    return 3.0


def test_program03_4():
    import program03
    args = ['CHAPTER II\n\n[Sidenote: _Pool of Tears_]\n\n"CURIOUSER and curiouser!" cried Alice (she was so much\nsurprised, that for a moment she quite forgot how to speak good\nEnglish); "now I\'m opening out like the largest telescope that ever was!\nGood-bye, feet!" (for when she looked down at her feet, they seemed to\nbe almost out of sight, they were getting so far off). "Oh, my poor\nlittle feet, I wonder who will put on your shoes and stockings for you\nnow, dears? I\'m sure _I_ sha\'n\'t be able! I shall be a great deal too\nfar off to trouble myself about you: you must manage the best way you\ncan--but I must be kind to them," thought Alice, "or perhaps they won\'t\nwalk the way I want to go! Let me see: I\'ll give them a new pair of\nboots every Christmas."\n\nAnd she went on planning to herself how she would manage it. "They must\ngo by the carrier," she thought; "and how funny it\'ll seem, sending\npresents to one\'s own feet! And how odd the directions will look!\n\n          Alice\'s Right Foot, Esq.\n              Hearthrug,\n                  near the Fender,\n                      (with Alice\'s love).\n\nOh dear, what nonsense I\'m talking!"\n\nJust then her head struck against the roof of the hall: in fact she was\nnow rather more than nine feet high, and she at once took up the little\ngolden key and hurried off to the garden door.\n\nPoor Alice! It was as much as she could do, lying down on one side, to\nlook through into the garden with one eye; but to get through was more\nhopeless than ever: she sat down and began to cry again.\n\n"You ought to be ashamed of yourself," said Alice, "a great girl like\nyou" (she might well say this), "to go on crying in this way! Stop this\nmoment, I tell you!" But she went on all the same, shedding gallons of\ntears, until there was a large pool all round her, about four inches\ndeep and reaching half down the hall.']
    ret = program03.parole(3,3,*args)
    check(ret, ['', '', '', '', 'and she was', 'for she how', 'now out the was', 'bye for she her', 'out far off', 'who put and for you', 'now sha too', 'far off you you the way you', 'can but won', 'the way Let see new', '', '', 'And she how she', 'the she and how', 'one own And how odd the', '', 'Esq', '', 'the', '', '', '', '', 'her the the she was', 'now and she the', 'key and off the', '', 'was she one', 'the one eye but get was', 'she sat and cry', '', 'You', 'you she say way', 'you But she all the', 'was all her', 'and the'] )
    return 3.0



tests = [test_program03_0, test_program03_1, test_program03_2, test_program03_3, test_program03_4]

if __name__ == '__main__':
    runtests(tests,logfile='grade03.csv')

