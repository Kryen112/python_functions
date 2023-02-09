from collections import defaultdict
import unittest

def two_sum(numbers, target):
    """
    Finds pairs of indices in the 'numbers' list whose elements sum to the given 'target'.
    'numbers' must be a list of integers and 'target' must be an integer.
    
    Parameters:
    numbers (list): a list of integers
    target (integer): an integer to which pairs of elements in 'numbers' should sum
    
    Returns:
    set: a set of tuples, each tuple representing a pair of indices of the 'numbers' list
    
    Raises:
    TypeError: if 'numbers' is not a list or 'target' is not an integer
    TypeError: if not all elements in the 'numbers' list are integers
    
    Examples:
    >>> two_sum([1, 2, 3, 4], 5)
    {(0, 3)}
    >>> two_sum([1, 2, 3, 4], 10)
    set()
    """

    check_input_types(numbers, target)
    
    pairs = set()
    seen = defaultdict(list)

    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            for j in seen[complement]:
                pairs.add((j, i))
        seen[num].append(i)

    return pairs

def check_input_types(numbers, target):
    """
    Checks that the input types for the 'two_sum' function are correct.
    'numbers' must be a list of numbers of integers and 'target' must be an integer.
    
    Parameters:
    numbers (list): a list of integers
    target (integer): an integer to which pairs of elements in 'numbers' should sum
    
    Raises:
    TypeError: if 'numbers' is not a list
    TypeError: if not all elements in the 'numbers' list are integers
    TypeError: if 'target' is not an integer
    
    Examples:
    >>> check_input_types([1, 2, 3, 4], 5)
    >>> check_input_types([1, 2, '3', 4], 5)
    TypeError: All elements in the 'numbers' list must be integers, but got <class 'str'> instead.
    >>> check_input_types({1, 2, 3, 4}, 5)
    TypeError: The 'numbers' parameter must be a list, but got <class 'set'> instead.
    >>> check_input_types([1, 2, 3, 4], '5')
    TypeError: The 'target' parameter must be an integer, but got <class 'list'> instead.
    """

    if type(numbers) is not list:
        raise TypeError("The 'numbers' parameter must be a list, but got " + str(type(numbers)) + " instead.")
    
    if not all(map(lambda x: type(x) is int, numbers)):
        raise TypeError("All elements in the 'numbers' list must be integers, but got " + 
                        str([type(x) for x in numbers if type(x) is not int]) + " instead.")
    
    if type(target) is not int:
        raise TypeError("The 'target' parameter must be an integer, but got " + str(type(target)) + " instead.")

class TestTwoSum(unittest.TestCase):
    """
    Attributes:
        None

    Methods:
        test_two_sum_correct_output (self): Tests that the two_sum function returns the expected output.
        test_two_sum_correct_input_types (self): Tests that the two_sum function raises the correct errors for incorrect input types.
        test_two_sum_empty_input (self): Tests the two_sum function on an empty input.
        test_two_sum_no_pairs (self): Tests the two_sum function when there are no pairs of numbers that sum to the target.
        test_two_sum_multiple_pairs (self): Tests the two_sum function when there are multiple pairs of numbers that sum to the target.
        test_two_sum_negative_numbers (self): Tests the two_sum function when the numbers in the input list include negative numbers.

    Examples:
        >>> test_two_sum = TestTwoSum()
        >>> test_two_sum.run_tests()
    """

    def test_two_sum(self):
        """
        Test the two_sum function to ensure it returns the correct indices of elements in the list that sum to the target.
        """

        """
        Test 1: normal case
        """
        numbers = [1, 2, 3, 4]
        target = 5
        result = two_sum(numbers, target)
        self.assertEqual(result, {(0, 3), (1, 2)})

        """
        Test 2: no pairs found
        """
        numbers = [1, 2, 3, 4]
        target = 10
        result = two_sum(numbers, target)
        self.assertEqual(result, set())

    def test_check_input_types(self):
        """
        Test the check_input_types function to ensure it correctly checks the types of the input parameters.
        """

        """
        Test 1: correct input types
        """
        numbers = [1, 2, 3, 4]
        target = 5
        self.assertIsNone(check_input_types(numbers, target))

        """
        Test 2: numbers is not a list
        """
        numbers = {1, 2, 3, 4}
        target = 5
        with self.assertRaises(TypeError) as cm:
            check_input_types(numbers, target)
        self.assertEqual(str(cm.exception), "The 'numbers' parameter must be a list, but got <class 'set'> instead.")

        """
        Test 3: not all elements in numbers are integers
        """
        numbers = [1, 2, '3', 4]
        target = 5
        with self.assertRaises(TypeError) as cm:
            check_input_types(numbers, target)
        self.assertEqual(str(cm.exception), "All elements in the 'numbers' list must be integers, but got [<class 'str'>] instead.")

        """
        Test 4: target is not an integer
        """
        numbers = [1, 2, 3, 4]
        target = '5'
        with self.assertRaises(TypeError) as cm:
            check_input_types(numbers, target)
        self.assertEqual(str(cm.exception), "The 'target' parameter must be an integer, but got <class 'str'> instead.")

if __name__ == '__main__':
    unittest.main()