import unittest
from datetime import date

from greetings import Greetings
from person import Person

class TestGreetings(unittest.TestCase):

    def setUp(self):
        # test data
        self.first_name = "Marcus"
        self.last_name = "Willock"
        self.birthday = date(1988, 1, 19)
        self.gender = "male"
        self.likes = ["Python", "Golang"]
        self.dislikes = ["Waking up early", "reality tv"]

        # creating a Marcus clones!
        self.person = Person(self.first_name,
                             self.last_name,
                             self.birthday,
                             self.gender,
                             self.likes,
                             self.dislikes)

        self.relationship1 = "alter_ego"
        self.relationship2 = "hater"
        self.gender1 = "male"
        self.gender2 = "female"
        self.add_greeting1 = (self.relationship1, self.gender1, self.say_hi)
        self.add_greeting2 = (self.relationship1, self.gender2, self.say_hi)
        self.add_greeting3 = (self.relationship2, self.gender1, self.say_hi)
        self.add_greetings = [self.add_greeting1,
                              self.add_greeting2,
                              self.add_greeting3]

        self.greetings = Greetings(self.default_greeting)

    def default_greeting(self, person):
        return "Hello {}".format(person.first_name)

    def say_hi(self, person):
        return "What's up {}?!".format(person.first_name)

    def test_default_greetings(self):
        self.assertEqual('Hello Marcus',
                         self.greetings.greet_a_person(self.person,
                                                       self.relationship1))

    def test_add_a_greeting(self):
        self.greetings.add_a_greeting(*self.add_greeting1)
        self.assertEqual(self.say_hi,
                         self.greetings
                             .relationships[self.relationship1][self.gender1])

    def test_add_greetings(self):
        self.greetings.add_greetings(self.add_greetings)
        for relationship, gender, func in self.add_greetings:
            self.assertEqual(func,
                             self.greetings
                                 .relationships[relationship][gender])

    def test_remove_a_greetings(self):
        self.greetings.add_a_greeting(*self.add_greeting1)
        self.greetings.remove_a_greeting(self.relationship1, self.gender1)
        self.assertEqual({},
                         self.greetings.relationships.get(self.relationship1))

    def test_greet_a_person(self):
        self.greetings.add_a_greeting(*self.add_greeting1)

        # Hit the appropriate greeting func
        self.assertEqual("What's up Marcus?!",
                         self.greetings.greet_a_person(self.person,
                                                       self.relationship1))
        # Hit the default func
        self.assertEqual("Hello Marcus",
                         self.greetings.greet_a_person(self.person,
                                                       self.relationship2))

if __name__ == "__main__":
    unittest.main()
