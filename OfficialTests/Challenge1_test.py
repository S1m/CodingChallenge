from Challenge1 import Sum

def test_challenge1():
    c = Sum()
    assert c(1) == 1
    assert c(2) == 3
    assert c(3) == 6
    assert c(4) == 10
    assert c(5) == 15
    assert c(6) == 21
    assert c(7) == 28
    assert c(8) == 36
    assert c(9) == 45
    assert c(10) == 55

