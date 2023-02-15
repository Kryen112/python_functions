import unittest

MAX_INPUT_LENGTH = 19

def validate_input(number_string):
    """
    Checks if a string contains only digits and is non-negative.

    Parameters:
    number_string (str): The string to check.

    Raises:
    TypeError: If 'number_string' is not a string.
    ValueError: If 'number_string' contains non-digit characters or is negative.
    """
    if not isinstance(number_string, str):
        raise TypeError("number_string must be a string.")
    if not number_string.isdigit():
        raise ValueError("number_string must consist only of digits.")
    if int(number_string) < 0:
        raise ValueError("number_string must be non-negative.")
    if not number_string:
        raise ValueError("number_string cannot be empty.")
    if len(number_string) > MAX_INPUT_LENGTH:
        raise ValueError("number_string is too long.")

def is_palindrome(number_string):
    """
    Checks if a string is a palindrome.

    Parameters:
    number_string (str): The string to check.

    Returns:
    bool: 'True' if 'number_string' is a palindrome, 'False' otherwise.

    Raises:
    TypeError: If 'number_string' is not a string.
    ValueError: If 'number_string' contains non-digit characters or is negative.
    """
    validate_input(number_string)
    return number_string == number_string[::-1]

def add_reverse(number_string):
    """
    Adds a string to its reverse.

    Parameters:
    number_string (str): The string to add.

    Returns:
    str: The result of adding 'number_string' to its reverse.

    Raises:
    TypeError: If 'number_string' is not a string.
    ValueError: If 'number_string' contains non-digit characters or is negative.
    """
    validate_input(number_string)
    return str(int(number_string) + int(number_string[::-1]))

def when_is_this_number_string_a_palindrome(number_string):
    """
    Returns the next palindrome number for a given string, 
    adding it's reverse every time it is not a palindrome.

    Parameters:
    number_string (str): The string for which to find the next palindrome number.

    Returns:
    str: The next palindrome number for 'number_string'.

    Raises:
    TypeError: If 'number_string' is not a string.
    ValueError: If 'number_string' contains non-digit characters or is negative.
    """
    validate_input(number_string)
    while not is_palindrome(number_string):
        number_string = add_reverse(number_string)
    return number_string

class TestPalindromeFunctions(unittest.TestCase):
    """
    A unit test case for the 'validate_input', 'is_palindrome', 'add_reverse',
    and 'when_is_this_number_string_a_palindrome' functions.
    """

    def test_validate_input_with_negative_number_string(self):
        with self.assertRaises(ValueError):
            validate_input("-123")

    def test_validate_input_with_non_digit_number_string(self):
        with self.assertRaises(ValueError):
            validate_input("1234.5")

    def test_validate_input_with_empty_number_string(self):
        with self.assertRaises(ValueError):
            validate_input("")

    def test_validate_input_with_long_number_string(self):
        with self.assertRaises(ValueError):
            validate_input("123456789012345678901")

    def test_validate_input_with_non_string_input(self):
        with self.assertRaises(TypeError):
            validate_input(1234)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("1111"))
        self.assertTrue(is_palindrome("3"))
        with self.assertRaises(TypeError):
            is_palindrome(1234)
        with self.assertRaises(ValueError):
            is_palindrome("one hundred")
        with self.assertRaises(ValueError):
            is_palindrome("-123")
        with self.assertRaises(ValueError):
            is_palindrome("")
        with self.assertRaises(ValueError):
            is_palindrome("123456789012345678901")
        self.assertFalse(is_palindrome("123"))

    def test_add_reverse(self):
        self.assertEqual(add_reverse("175"), "746")
        self.assertEqual(add_reverse("123456"), "777777")
        self.assertEqual(add_reverse("9"), "18")
        self.assertEqual(add_reverse("0"), "0")
        with self.assertRaises(TypeError):
            add_reverse(1234)
        with self.assertRaises(ValueError):
            add_reverse("one hundred")
        with self.assertRaises(ValueError):
            add_reverse("-123")
        with self.assertRaises(ValueError):
            add_reverse("")
        with self.assertRaises(ValueError):
            add_reverse("123456789012345678901")

    def test_when_is_this_number_string_a_palindrome(self):
        self.assertEqual(when_is_this_number_string_a_palindrome("12321"), "12321")
        self.assertEqual(when_is_this_number_string_a_palindrome("12"), "33")
        self.assertEqual(when_is_this_number_string_a_palindrome("123456"), "777777")
        self.assertEqual(when_is_this_number_string_a_palindrome("9"), "9")
        self.assertEqual(when_is_this_number_string_a_palindrome("0"), "0")
        self.assertEqual(when_is_this_number_string_a_palindrome("12345678987654321"), "12345678987654321")
        with self.assertRaises(TypeError):
            when_is_this_number_string_a_palindrome(1234)
        with self.assertRaises(ValueError):
            when_is_this_number_string_a_palindrome("one hundred")
        with self.assertRaises(ValueError):
            when_is_this_number_string_a_palindrome("-123")
        with self.assertRaises(ValueError):
            when_is_this_number_string_a_palindrome("")
        with self.assertRaises(ValueError):
            when_is_this_number_string_a_palindrome("123456789012345678901")

if __name__ == '__main__':
    unittest.main()
