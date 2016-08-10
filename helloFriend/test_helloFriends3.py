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
            self.assertEqual(test.answer,
                             "\n".join(greet_a_person(test.input,
                                                      self.people)),
                          test.error_msg)


    def test_greet_not_so_close_friend(self):
        data = (self.Data("Julie", "Hey Julie?! How have you been?", "female case"),
                self.Data("Tony", "Hey Tony?! How have you been?", "male case"))

        for test in data:
            self.assertEqual(test.answer,
                          "\n".join(greet_a_person(test.input, self.people)),
                          test.error_msg)

    def test_greet_stranger(self):
        data = (self.Data("UnknownGuy",
                          ("Hi UnknownGuy. My name is Marcus\nGive UnknownGuy"
                            " a firm handshake while looking him in the eyes"), 
                          "male case"),
                self.Data("UnknownGirl",
                          ("Hi UnknownGirl. My name is Marcus\nGive "
                           "UnknownGirl a slight wave while telling "
                           "her my name"), 
                          "female case"))

        for test in data:
            self.assertEqual(test.answer,
                             "\n".join(greet_a_person(test.input,
                                                      self.people)),
                             test.error_msg)

    def test_print_to_screen(self):
        pass

    def test_greet_a_person_bad_input(self):
        with self.assertRaises(TypeError) as cm:
            greet_a_person("Christy", None)

        the_exception = cm.exception
        self.assertEqual(cm.expected, type(cm.exception))


if __name__ == "__main__":
    unittest.main()
