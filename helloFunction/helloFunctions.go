package main

import (
	"fmt"
	"strings"
)

func hello() {
	fmt.Println("Hello World")
}

func helloOneParam(name string) {
	fmt.Printf("Hello %s\n\n", name)
}

func helloTwoParams(name1, name2 string) {
	fmt.Printf("Hello %s and %s\n\n", name1, name2)
}

func helloSlice(listOfNames []string) {
	for _, name := range listOfNames {
		fmt.Printf("Hello %s\n", name)
	}
	fmt.Printf("\n\n")
}

func helloSlice2(listOfNames []string) {
	stringOfNames := strings.Join(listOfNames[:len(listOfNames)-1], ", ")
	fmt.Printf("Hello %s, and %s\n\n", stringOfNames, listOfNames[len(listOfNames)-1])
}

func helloNParams(names ...string) {
	helloSlice(names)
}

func helloNParams2(names ...string) {
	helloSlice2(names)
}

//Go pointers
func helloOneParamPointer(name *string) {
	fmt.Printf("Hello %v\n\n", name)
}

func helloTwoParamsPointer(name1, name2 *string) {
	fmt.Printf("Hello %v and %v\n\n", name1, name2)
}

func main() {
	name1 := "Marcus"
	name2 := "Allen"
	name3 := "Willock"
	name4 := "Jovanna"
	name5 := "Evelyn"
	name6 := "Christy"
	name7 := "TY"
	name1Pointer := &name1
	name2Pointer := &name2

	nameList := []string{name1, name2, name3, name4, name5, name6, name7}

	hello()
	helloOneParam(name1)
	helloTwoParams(name1, name2)
	helloSlice(nameList)
	helloSlice2(nameList)
	helloNParams(name1, name2)
	helloNParams2(name1, name2)

	//Pointer functions
	helloOneParamPointer(name1Pointer)
	helloTwoParamsPointer(name1Pointer, name2Pointer)
}
