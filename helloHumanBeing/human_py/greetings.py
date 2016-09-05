class Greetings:

    def __init__(self, default_func, **kwargs):
        self.default_func = default_func
        self.relationships = {}

    def add_greetings(self, greetings):
        for greeting in greetings:
            self.add_a_greeting(*greeting)

    def add_a_greeting(self, type_of_relationship, gender, function):

        # If the relationship exists, I do not want to override it
        if self.relationships.get(type_of_relationship):
            self.relationships[type_of_relationship][gender] = function

        else:
            self.relationships[type_of_relationship] = {gender: function}

    def remove_a_greeting(self, type_of_relationship, gender):
        if self.relationships.get(type_of_relationship):
            if self.relationships[type_of_relationship].get(gender):
                del self.relationships[type_of_relationship][gender]
            else:
                raise NameError("{} does not exist for {} relationship"
                          .format(gender))
        else:
            raise NameError("No relationship by the name of {}"
                      .format(type_of_relationship))

    def greet_a_person(self, person, type_of_relationship):
        gender = person.gender
        if self.relationships.get(type_of_relationship):
            if self.relationships[type_of_relationship].get(gender):
                func = self.relationships[type_of_relationship][gender]
                return func(person)
            else:
                return self.default_func(person)
        else:
            return self.default_func(person)

    def __str__(self):
        return ("Greetings!\n"
                "Default Func: {}\n"
                "greetings dict: {}").format(self.default_func.__name__,
                                             self.relationships)


if __name__ == "__main__":
    def hi(name):
        print("hi {}".format(name))

    def hello(name):
        print("hello sucker! I am {}".format(name))

    test = Greetings(hi)
    print(test)
    test.add_a_greeting("lover", "female", hello)
    print(test)

    class Foo: pass
    jo = Foo()
    jo.gender = "female"
    test.greet_a_person(jo, "lover")
