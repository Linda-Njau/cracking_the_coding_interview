def isRotation(s1, s2):
    """Time complexity is O(N) is isSubstring runs at O(A+B)"""
    if len(s1) == len(s2):
        s1s1 = s1 + s1
        return isSubstring(s1s1, s2)
    return False
