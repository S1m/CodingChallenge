'''
Trivial Challenge 1
'''

class Sum:
    def __init__(self):
        self.sum = 0

    def add(self, num):
        self.sum += num
        return self.sum

    def __call__(self, num):
        return self.add(num)
    

# Test cases for Sum
def test_sum():
    s = Sum()
    assert s(1) == 1
    assert s(2) == 3
    assert s(3) == 6
    assert s(4) == 10
    assert s(5) == 15
    assert s(6) == 21
    assert s(7) == 28
    assert s(8) == 36
    assert s(9) == 45
    assert s(10) == 55
    print("All test cases passed for Sum")

if __name__ == "__main__":
    test_sum()