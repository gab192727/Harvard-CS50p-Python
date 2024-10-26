from plates import is_valid

def test_is_valid_alphanumeric():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid(" 2") == False
    assert is_valid("01") == False
    assert is_valid("0") == False
    assert is_valid("CS05") == False
    assert is_valid("C50S") == False
    assert is_valid("01") == False
    assert is_valid("CS.5") == False
    assert is_valid("thisistoomuch") == False
    assert is_valid("CS5T") == False

