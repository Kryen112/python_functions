import unittest

def find_pairs_with_sum(numbers, target_sum):
    """
    Find all unique pairs of numbers in a list that add up to a target sum.

    Parameters:
    numbers (list): A list of integers.
    target_sum (int): The target sum to find pairs for.

    Returns:
    set: A set of unique pairs of numbers (tuple) that add up to the target sum.
    If no pairs are found, an empty set is returned.

    Raises:
    TypeError: If the 'numbers' parameter is not a list.
                If the values within 'numbers' are not integers.
                If the 'target_sum' parameter is not an integer.

    Example:
    >>> find_pairs_with_sum([1, 2, 3, 4, 5], 5)
    [(1, 4), (2, 3)]
    >>> find_pairs_with_sum([1, 2, 3, 4, 5], 7)
    [(2, 5), (3, 4)]
    """
    check_value_types(numbers, target_sum)
    
    pairs = set()
    for number in numbers:
        difference = target_sum - number
        if difference in numbers and difference != number and number < difference:
            pairs.add((number, difference))
    return pairs

def check_value_types(numbers, target_sum):
    """
    Raise a 'TypeError' if the input parameters are invalid.

    Parameters:
    numbers (list): A list of integers.
    target_sum (int): The target sum to find pairs for.

    Raises:
    TypeError: If the 'numbers' parameter is not a list.
                If the values within 'numbers' are not integers.
                If the 'target_sum' parameter is not an integer.
    """
    if not isinstance(numbers, list):
        raise TypeError("The 'numbers' parameter must be a list, but got " + str(type(numbers)) + " instead.")
    
    if not all(isinstance(number, int) for number in numbers):
        raise TypeError("All elements in the 'numbers' list must be integers, but got " + str([type(x) for x in numbers if not isinstance(x, int)]) + " instead.")
    
    if not isinstance(target_sum, int):
        raise TypeError("The 'target_sum' parameter must be an integer, but got " + str(type(target_sum)) + " instead.")
    
class testFindPairsWithSum(unittest.TestCase):
    """
    Test cases for the find_pairs_with_sum function.
    """

    def test_numbers_not_a_list(self):
        """
        Test if a TypeError is raised if the 'numbers' parameter is not a list.
        """
        with self.assertRaises(TypeError):
            find_pairs_with_sum((1, 2), 7)

    def test_numbers_contain_non_integers(self):
        """
        Test if a TypeError is raised if the values within 'numbers' are not integers.
        """
        with self.assertRaises(TypeError):
            find_pairs_with_sum(['a', 1, 2], 7)

    def test_target_sum_not_integer(self):
        """
        Test if a TypeError is raised if 'target_sum' is not an integer.
        """
        with self.assertRaises(TypeError):
            find_pairs_with_sum([0, 1, 2], '7')

    def test_find_pairs_with_sum(self):
        """
        Test if a the correct answers are given to the problem.
        """
        self.assertSetEqual(find_pairs_with_sum([1, 2, 3, 4, 5], 5), {(1, 4), (2, 3)})
        self.assertSetEqual(find_pairs_with_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 10), {(1, 9), (2, 8), (3, 7), (4, 6)})
        self.assertSetEqual(find_pairs_with_sum([], 10), set())
        self.assertSetEqual(find_pairs_with_sum([1], 10), set())
        self.assertSetEqual(find_pairs_with_sum([1,8], 10), set())
        self.assertSetEqual(find_pairs_with_sum([-1, 11], 10), {(-1, 11)})
        self.assertSetEqual(find_pairs_with_sum([-2, -9, -13, 4, 12, 9, 1, 2], 10), {(1, 9), (-2, 12)})
        self.assertSetEqual(find_pairs_with_sum([1, 1, 3, 3, 5, 5, 7, 100, 9], 10), {(1, 9), (3, 7)})

if __name__ == '__main__':
    unittest.main()