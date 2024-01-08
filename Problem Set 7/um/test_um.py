from um import count

def test_count():
    assert count("um") == 1
    assert count("um, hello, um, world") == 2
    assert count("um...") == 1

def test_um_in_word():
    assert count("yum") == 0
    assert count("yummy") == 0

def test_caps():
    assert count("UM") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
