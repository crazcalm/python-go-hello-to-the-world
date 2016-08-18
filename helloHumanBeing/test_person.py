import unittest
from datetime import date

from person import Person

class TestFriend(unittest.TestCase):
    def setUp(self):
        # test data
        self.first_name = "Marcus"
        self.last_name = "Willock"
        self.birthday = date(1988, 1, 19)
        self.gender = "male"
        self.likes = ["Python", "Golang"]
        self.dislikes = ["Waking up early", "reality tv"]

        # creating my people (Marcus clones!)
        self.person = Person(self.first_name,
                             self.last_name,
                             self.birthday,
                             self.gender,
                             self.likes,
                             self.dislikes)

        self.person2 = Person(self.first_name,
                             self.last_name,
                             self.birthday,
                             self.gender,
                             self.likes,
                             self.dislikes)

        self.person3 = Person("hi",
                             self.last_name,
                             self.birthday,
                             self.gender,
                             self.likes,
                             self.dislikes)

        self.person4 = Person(self.first_name,
                             "hi",
                             self.birthday,
                             self.gender,
                             self.likes,
                             self.dislikes)

        self.person5 = Person(self.first_name,
                             self.last_name,
                             self.birthday,
                             date(1,1,1),
                             self.likes,
                             self.dislikes)

        self.person6 = Person(self.first_name,
                             self.last_name,
                             self.birthday,
                             "hi",
                             self.likes,
                             self.dislikes)

        self.person7 = Person(self.first_name,
                             self.last_name,
                             self.birthday,
                             self.gender,
                             ["None"],
                             self.dislikes)

        self.person8 = Person(self.first_name,
                             self.last_name,
                             self.birthday,
                             self.gender,
                             self.likes,
                             ["None"])

        # expected answers
        self.age = 28

    def test_test(self):
        self.assertEqual(1,1)

    def test__eq__(self):
        # Different instance but same info
        self.assertEqual(self.person, self.person2)

        # different first name
        self.assertNotEqual(self.person, self.person3)

        # different last name
        self.assertNotEqual(self.person, self.person4)

        # different birthday
        self.assertNotEqual(self.person, self.person5)

        # different gender
        self.assertNotEqual(self.person, self.person6)

        # different likes
        self.assertNotEqual(self.person, self.person7)

        # different dislikes
        self.assertNotEqual(self.person, self.person8)

    def test_age(self):
        # Note that this answer goes up by 1 every Jan 19th
        self.assertEqual(self.person.age, self.age)

    def test_birthday_error(self):
        with self.assertRaises(TypeError) as cm:
            self.person.birthday("Jan 1, 1988")
        self.assertEqual(cm.expected, type(cm.exception))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
