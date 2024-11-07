def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    dict = {}
    
    for char in s:
        dict[char] = dict.get(char, 0) + 1
    
    for char in t:
        if char in dict:
            dict[char] -= 1
            if dict[char] < 0:
                return False
        else:
            return False
        
    return all(count == 0 for count in dict.values())
