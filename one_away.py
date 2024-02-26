import unittest

class Test(unittest.TestCase):
    test_cases =[
        ("pale", "ple", True),
        ("pales", "pale", True),
        ("pale", "bale", True),
        ("pale", "bake", False),
        ("pale", "bae", False)
        
        
               ]
    def test_one_way(self):
        for [str_a, str_b, expected] in self.test_cases:
            assert one_way(str_a, str_b) == expected
    

def one_way(str_a, str_b):
    "time complexity O(n)"
    charmap = {}
    count = 0
    for a in str_a:
        charmap[a] = 1
    for b in str_b:
        charmap[b] = 0
    for value in charmap.values():
        if value == 1:
            count += 1
    if count > 1:
        return False
    else:
        return True

if __name__ == "__main__":
    unittest.main()
