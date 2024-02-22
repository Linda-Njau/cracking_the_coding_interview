import re
import unittest
class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    
    def test_isPermutationsofPalindrome(self):
        for [test_string, expected] in self.test_cases:
            assert isPermutationofPalindromeBitwise(test_string) == expected

def isPermutationofPalindrome(string):
    "time complexity O(n)"
    charmap = {}
    count = 0
    new_string = re.sub("[^A-Za-z]","",string).lower()
    for char in new_string:
        charmap[char] = charmap.get(char, 0) + 1
    for char_count in charmap.values():
        if char_count % 2 != 0:
            count += 1
            if count > 1:
                return False
    return True


def isPermutationofPalindromeBitwise(string):
    "time complexity O(n)"
    r = 0
    new_string = re.sub("[^A-Za-z]", "", string).lower()
    for char in new_string:
        val = ord(char)
        mask = 1 << val
        if r & mask:
            r &= ~mask
        else:
            r |= mask
    return (r -1) & r == 0
            
        
    
if __name__ == "__main__":
    unittest.main()
        