def test_isUniqueChars():
    test_strings = ["a", "abcdefg", "hello", "world", "aa" ""]

    for test_str in test_strings:
        result = isUniqueCharacters(test_str)
        print(f"String: {test_str}, Unique: {result}")



def isUniqueCharacters(string):
    if len(string) > 128:
        return False
    
    char_set = [False] * 128
    
    for char in string:
        value = ord(char)
        if char_set[value]:
            return False
        char_set[value] = True
    return True

test_isUniqueChars()
