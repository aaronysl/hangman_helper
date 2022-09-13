import unittest
from hangman_intelligent_helper import HangmanHelper

class TestCase(unittest.TestCase):
    def setUp(self):
        self.test_class = HangmanHelper()

    def test_function_should_return_something(self):
        pattern = "s____g"
        used_letters = list("abcde")
        word_list = ["strong","happy","dog"]
        assert self.test_class.guess_next_letter(pattern, used_letters, word_list) is not None

    def test_max_chances_of_guessing(self):
        pattern = "____g"
        used_letters = list("abcdg")
        word_list = ["strong","happy","dog"]
        assert self.test_class.guess_next_letter(pattern, used_letters, word_list) is None

    def test_next_possible_guess(self):
        pattern = "____y"
        used_letters = list("y")
        word_list = ["glory","happy","dog","apple","marry","army"]
        assert self.test_class.guess_next_letter(pattern, used_letters, word_list) == 'r'

    def test_first_try(self):
        pattern = "_____"
        used_letters = list()
        word_list = ["glory","happy","dog","apple","marry","army"]
        assert self.test_class.guess_next_letter(pattern, used_letters, word_list) == 'p'
