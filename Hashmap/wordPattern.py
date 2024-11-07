def wordPattern(pattern: str, s: str) -> bool:
    dict = {}
    words = s.split()
    
    if len(words) != len(pattern):
        return False
    
    for char, word in zip( pattern, words):
        if char in dict:
            if dict[char] != word:
                return False
        else:
            dict[char] = word
    return True
