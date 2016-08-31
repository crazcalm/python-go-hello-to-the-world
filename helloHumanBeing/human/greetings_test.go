package human

import (
    "testing"
    "fmt"
    "time"
    "strings"
)

var person = Person{"Marcus",
                    "Willock",
                    time.Date(1988, time.January, 19, 0, 0, 0, 0, time.UTC),
                    "Male",
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

var test = map[string]func(string)string{"male": heyGuy, "female": heyGirl}

var relationships = map[string]map[string]func(string)string{"closeFriend": test}

var greetingObject = Greetings{relationships, defaultGreeting}

func TestString(t *testing.T){
    result := greetingObject.String()
    expected := []string{"closeFriend", "male", "female"}
    for _, expect :=range expected{
        if !strings.Contains(result, expect){
            t.Errorf("%s not in %s", expect, result)
        }
    }
}

func TestAddAGreeting(t *testing.T){
    //Making sure it does not panic!
    greetingObject.AddAGreeting("AddAGreeting", "test", heyGuy)
    greetingObject.AddAGreeting("AddAGreeting", "test2", heyGuy)
}

func TestRemoveAGreeting(t *testing.T){
    err := greetingObject.RemoveAGreeting("closeFriend", "male")
    if err != nil{
        t.Errorf(err.Error())
    }
}

func TestGreetAPerson(t *testing.T){
    // need more cases...
    _, err := greetingObject.GreetAPerson(person, "closeFriend")
    if err != nil{
        t.Errorf("Just testing this out")
    }
}
