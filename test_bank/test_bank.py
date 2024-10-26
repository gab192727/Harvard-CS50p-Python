from bank import value

def testvalue_capital():
    assert value("Hello, friend") == 0

def testvalue_lower():
    assert value("hello, friend") == 0

def testvalue_h():
    assert value("how are you") == 20

def testvalue_main():
    assert value("What's up") == 100
