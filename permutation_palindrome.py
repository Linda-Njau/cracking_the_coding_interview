import re

def test_isPermutationsofPalindrome():
    string = "no x in nixon"
    result =isPermutationofPalindrome(string)
    print (result)

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

test_isPermutationsofPalindrome()
        