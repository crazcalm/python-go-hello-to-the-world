package human

import (
	"fmt"
	"os"
	"time"
)

var monthMap = map[string]int{
	"January":   1,
	"February":  2,
	"March":     3,
	"April":     4,
	"May":       5,
	"June":      6,
	"July":      7,
	"August":    8,
	"September": 9,
	"October":   10,
	"November":  11,
	"December":  12,
}

func monthToInt(month string) int {
	// check for error
	// add a panic if value is wrong
	value, ok := monthMap[month]
	if !ok {
		fmt.Fprintf(os.Stderr, "%v is not a supported Month", month)
		os.Exit(1)
	}
	return value
}

// The function compares two slices and returns a boolean
// based on whether or not they are equal.
func compareSlice(slice1, slice2 []string) bool {
	result := true
	for index, value := range slice1 {
		if value != slice2[index] {
			result = false
			break
		}
	}

	return result
}

type Person struct {
	FirstName string
	LastName  string
	Birthday  time.Time // Need to learn how to use...
	Gender    string
	Likes     []string
	Dislikes  []string
}

func (p Person) Age() int {
	delta := time.Now().AddDate(-p.Birthday.Year(),
		monthToInt(p.Birthday.Month().String()),
		p.Birthday.Day())
	return delta.Year()
}

// This method it needed to satisfy the stringer interface.
// This means that printing the struct will call this method.
func (p Person) String() string {
	return fmt.Sprintf("%s %s", p.FirstName, p.LastName)
}

// This method compares two People and returns a boolean
// based on whether or not their attributes are the same.
func (p Person) Equal(p2 Person) bool {
	result := true

	if p.FirstName != p2.FirstName {
		result = false
	} else if p.LastName != p2.LastName {
		result = false
	} else if p.Birthday != p2.Birthday {
		result = false
	} else if p.Gender != p2.Gender {
		result = false
	} else if len(p.Likes) != len(p2.Likes) {
		result = false
	} else if len(p.Dislikes) != len(p2.Dislikes) {
		result = false
	}

	if result == true {
		if compareSlice(p.Likes, p2.Likes) == false {
			result = false
		} else if compareSlice(p.Dislikes, p2.Dislikes) == false {
			result = false
		}
	}

	return result
}

func main() {
	test := Person{"Marcus",
		"Willock",
		time.Date(1988, time.January, 19, 0, 0, 0, 0, time.UTC),
		"Male",
		[]string{"Computers"},
		[]string{"Work"}}

	test2 := Person{"Marcus",
		"Willock",
		time.Date(1988, time.January, 19, 0, 0, 0, 0, time.UTC),
		"Male",
		[]string{"Computers"},
		[]string{"Work"}}

	test3 := Person{"Marcus",
		"Willock",
		time.Date(1988, time.January, 19, 0, 0, 0, 0, time.UTC),
		"Male",
		[]string{"Computers", "People"},
		[]string{"Work"}}
	fmt.Println(test)
	fmt.Println(test.Birthday)
	fmt.Println(test.Age())
	fmt.Println(test.Equal(test2))
	fmt.Println(test.Equal(test3))
}
