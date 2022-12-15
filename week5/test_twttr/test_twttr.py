from twttr import shorten

def test_shorten():
    assert shorten("bob") == "bb"
    assert shorten("") == ""
    assert shorten("god bless your soul") == "gd blss yr sl"
    assert shorten("ABCD") == "BCD"
    assert shorten("1234") == "1234"
    assert shorten("!.!.") == "!.!."

