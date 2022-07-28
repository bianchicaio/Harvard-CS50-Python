from bank import value

def test_zero():
    assert value('Hello') == 0
    assert value('helLO') == 0

def test_twenty():
    assert value('Hi my name is') == 20
    assert value('Hey tHere') == 20

def test_onehundred():
    assert value('My Name Is') == 100
    assert value('Congratulations') == 100