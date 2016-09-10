import json
from datetime import date

from human_py.person import Person


def read_json(file):
    with open(file, "r") as f:
        data = f.read()
    json_string = json.loads(data)
    return json_string

def create_people(data):
    people_list = []
    for person in data:
        first_name = person["first_name"]
        last_name = person["last_name"]

        # Need to parse and format the date
        bday = person["birthday"].split("T")[0].split("-")
        birthday = date(int(bday[0]), int(bday[1]), int(bday[2]))

        gender = person["gender"]
        likes = person["likes"]
        dislikes = person["dislikes"]
        testing = Person(first_name, last_name, birthday, gender, likes,
                         dislikes)
        people_list.append(testing)

    return people_list

if __name__ == "__main__":
    data = read_json("test_json")
    people = create_people(data)
    for person in people:
        print(person)
        print("\n------------------------------\n")
