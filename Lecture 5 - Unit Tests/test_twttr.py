from twttr import shorten

def test_shorten_normal():
    assert shorten('Caio Bianchi') == 'C Bnch'
    assert shorten('TEStTeST') == 'TStTST'

def test_shorten_pontuations():
    assert shorten('Test.test,test') == 'Tst.tst,tst'
    assert shorten('test!@#$%') == 'tst!@#$%'

def test_shorten_numbers():
    assert shorten('Test 1') == 'Tst 1'
    assert shorten('TeST 223579') == 'TST 223579'