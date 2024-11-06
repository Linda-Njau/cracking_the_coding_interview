def isIsomorphic(s: str, t: str) -> bool:
    charmap = {}
    for char_s, char_t in zip(s, t):
        if char_s in charmap:
            if charmap[char_s] != char_t:
                return False
            elif char_t in charmap.values():
                return False
            charmap[char_s] = char_t
    return True
