from bank import value

def test_value():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("bob") == 100
    assert value("boSRDGSb") == 100