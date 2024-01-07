from plates import is_valid

def test_start_letters():
    assert is_valid("CS") == True
    assert is_valid("CS50") == True
    assert is_valid("H") == False
    assert is_valid("@CSP") == False
    assert is_valid("0sc") == False
    assert is_valid("50") == False
    assert is_valid("11cs50") == False

def test_middle_num():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("CS05") == False


def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("CS50!") == False

def test_char_length():
    assert is_valid("OUTATIME") == False
    assert is_valid("Hello,  world") == False
    assert is_valid("AAA222") == True
    assert is_valid("CS") == True
    assert is_valid(" H") == False
