from lib import average

def test_average():
    assert average([10, 20, 30]) == 20
    assert average([1, 2, 3, 4]) == 2.5
    assert average([10, -10]) == 0