def test_isUniqueChars():
    test_strings = ["a", "abcdefg", "hello", "world", "aa" ""]

    for test_str in test_strings:
        result = isUniqueCharactersHashtable(test_str)
        print(f"String: {test_str}, Unique: {result}")



def isUniqueCharacters(string):
    "Works on the assumption that the string is ASCII characters. Time complexity O(n)"
    if len(string) > 128:
        return False
    
    char_set = [False] * 128
    
    for char in string:
        value = ord(char)
        if char_set[value]:
            return False
        char_set[value] = True
    return True

def isUniqueCharactersSet(str):
    "the complexity is O(n) "
    char_set = set(str)
    if len(char_set) != len(str):
        return False
    else:
        return True

def isUniqueCharactersHashtable(str):
    "the complexity is O(n^2), not efficient"
    charmap = {}
    for char in str:
        if char in charmap.values():
            return False
        charmap[char] = char
    return True

test_isUniqueChars()
