package human

import (
    "testing"
    "time"
)

var person1 = Person{"Marcus",
                     "Willock",
                     time.Date(1988, time.January, 19, 0, 0, 0, 0, time.UTC),
                     "Male",
                     []string{"Computers"},
                     []string{"Work"}}

var person2 = Person{"Marcus",
                     "Willock",
                     time.Date(1988, time.January, 19, 0, 0, 0, 0, time.UTC),
                     "Male",
                     []string{"Computers"},
                     []string{"Work"}}

var person3 = Person{"Marcus",
                     "Willock",
                     time.Date(1988, time.January, 19, 0, 0, 0, 0, time.UTC),
                     "Male",
                     []string{"Computers", "People"},
                     []string{"Work"}}

var people = []Person{person1, person2, person3}

func TestPersonString(t *testing.T){
    answer := "Marcus Willock"
    for _, p :=range people{
        if p.String() != answer{
            t.Errorf("%s != %s", p.String(), answer)
        }
    }
}

func TestPersonAge(t *testing.T){
    answer := 28 //Note that this grows by one every year.
    if person1.Age() != answer{
        t.Errorf("Age: %d != %d", person1.Age(), answer)
    }
}

func TestPersonEqual(t *testing.T){
    if !person1.Equal(person2){
        t.Errorf("%s != %s", person1, person2)
    }

    if person1.Equal(person3){
        t.Errorf("%s == %s", person1, person3)
    }
}
