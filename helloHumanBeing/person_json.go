package main

import(
    "time"
    "fmt"
    "os"
    "github.com/crazcalm/python-go-hello-to-the-world/helloHumanBeing/human"
)


func main(){
    test := human.Person{
        "Marcus",
        "Willock",
        time.Date(1988, time.January, 19, 0, 0, 0, 0, time.UTC),
        "male",
        []string{"hanging out with friends"},
        []string{"waking up in the morning"},
    }
    fmt.Println(test)

    //learn to open files
    f, err := os.Open("test_json")
    defer f.Close()
    if err != nil{
        fmt.Errorf("Error reading file.")
        os.Exit(1)
    }
    fmt.Println(f)
}
