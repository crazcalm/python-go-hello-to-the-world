import unittest

from helloFriends2 import _greet_close_friend
from helloFriends2 import _greet_not_so_close_friend
from helloFriends2 import _greet_stranger
from helloFriends2 import _greet_male
from helloFriends2 import _greet_female
from helloFriends2 import greet_a_person


class Testing(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testing(self):
        self.assertEqual(1,1)

class TestHelloFriends2(unittest.TestCase):
    def setUp(self):
        self.expected_input = ["Marcus", "Jovanna Teran", "杜明卫", b"Name1", 
                               u"Name2" ]
        self.unexpected_input = [None, "", "\n\n\n\n", True, False, 5, 20.5,
                                 [], {}]

    def tearDown(self):
        pass

    def test_expected_input__greet_close_friend(self):
        for item in self.expected_input:
            # figure out how to test the buffer
            _greet_close_friend(item)

    def test_unexpected_input__greet_close_friend(self):
        for item in self.unexpected_input:
            # figure which errors should be caught
            _greet_close_friend(item)

    def test_expected_input__greet_not_so_close_friend(self):
        for item in self.expected_input:
            _greet_not_so_close_friend(item)

    def test_unexpected_input__greet_not_so_close_friend(self):
        for item in self.unexpected_input:
            _greet_not_so_close_friend(item)

    def test_expected_input__greet_stranger(self):
        for item in self.expected_input:
            _greet_stranger(item)

    def test_unexpected_input__greet_stranger(self):
        for item in self.unexpected_input:
            _greet_stranger(item)

    def test_expected_input__greet_male(self):
        for item in self.expected_input:
            _greet_male(item)

    def test_unexpected_input__greet_male(self):
        for item in self.unexpected_input:
            _greet_male(item)

    def test_expected_input__greet_female(self):
        for item in self.expected_input:
            _greet_female(item)

    def test_unexpected_input__greet_female(self):
        for item in self.unexpected_input:
            _greet_female(item)


if __name__ == "__main__":
    unittest.main()
