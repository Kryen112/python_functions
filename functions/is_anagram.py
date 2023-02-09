import collections
import unittest

def is_anagram(word1, word2):
    """
    This function returns True if 'word1' and 'word2' are anagrams, False otherwise.
    Both inputs must be strings of the same length.

    Parameters:
    word1 (str): the first word
    word2 (str): the second word

    Returns:
    bool: True if 'word1' and 'word2' are anagrams, False otherwise.

    Raises:
    TypeError: if either 'word1' or 'word2' is not a string
    ValueError: if 'word1' and 'word2' are not of the same length

    Examples:
    >>> is_anagram('listen', 'silent')
    True
    >>> is_anagram('listen', 'silent!')
    False
    """

    are_words_strings(word1, word2)
    
    word1, word2 = normalize_words(word1, word2)
    
    are_words_the_same_length(word1, word2)
    
    return collections.Counter(word1) == collections.Counter(word2)

def are_words_strings(word1, word2):
    """
    Check if both words are strings.

    Args:
    word1 (str): The first word.
    word2 (str): The second word.

    Raises:
    TypeError: If either 'word1' or 'word2' is not a string.
    """

    if not all(map(lambda x: isinstance(x, str), (word1, word2))):
        raise TypeError("Both inputs must be strings.")

def are_words_the_same_length(word1, word2):
    """
    Check if both words are the same length.

    Args:
    word1 (str): The first word.
    word2 (str): The second word.

    Raises:
    ValueError: If 'word1' and 'word2' are not the same length.
    """

    if len(word1) != len(word2): 
        raise ValueError("Both words must have the same length.")

def normalize_words(word1, word2):
    """
    Normalize words by converting to lowercase and removing non-alphanumeric characters.

    Args:
    word1 (str): The first word.
    word2 (str): The second word.

    Returns:
    tuple: A tuple of two normalized words.
    """
    
    word1 = word1.lower()
    word2 = word2.lower()

    word1 = ''.join(char for char in word1 if char.isalnum())
    word2 = ''.join(char for char in word2 if char.isalnum())

    return (word1, word2)

class TestIsAnagram(unittest.TestCase):
    """
    Test case for the `is_anagram` function.
    """

    def test_words_not_string(self):
        """
        Test the case where the inputs are not strings.
        """

        with self.assertRaises(TypeError):
            is_anagram(['listen'], 'silent')

        with self.assertRaises(TypeError):
            is_anagram('listen', ['silent'])

        with self.assertRaises(TypeError):
            is_anagram(['listen'], ['silent'])

    def test_words_not_same_length(self):
        """
        Test the case where the inputs are strings but have different lengths.
        """

        with self.assertRaises(ValueError):
            is_anagram('listen', 'silents')

    def test_words_are_anagrams(self):
        """
        Test the case where the inputs are anagrams.
        """

        self.assertTrue(is_anagram('listen', 'silent'))
        self.assertTrue(is_anagram('LiStEn!', 'SILENT'))
        self.assertTrue(is_anagram('Toss', 'Sost'))

    def test_words_are_not_anagrams(self):
        """
        Test the case where the inputs are not anagrams.
        """
        
        self.assertFalse(is_anagram('listen', 'solved'))

if __name__ == '__main__':
    unittest.main()
