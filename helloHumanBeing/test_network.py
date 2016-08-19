import unittest
import sys
from collections import namedtuple

from network import Network


class TestNetwork(unittest.TestCase):
    def setUp(self):
        self.close_friends = set(["David", "Christy", "Carmela", "Evelyn"])
        self.not_so_close_friends = set(["Tony", "Ivan", "Alex", "Julie"])
        self.strangers = set(["UnknownGuy", "UnknownGirl"])
        self.dislike = set(["Marcus"])

        self.Group = namedtuple("Data", ["group_name", "value"])
        self.Data = namedtuple("Errors", ["error", "group"])
        self.new_group = self.Group("haters", set(["Willock"]))
        self.existing_group = self.Group("strangers", set(["J.Cole"]))
        self.bad_value_group = self.Group("love", None)
        self.bad_groups = [self.Data(NameError, self.existing_group),
                           self.Data(TypeError, self.bad_value_group)]

        self.a_group_name = "strangers"
        self.not_a_group_name = "power_rangers"

        self.network = Network(self.close_friends, 
                               self.not_so_close_friends,
                               self.strangers,
                               self.dislike)

        self.print_network_lines = ["Social Network:",
                                    "close_friends: {",
                                    "people_i_dislike: {'Marcus'}",
                                    "not_so_close_friends: {",
                                    "strangers: {"]

    def test_has_group_good_input(self):
        self.assertTrue(self.network.has_group(self.a_group_name))

    def test_has_group_bad_input(self):
        self.assertFalse(self.network.has_group(self.not_a_group_name))

    def test_add_group_good_input(self):
        self.network.add_group(*self.new_group)
        self.assertTrue(self.network.has_group(self.new_group.group_name))
        self.assertEqual(self.new_group.value,
                         self.network.__getattribute__(
                             self.new_group.group_name))

    def test_Add_group_bad_input(self):
        for data in self.bad_groups:
            with self.assertRaises(data.error) as cm:
                self.network.add_group(*data.group)
            self.assertEqual(cm.expected, type(cm.exception))

    def test_remove_group_good_input(self):
        self.network.remove_group(self.a_group_name)
        self.assertFalse(self.network.has_group(self.a_group_name))

    def test_remove_group_bad_input(self):
        with self.assertRaises(NameError) as cm:
            self.network.remove_group(self.not_a_group_name)
        self.assertEqual(cm.expected, type(cm.exception))

    def test__str__(self):
        print(self.network)
        sys_output = sys.stdout.getvalue()
        for line in self.print_network_lines:
            self.assertIn(line, sys_output)


if __name__ == "__main__":
    unittest.main(buffer=True)
