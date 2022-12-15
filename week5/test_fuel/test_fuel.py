import pytest
from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()
    test_zero_Div()
def test_convert():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
def test_zero_Div():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0") 