def test_urlify():
    str = 'Mr John Smith'
    result = urlify_replace(str)
    print(result)
    
def urlify_replace(str):
    "time complexity is O(n) time"
    if " " in str:
        new_str= str.replace(" ", "%20")
    return new_str
        

test_urlify()
