package human

import (
	"fmt"
	"os"
)

type Greetings struct {
	Greetings       map[string]map[string]func(string) string
	DefaultGreeting func(string) string
}

func (g Greetings) String() string {
	var result string
	for key, dict := range g.Greetings {
		result += fmt.Sprintf("%s:\n", key)
		for k, _ := range dict {
			result += fmt.Sprintf("\t%s\n", k)
		}
	}
	return result
}

func (g Greetings) AddAGreeting(relationship string, gender string,
	greeting func(string) string) {

	genders, ok := g.Greetings[relationship]
	if !ok {
		g.Greetings[relationship] = map[string]func(string) string{gender: greeting}
	} else {
		genders[gender] = greeting
	}
}

func (g Greetings) RemoveAGreeting(relationship, gender string) error {
	var err error
	_, ok := g.Greetings[relationship]
	if !ok {
		// Need to learn how to through errors...
		errMsg := fmt.Sprintf("relationship %s does not exist\n",
			relationship)
		fmt.Fprintf(os.Stderr, errMsg)
		// should return error here
		err = fmt.Errorf(errMsg)
		return err
	}
	_, ok = g.Greetings[relationship][gender]
	if !ok {
		errMsg := fmt.Sprintf("relationship %s has no greetings for %s",
			relationship, gender)
		fmt.Fprintf(os.Stderr, errMsg)
		//should return error here
		err = fmt.Errorf(errMsg)
		return err
	}
	delete(g.Greetings[relationship], gender)
	return err
}

func (g Greetings) GreetAPerson(p Person, relationship string) string {
	_, ok := g.Greetings[relationship]
	if !ok {
		return g.DefaultGreeting(p.FirstName)
	}
	greeting, ok := g.Greetings[relationship][p.Gender]
	if !ok {
		return g.DefaultGreeting(p.FirstName)
	}

	return greeting(p.FirstName)
}
