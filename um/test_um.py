from um import count

def test():
    assert count('hello, um, world') == 1
    assert count('um, hello, um, world') == 2
    assert count('um...') == 1
    assert count('um...') == 1
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2
