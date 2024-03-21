from Challenge1 import find_zero_sum

def test_example_cases():
    assert find_zero_sum([3, -4, -3, 4, 2, -2]) == [2, -2]
    assert find_zero_sum([1, 2, 3]) == []
    assert find_zero_sum([-2, 2, -3, 3, -4, 4]) == [-4, 4]

def test_no_zero_sum():
    assert find_zero_sum([1, 2, 3, 4, 5]) == []
    assert find_zero_sum([-1, -2, -3, -4, -5]) == []

def test_multiple_zero_sum_pairs():
    assert find_zero_sum([1, 2, -2, -1, 3, -3]) == [1, -1]
    assert find_zero_sum([1, 2, -2, -1, 3, -3, 4, -4]) == [1, -1]
    assert find_zero_sum([-1, -2, 2, 1, -3, 3, -2]) == [2, -2]

def test_single_element():
    assert find_zero_sum([0]) == []
    assert find_zero_sum([1]) == []
    assert find_zero_sum([-1]) == []