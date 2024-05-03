# Done by Mungai Simon Munga 662150

import unittest

def roman_to_int(roman):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0
    for numeral in roman[::-1]:
        value = roman_dict.get(numeral, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

# The Tests 
# 1. Single Letters:I, V, X, L, C, D, M.
class TestRomanToInt(unittest.TestCase):
    def test_single_letters(self):
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('V'), 5)
        self.assertEqual(roman_to_int('X'), 10)
        self.assertEqual(roman_to_int('L'), 50)
        self.assertEqual(roman_to_int('C'), 100)
        self.assertEqual(roman_to_int('D'), 500)
        self.assertEqual(roman_to_int('M'), 1000)

#2. Many Letters: XI
    def test_many_letters(self):
        self.assertEqual(roman_to_int('XI'), 11)

# 3. Subtractive notation (SN):IV
    def test_subtractive_notation(self):
        self.assertEqual(roman_to_int('IV'), 4)

#4. With and without SN:XIV
    def test_with_and_without_subtractive_notation(self):
        self.assertEqual(roman_to_int('XIV'), 14)

# 5. Repetition  
    def test_repetition(self):
        self.assertEqual(roman_to_int('II'), 2)

#6. First number:I
    def test_first_number(self):
        self.assertEqual(roman_to_int('I'), 1)

#7. inValid Letter:Z
    def test_invalid_letter(self):
        self.assertEqual(roman_to_int('Z'), 0)

#8. Invalid and valid Letter: XIZ
    def test_invalid_and_valid_letters(self):
        self.assertEqual(roman_to_int('XIZ'), 0)

#9. Not Valid:VV
    def test_not_valid(self):
        self.assertEqual(roman_to_int('VV'), 0)

#10. Null
    def test_null(self):
        self.assertEqual(roman_to_int(''), 0)

if __name__ == '__main__':
    unittest.main()
