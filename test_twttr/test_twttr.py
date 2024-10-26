from twttr import shorten

def main():
    assert shorten('world') == 'wrld'

def test_capital():
    assert shorten('sA wArUdO') == 's wrd'

def test_lower():
    assert shorten('sa warudo') == 's wrd'

def test_number():
    assert shorten('sa warudo123') == 's wrd123'

def test_punctuation():
    assert shorten('hello, myfriend') == 'hll, myfrnd'
