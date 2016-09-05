from datetime import date


def _date_validator(value):
    if not isinstance(value, date):
        raise TypeError("Need a object of type {}", type(date))
    return value

class Person:

    def __init__(self, first_name, last_name, birthday, gender, likes=[], 
                 dislikes=[], network=None, greetings=None):
        self.first_name = first_name
        self.last_name = last_name
        self._birthday = _date_validator(birthday)
        self.gender = gender
        self.likes = likes
        self.dislikes = dislikes
        self.network = network
        self.greetings = greetings

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = _date_validator(value)

    @property
    def age(self):
        return (date.today() - self.birthday).days // 365

    def __eq__(self, person):
        result = True
        if not self.first_name == person.first_name:
            result = False

        if not self.last_name == person.last_name:
            result = False

        if not self.birthday == person.birthday:
            result = False 

        if not self.gender == person.gender:
            result = False

        if not self.likes == person.likes:
            result = False

        if not self.dislikes == person.dislikes:
            result = False

        return result

    def __str__(self):
        return ("First Name: {}\n"
                "Last Name: {}\n"
                "Birthday: {}\n"
                "Age: {}\n"
                "Gender: {}\n"
                "Likes: {}\n"
                "Dislikes: {}").format(self.first_name,
                                       self.last_name,
                                       self.birthday,
                                       self.age,
                                       self.gender,
                                       self.likes,
                                       self.dislikes)


if __name__ == "__main__":
    test = Person("Marcus", "Willock", date(1988, 1, 19), "male",
                  ["Python", "Golang"], ["Waking up early", "reality tv"])
    print(test)
