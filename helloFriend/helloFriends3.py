def print_to_screen(string_list):
    for string in string_list:
        print(string)
    print("\n")

def _greet_close_friend(friend):
    return "I hug {}".format(friend)

def _greet_not_so_close_friend(friend):
    return "Hey {}?! How have you been?".format(friend)

def _greet_stranger(stranger):
    return "Hi {}. My name is Marcus".format(stranger)

def _greet_male(male):
    return ("Give {} a firm handshake while looking"
            " him in the eyes").format(male)

def _greet_female(female):
    return "Give {} a slight wave while telling her my name".format(female)

def greet_a_person(name, people):
    """
    I should be able to pass in a name of a person and figure out the proper
    way to greet them...
    """
    type_of_friend = None
    gender = None
    greetings = []

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
        greetings.append(_greet_close_friend(name))
    elif type_of_friend == "not_so_close_friend":
        greetings.append(_greet_not_so_close_friend(name))
    elif type_of_friend == "stranger":
        greetings.append(_greet_stranger(name))
        if gender == "male":
            greetings.append(_greet_male(name))
        elif gender == "female":
            greetings.append(_greet_female(name))
        else:
            pass
    return greetings


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
    
    print_to_screen(greet_a_person("Christy", people))
    print_to_screen(greet_a_person("Julie", people))
    print_to_screen(greet_a_person("UnknownGuy", people))
    print_to_screen(greet_a_person("UnknownGirl", people))
    print_to_screen(greet_a_person("UnknownUnknown", people))
