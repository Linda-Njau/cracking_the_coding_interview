def isPalindrome(s: str) -> bool:
    s = s.islower()
    p1 = 0
    p2 = s(len)- 1
    
    while p1 < p2:
        while p1 < p2 and not s[p1].isalnum():
            p1 += 1
        while p1 < p2 and not s[p2].isalnum():
            p2 -= 1
        
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1
        
    return True
