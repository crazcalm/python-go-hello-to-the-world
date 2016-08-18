import unittest
import sys

from network import Network


class TestNetwork(unittest.TestCase):
    def setUp(self):
        self.close_friends = set(["David", "Christy", "Carmela", "Evelyn"])
        self.not_so_close_friends = set(["Tony", "Ivan", "Alex", "Julie"])
        self.strangers = set(["UnknownGuy", "UnknownGirl"])
        self.dislike = set(["Marcus"])
        self.new_group = ("haters", set(["Willock"]))
        self.network = Network(self.close_friends, 
                               self.not_so_close_friends,
                               self.strangers,
                               self.dislike)

    def test_has_group(self):
        pass

    def test_add_group(self):
        pass

    def test_remove_group(self):
        pass

    def test__str__(self):
        pass


if __name__ == "__main__":
    unittest.main(buffer=True)
