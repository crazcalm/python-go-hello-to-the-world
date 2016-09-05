package main

import (
	"fmt"
)

func printToScreen(stringSlice []string) {
	for _, _string := range stringSlice {
		fmt.Println(_string)
	}
	fmt.Printf("\n\n")
}

func greetCloseFriend(friend string) string {
	return fmt.Sprintf("I hug %s", friend)
}

func greetNotSoCloseFriend(friend string) string {
	return fmt.Sprintf("Hey %s?! How have you been?", friend)
}

func greetStranger(stranger string) string {
	return fmt.Sprintf("Hi %s. My name is Marcus", stranger)
}

func greetMale(male string) string {
	return fmt.Sprintf("Give %s a firm handshake while looking him in the eyes", male)
}

func greetFemale(female string) string {
	return fmt.Sprintf("Give %s a slight wave while telling her my name", female)
}

// I need to rethink how I am going to write this...
func greetAPerson(name string, people map[string][]string, genders map[string][]string) {
	var typeOfFriend string // relationship of person
	var gender string  // gender of person
	var greetings []string //

    // Checks to see if there is a typeOfFriend relationship
    // list for the name of the parson that was passed in.
	for key, values := range people {
		for _, value := range values {
			if name == value {
				typeOfFriend = key
				break
			}
		}
        // This is used to break out of the outer for loop.
		if typeOfFriend != "" {
			break
		}
	}

	// If a relationship was not found, make them a stranger.
	if typeOfFriend == "" {
		typeOfFriend = "stranger"
	}

    // Checks to see if we know the gender for this person.
	for key, values := range genders {
		for _, value := range values {
			if name == value {
				gender = key
				break
			}
		}
        // Used to break out of the outer for loop.
		if gender != "" {
			break
		}
	}

	// add if; else if; else statement for calling the right function
	if typeOfFriend == "closeFriend" {
		greetings = append(greetings, greetCloseFriend(name))
	} else if typeOfFriend == "notSoCloseFriend" {
		greetings = append(greetings, greetNotSoCloseFriend(name))
	} else if typeOfFriend == "stranger" {
		greetings = append(greetings, greetStranger(name))

		if gender == "male" {
			greetings = append(greetings, greetMale(name))
		} else if gender == "female" {
			greetings = append(greetings, greetFemale(name))
		}
	}
	printToScreen(greetings)
}

func main() {
	closeFriends := []string{"David", "Christy", "Carmela", "Evelyn"}
	notSoCloseFriends := []string{"Tony", "Ivan", "Alex", "Julie"}
	strangers := []string{"UnknownGuy", "UnknownGirl"}
	males := []string{"David", "Tony", "Alex", "Ivan", "UnknownGuy"}
	females := []string{"Christy", "Carmela", "Evelyn", "Julie", "UnknownGirl"}

	people := map[string][]string{
		"closeFriend":      closeFriends,
		"notSoCloseFriend": notSoCloseFriends,
		"stranger":         strangers,
	}

	genders := map[string][]string{
		"male":   males,
		"female": females,
	}

	greetAPerson("David", people, genders)
	greetAPerson("UnknownGirl", people, genders)
}
