import unittest
from collections import namedtuple

from helloFriends3 import _greet_close_friend
from helloFriends3 import _greet_not_so_close_friend
from helloFriends3 import _greet_stranger
from helloFriends3 import _greet_male
from helloFriends3 import _greet_female
from helloFriends3 import greet_a_person
from helloFriends3 import print_to_screen


class TesthelloFriends3(unittest.TestCase):
    def setUp(self):
        self.Data = namedtuple("TestData", ["input", "answer", "error_msg"])

        self.close_friends = ["David", "Christy", "Carmela", "Evelyn"]
        self.not_so_close_friends = ["Tony", "Ivan", "Alex", "Julie"]
        self.strangers = ["UnknownGuy", "UnknownGirl"]
        self.males = ["David", "Tony", "Alex", "Ivan", "UnknownGuy"]
        self.females = ["Christy", "Carmela", "Evelyn", "Julie", "UnknownGirl"]
        self.people = {
            "close_friends": self.close_friends,
            "not_so_close_friends": self.not_so_close_friends,
            "males": self.males,
            "females": self.females
        }

    def tearDown(self):
        pass

    def test_greet_close_friend(self):
        data = (self.Data("Christy", "I hug Christy", "female case"),
                self.Data("David", "I hug David", "male case"))

        for test in data:
            self.assertIn(test.answer,
                          greet_a_person(test.input, self.people),
                          test.error_msg)


    def test_greet_not_so_close_friend(self):
        data = (self.Data("Julie", "Hey Julie?! How have you been?", "female case"),
                self.Data("Tony", "Hey Tony?! How have you been?", "male case"))

        for test in data:
            self.assertIn(test.answer,
                             greet_a_person(test.input, self.people),
                             test.error_msg)

if __name__ == "__main__":
    unittest.main()
