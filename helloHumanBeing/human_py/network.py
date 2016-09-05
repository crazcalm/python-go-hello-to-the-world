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

    def remove_group(self, group_name):
        if not self.has_group(group_name):
            raise NameError("{} is not a group".format(group_name))

        self.__delattr__(group_name)

        self.groups.pop(group_name)

    def get_group(self, person):
        result = None
        for key, value in self.groups.items():
            if person in value:
                result = key
                break
        return result

    def __contains__(self, person):
        union = set().union(*group.values())
        return person in union

    def __str__(self):
        result = "Social Network:\n\n"
        for key, value in self.groups.items():
            result += "{}: {}\n".format(key, value)
        return result


if __name__ == "__main__":
    close_friends = ["David", "Christy", "Carmela", "Evelyn"]
    not_so_close_friends = ["Tony", "Ivan", "Alex", "Julie"]
    strangers = ["UnknownGuy", "UnknownGirl"]
    test = Network(set(close_friends), set(not_so_close_friends),
                   set(strangers), set(["Marcus"]))
    print(test)
    print(test.get_group("Marcus"))
    print(test.has_group("close_friends"))
    print(test.has_group("haters"))
    test.add_group("haters", set(["Willock"]))
    print(test)
    test.remove_group("haters")
    test.remove_group("strangers")
    print(test)
