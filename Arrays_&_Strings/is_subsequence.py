def is_subsequence(s: str, t: str) -> bool:
    ps = pt = 0
    
    while ps < len(s) and pt < len(t):
        if s[ps] == t[ps]:
            ps += 1
        pt += 1
    
    return ps == len(s)
