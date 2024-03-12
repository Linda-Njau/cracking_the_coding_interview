def test_is_permutation():
    str_a ="baaa"
    str_b = "aaab"

    result = is_permutation_hash_table(str_a, str_b)
    print(result)

def is_permutation_sorting(str_a, str_b):
    """The time complexity is O(n log n) due to the sorting"""
    if len(str_a) != len(str_b):
        return False
    
    if sorted(str_a) != sorted(str_b):
        return False
    else:
        return True
    
def is_permutation_hash_table(str_a, str_b):
    "The time complexity is 0(n)"
    if len(str_a) != len(str_b):
        return False
    
    charmap = {}
    
    for a in str_a:
        charmap[a] = 1
    for b in str_b:
        charmap[b] = 0
        
    if 1 in charmap.values():
        return False
    else:
        return True 

test_is_permutation()


