package main

import(
    "time"
    "fmt"
    "io/ioutil"
    "encoding/json"
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

    //passes content of file to a buffer
    b, err := ioutil.ReadFile("test_json")
    if err != nil{
        fmt.Errorf("Error reading file.")
        panic(err)
    }
    fmt.Println(string(b))

    var f interface{}
    err = json.Unmarshal(b, &f)
    if err != nil{
        fmt.Errorf("Json Unmarshaled failed")
        panic(err)
    }

    fmt.Println(f)

    /*
    var people = []Person{}
    _, item := range data {
        key, person := range item{
            fname := person["first_name"]
            lname := person["last_name"]
            _bday := person["birthday"]
            bday := time.Date(_bday["year"], _bday["month"], _bday["day"],
                              0, 0, 0, 0, time.UTC)
            gender := person["gender"]
            likes := person["likes"]
            dislikes := person["dislikes"]

            append(people, Person{fname, lname, bday, gender, likes, dislikes})
        }
    }

    fmt.Println(people)
    */
}
