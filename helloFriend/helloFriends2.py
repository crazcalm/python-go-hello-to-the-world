def _greet_close_friend(friend):
    print("I hug {}\n".format(friend))

def _greet_not_so_close_friend(friend):
    print("Hey {}?! How have you been?\n".format(friend))

def _greet_stranger(stranger):
    print("Hi {}. My name is Marcus".format(stranger))

def _greet_male(male):
    print("Give {} a firm handshake while looking him in the eyes\n".format(male))

def _greet_female(female):
    print("Give {} a slight wave while telling her my name\n".format(female))

def greet_a_person(name, people):
    """
    I should be able to pass in a name of a person and figure out the proper
    way to greet them...
    """
    type_of_friend = None
    gender = None

    # figure out friend type
    if name in people.get("close_friends"):
        type_of_friend = "close_friend"
    elif name in people.get("not_so_close_friends"):
        type_of_friend = "not_so_close_friend"
    else:
        type_of_friend = "stranger"

    # figure out gender
    if name in people.get("males"):
        gender = "male"
    elif name in people.get("females"):
        gender = "female"
    else:
        gender = "Unknown"

    # figure out my actions
    if type_of_friend == "close_friend":
        _greet_close_friend(name)
    elif type_of_friend == "not_so_close_friend":
        _greet_not_so_close_friend(name)
    elif type_of_friend == "stranger":
        _greet_stranger(name)
        if gender == "male":
            _greet_male(name)
        elif gender == "female":
            _greet_female(name)
        else:
            pass      


if __name__ == "__main__":
    close_friends = ["David", "Christy", "Carmela", "Evelyn"]
    not_so_close_friends = ["Tony", "Ivan", "Alex", "Julie"]
    strangers = ["UnknownGuy", "UnknownGirl"]
    males = ["David", "Tony", "Alex", "Ivan", "UnknownGuy"]
    females = ["Christy", "Carmela", "Evelyn", "Julie", "UnknownGirl"]

    people = {
        "close_friends": close_friends,
        "not_so_close_friends": not_so_close_friends,
        "males": males,
        "females": females
    }
    
    greet_a_person("Christy", people)
    greet_a_person("Julie", people)
    greet_a_person("UnknownGuy", people)
    greet_a_person("UnknownGirl", people)
    greet_a_person("UnknownUnknown", people)
