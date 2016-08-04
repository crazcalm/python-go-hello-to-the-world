def greet_close_friends(friends):
    """
    If you greet both male and female friends in the same manner,
    then this is fine.
    """
    for friend in friends:
        print("I hug {}\n".format(friend))

def greet_not_so_close_friends(friends):
    for friend in friends:
        print("Hey {}?! How have you been?\n".format(friend))

def greet_strangers(strangers):
    for stranger in strangers:
        print("Hi {}. My name is Marcus\n".format(stranger))

def greet_males(males):
    for male in males:
        print("Give {} a firm handshake while looking him in the eyes".format(male))

def greet_females(females):
    for female in females:
        print("Give {} a slight wave while telling her my name".format(female))

if __name__ == "__main__":
    close_friends = ["David", "Christy", "Carmela", "Evelyn"]
    not_so_close_friends = ["Tony", "Ivan", "Alex", "Julie"]
    strangers = ["UnknownGuy", "UnknownGirl"]
    males = ["David", "Tony", "Alex", "Ivan", "UnknownGuy"]
    females = ["Christy", "Carmela", "Evelyn", "Julie", "UnknownGirl"]
    
    print("{}:".format(greet_close_friends.__name__))
    greet_close_friends(close_friends)

    print("\n{}:".format(greet_not_so_close_friends.__name__))
    greet_not_so_close_friends(not_so_close_friends)

    print("\n{}:".format(greet_strangers.__name__))
    greet_strangers(strangers)

    print("\n{}:".format(greet_males.__name__))
    greet_males(males)

    print("\n{}:".format(greet_females.__name__))
    greet_females(females)
