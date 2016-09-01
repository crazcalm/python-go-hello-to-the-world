package human

import (
	"fmt"
	"strings"
	"testing"
	"time"
)

var person = Person{"Marcus",
	"Willock",
	time.Date(1988, time.January, 19, 0, 0, 0, 0, time.UTC),
	"male",
	[]string{"Computers"},
	[]string{"Work"}}

func defaultGreeting(name string) string {
	return fmt.Sprintf("Hello %s", name)
}

func heyGuy(name string) string {
	return fmt.Sprintf("%s da man!", name)
}

func heyGirl(name string) string {
	return fmt.Sprintf("%s, you go girl!", name)
}

var test = map[string]func(string) string{"male": heyGuy, "female": heyGirl}

var relationships = map[string]map[string]func(string) string{"closeFriend": test}

var greetingObject = Greetings{relationships, defaultGreeting}

func TestString(t *testing.T) {
	result := greetingObject.String()
	expected := []string{"closeFriend", "male", "female"}
	for _, expect := range expected {
		if !strings.Contains(result, expect) {
			t.Errorf("%s not in %s", expect, result)
		}
	}
}

func TestAddAGreeting(t *testing.T) {
	//Making sure it does not panic!
	greetingObject.AddAGreeting("AddAGreeting", "test", heyGuy)
	greetingObject.AddAGreeting("AddAGreeting", "test2", heyGuy)
}

func TestRemoveAGreeting(t *testing.T) {
	err := greetingObject.RemoveAGreeting("AddAGreeting", "test")
	if err != nil {
		t.Errorf(err.Error())
	}
}

func TestGreetAPerson(t *testing.T) {
	tests := []struct {
		p            Person
		relationship string
		answer       string
	}{
		{person,
			"closeFriend",
			"Marcus da man!"},
		{person,
			"Unkown",
			"Hello Marcus"},
	}
	for _, test := range tests {
		result := greetingObject.GreetAPerson(test.p, test.relationship)
		if result != test.answer {
			t.Errorf("%s != %s", result, test.answer)
		}
	}
}
