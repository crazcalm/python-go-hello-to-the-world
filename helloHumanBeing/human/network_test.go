package human

import (
    "testing"
    "time"
    "strings"
)

var person4 = Person{"Person4",
                     "Willock",
                     time.Date(1988, time.January, 19, 0, 0, 0, 0, time.UTC),
                     "Male",
                     []string{"Computers"},
                     []string{"Work"},
              }

var groupMe = []Person{person}
var groupNotMe = []Person{person1, person2, person3, person4}

var network = Network{map[string][]Person{
                        "groupMe": groupMe,
                        "groupNotMe": groupNotMe}}

func TestNetworkString(t *testing.T){
    result := network.String()
    expected := []string{"Marcus Willock",
                         "Person4 Willock",
                         "groupMe",
                         "groupNotMe"}
    for _, expect :=range expected{
        if !strings.Contains(result, expect){
            t.Errorf("%s not in %s", expect, result)
        }
    }
}

func TestHasGroup(t *testing.T){
    tests := []struct{group string
                      answer bool}{
                                    {"me", false},
                                    {"groupMe", true},
                     }
    for _, test := range tests{
        if network.HasGroup(test.group) != test.answer{
            t.Errorf("expected %s for %s", test.answer, test.group)
        }
    }
}

func TestAddGroup(t *testing.T){
    tests := []struct{
                      relationship string
                      people []Person
                     errMsg  string
                    }{
                      {"two", []Person{person2}, ""},
                      {"marcus", []Person{person}, ""},
                      {"marcus", []Person{person1},
                       "Group marcus already exists"},
                     }
    var err error
    for _, test := range tests{
        err = network.AddGroup(test.relationship, test.people)
        if err != nil{

            // used to test the error case
            if err.Error() != test.errMsg{
                t.Errorf("%s != %s", err.Error(), test.errMsg)
            }
        }
    }
}

func TestRemoveGroup(t *testing.T){
    err := network.RemoveGroup("groupMe")
    if err != nil{
        t.Errorf(err.Error())
    }
}

func TestGetGroup(t *testing.T){
    _, err := network.GetGroup(person1)
    if err != nil{
        t.Errorf(err.Error())
    }
}
