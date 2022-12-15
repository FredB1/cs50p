from plates import is_valid

def test_is_valid():
    assert is_valid("bob") == True
    assert is_valid("NE@asd") == False
    assert is_valid("CS05") == False
    assert is_valid("5saasd") == False
    assert is_valid(".saasd") == False
    assert is_valid("wepoer44") == False
    assert is_valid("wep44d") == False
    assert is_valid("!ep44d") == False