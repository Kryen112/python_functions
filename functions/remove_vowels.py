import unittest

VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def remove_vowels(input_string):
    """
    Removes all vowels (both uppercase and lowercase) from the input string and returns the resulting string.
    
    Parameters:
    input_string (str): The input string from which vowels should be removed.
    
    Returns:
    str: The string with all vowels removed.
    
    Raises:
    TypeError: If the input is not a string.
    ValueError: If the input string is empty.
    
    Examples:
    >>> remove_vowels("Hello World!")
    'Hll Wrld!'
    >>> remove_vowels("Python")
    'Pythn'
    """
    check_input(input_string)
    
    output = ""
    for letter in input_string:
        if letter not in VOWELS:
            output = output + letter

    return output.strip()

def check_input(input_string):
    """
    Validates the input for the 'remove_vowels' function.
    
    Parameters:
    input_string (str): The input string to be validated.
    
    Raises:
    TypeError: If the input is not a string.
    ValueError: If the input string is empty.
    """
    if type(input_string) is not str:
        raise TypeError("The 'input' parameter must be a string, but got " + str(type(input_string)) + " instead.")
    
    if input_string == "":
        raise ValueError("The 'input_str' parameter cannot be an empty string.")
    
class TestRemoveVowels(unittest.TestCase):
    def test_remove_vowels_with_valid_input(self):
        self.assertEqual(remove_vowels("Hello World!"), "Hll Wrld!")
        self.assertEqual(remove_vowels("A Python was here"), "Pythn ws hr")
    
    def test_remove_vowels_with_empty_input(self):
        with self.assertRaises(ValueError):
            remove_vowels("")
    
    def test_remove_vowels_with_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_vowels(123)

class TestCheckInput(unittest.TestCase):
    def test_check_input_with_valid_input(self):
        try:
            check_input("Hello World!")
        except Exception as e:
            self.fail("check_input raised an unexpected exception: {}".format(e))
    
    def test_check_input_with_empty_input(self):
        with self.assertRaises(ValueError):
            check_input("")
    
    def test_check_input_with_invalid_input(self):
        with self.assertRaises(TypeError):
            check_input(123)

if __name__ == "__main__":
    unittest.main()