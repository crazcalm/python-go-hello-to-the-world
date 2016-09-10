package main

import (
	"encoding/json"
	"fmt"
	"github.com/crazcalm/python-go-hello-to-the-world/helloHumanBeing/human"
	"io/ioutil"
	"time"
)

func main() {
	p1 := human.Person{
		"Marcus",
		"Willock",
		time.Date(1988, time.January, 19, 0, 0, 0, 0, time.UTC),
		"male",
		[]string{"hanging out with friends"},
		[]string{"waking up in the morning"},
	}

	p2 := human.Person{
		"Jovanna",
		"Teran",
		time.Date(1987, time.September, 17, 0, 0, 0, 0, time.UTC),
		"female",
		[]string{"yoga"},
		[]string{"running"},
	}
	sliceP := []human.Person{p1, p2}

	// Convert our people to json
	data, err := json.MarshalIndent(sliceP, "", "    ")
	if err != nil {
		panic(err)
	}
	fmt.Println(string(data))

	// Opens the file and stores contents to buffer
	b, err := ioutil.ReadFile("test_json")
	if err != nil {
		fmt.Errorf("Error reading file.")
		panic(err)
	}

	// Data structure used to convert json to Go code
	var f []human.Person
	err = json.Unmarshal(b, &f)
	if err != nil {
		fmt.Errorf("Json Unmarshaled failed")
		panic(err)
	}
	fmt.Println(f) // Calls their String method

	for _, p := range f {
		// Printing some stuff to screen as proof of a
		// job well done!
		fmt.Println(p.FirstName)
		fmt.Println(p.LastName)
		fmt.Println(p.Birthday)
		fmt.Printf("\n-----------------\n")
	}
}
