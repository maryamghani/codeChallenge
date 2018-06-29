"""
Write a function to print a 2-D array (n x m) in spiral order (clockwise).

For example, consider the following input:
***
1 2 3
4 5 6
7 8 9
***

Then the output of your program should be:
***
1 2 3 6 9 8 7 4 5
***
"""

import unittest


class Spiral(object):

    """
    This Method is getting the first array in array
    and calling array_rotation method to read
    the rest of the array and rotating them
    """
    def spiral(self, arr):
        result = []
        c = []
        c.append(arr[0])
        rest_arr = arr[1:]
        while len(rest_arr) > 0:
            rest_arr = self.array_rotation(rest_arr)
            c.append(rest_arr[0])
            rest_arr = rest_arr[1:]
        for items in c:
            for item in items:
                result.append(item)
        return result

    @staticmethod
    def array_rotation(arr):
        li = []
        result = list(zip(*arr))
        for i in range(len(result)-1, -1, -1):
            li.append(list(result[i]))
        return li


# Unit test
class MyTest(unittest.TestCase):
    def test_three_by_three_array(self):
        input_arr = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
        spr = Spiral()
        output = spr.spiral(input_arr)
        expected_result = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEquals(output, expected_result)


if __name__ == '__main__':
    unittest.main()