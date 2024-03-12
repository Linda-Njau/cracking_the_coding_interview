import unittest

class Test(unittest.TestCase):
    test_cases= [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcde', 'abcde'),
        ('aaaaaa', 'a6'),
        ('a', 'a'),
        ('zzZZ', 'z2Z2')
    ]

    def test_string_comprehension(self):
        for string, expected in self.test_cases:
            actual = string_comprehension(string)
            self.assertEqual(actual, expected)
            
def string_comprehension(string):
    comp_str = ""
    count = 1
    prev_char = string[0]

    for i in range(1, len(string)):
        if string[i] == prev_char:
            count += 1
        else:
            comp_str += prev_char + str(count)
            prev_char = string[i]
            count = 1
        
    comp_str += prev_char + str(count)
    
    return comp_str if len(comp_str) <= len(string) else string 


if __name__ == "__main__":
    unittest.main()
