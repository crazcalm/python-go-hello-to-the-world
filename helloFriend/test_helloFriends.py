import unittest
from collections import namedtuple
import sys

from helloFriends3 import greet_a_person
from helloFriends3 import print_to_screen


class TesthelloFriends3(unittest.TestCase):

    def setUp(self):
        # The namedtuple is used to make our test more readable
        self.Data = namedtuple("TestData", ["input", "answer", "error_msg"])

        # This test data is the same as the one used before
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
        # If you need some code "clean up" code that runs after each test,
        # then you write that code here.
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
        data = (self.Data("Julie", "Hey Julie?! How have you been?",
                          "female case"),
                self.Data("Tony", "Hey Tony?! How have you been?",
                          "male case"))

        for test in data:
            self.assertEqual(test.answer,
                             "\n".join(
                                       greet_a_person(test.input, self.people)
                                  ),
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
        # One way to test that something is being printed to screen
        # is to capture the system standard output and check that
        # its contents has the content that you printed to screen.
        # In order to do this, you must pass the -b (--buffer) flag
        # to unittest so that the standard output is captured.
        data = [["Hello World"], ["Hi Jo", "I am Marcus"]]
        for test in data:
            print_to_screen(test)
            sys_output = sys.stdout.getvalue()
            self.assertIn("\n".join(test), sys_output)

    def test_print_to_screen_bad_input(self):
        data = ["Hello", b"hi", None]
        for test in data:
            with self.assertRaises(TypeError) as cm:
                print_to_screen(test)
        self.assertEqual(cm.expected, type(cm.exception))

    def test_greet_a_person_bad_input1(self):
        with self.assertRaises(TypeError) as cm:
            # Note that passing None will cause an error
            # because the code expects a dict
            greet_a_person("Christy", None)

        self.assertEqual(cm.expected, type(cm.exception))

    def test_greet_a_person_bad_input2(self):

        # Note that passing objects that are not strings
        # do not cause an error, but I would like to fail
        # when something other than a string is passed in.
        data = [None, [], [[]], {}]
        for test in data:
            with self.assertRaises(TypeError) as cm:
                greet_a_person(test, self.people)

            self.assertEqual(cm.expected, type(cm.exception))


if __name__ == "__main__":
    unittest.main(buffer=True)
