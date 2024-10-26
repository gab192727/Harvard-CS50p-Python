from seasons import convert_to_minutes

def test_seasons():
    assert convert_to_minutes(2003, 5, 17) == "Ten million, nine hundred forty-nine thousand, seven hundred sixty minutes"
    assert convert_to_minutes(29, 1, 2983) == "Invalid Date"
