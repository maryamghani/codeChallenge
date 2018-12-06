import unittest


def string_has_all_unique_character(string):
    # Cracking code interview 1.1
    dic = {}
    li = list(string.lower())
    for x in li:
        dic[x] = li.count(x)
    print(dic)
    for k, v in dic.items():
        if v > 1:
            return False
    return True


class TestCrackingCodingInterview(unittest.TestCase):
    def test_not_unique_ch(self):
        actual = string_has_all_unique_character('hi are you')
        self.assertEqual(actual, False)
        
    def test_unique_ch(self):
        actual = string_has_all_unique_character('hi')
        self.assertEqual(actual, True)
        
    def test_with_upper_case_ch(self):
        actual = string_has_all_unique_character('HeO World')
        self.assertEqual(actual, False)