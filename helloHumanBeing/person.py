from datetime import date


class Network:

    def __init__(self, close_friends=set(), not_so_close_friends=set(),
                 strangers=set(), people_i_dislike=set()):
        self.close_friends = close_friends
        self.not_so_close_friends = not_so_close_friends
        self.strangers = strangers
        self.people_i_dislike = people_i_dislike
        self.groups = {"close_friends": self.close_friends,
                       "not_so_close_friends": self.not_so_close_friends,
                       "strangers": self.strangers,
                       "people_i_dislike": self.people_i_dislike}

    def has_group(self, group_name):
        return hasattr(self, group_name)

    def add_group(self, group_name, value=set()):
        if self.has_group(group_name):
            raise NameError("{} is already a group".format(group_name))

        if not isinstance(value, set):
            raise TypeError("recieved type: {}\nexpected type {}"
                            .format(type(value), set))

        self.__setattr__(group_name, value)

        self.groups[group_name] = value

    def get_group(self, person):
        result = None
        for key, value in self.groups.values():
            if person in value:
                result = key
                break
        return result

    def __contains__(self, person):
        union = set().union(*group.values())
        return person in union

    def __str__(self):
        result = "Social Network:\n\n"
        for key, value in self.groups.values():
            result += "{}: {}\n".format(key, value)
        return result


class Person:

    def __init__(self, first_name, last_name, birthday, gender, likes=[], 
                 dislikes=[]):
        self.first_name = first_name
        self.last_name = last_name
        self._birthday = birthday  # Not being validated... 
        self.gender = gender
        self.likes = likes
        self.dislikes = dislikes

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        if not instance(value, date):
            raise TypeError("Need a object of type {}", type(date))
        self._birthday = value

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
    test = Person("Marcus", "Willock", date(1988, 1, 19), "mail")

