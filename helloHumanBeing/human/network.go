/*
I need to learn how to create and propagate errors...
*/
package human

import (
    "fmt"
    "os"
)

type Network struct{
    groups map[string][]Person
}

func (n Network) String () string {
    var result string
    for key, group :=range n.groups{
        result += fmt.Sprintf("%s:\n", key)
        for k, v :=range group {
            result += fmt.Sprintf("\t%s: %v", k, v)
        }
    }
    return result
}

func (n Network) HasGroup (group string) bool {
    _, ok := n.groups[group]
    return ok
}

//Need to add error handling (Exiting the program is mean...).
func (n Network) AddGroup (group string, value []Person) {
    if !n.HasGroup(group){
        n.groups[group] = value
    }else{
        fmt.Fprintf(os.Stderr, "Group %s already exists", group)
        os.Exit(1)
    }
}

// Need to add error handling
func (n Network) RemoveGroup (group string) {
    if n.HasGroup(group){
        delete(n.groups, group)
    }else{
        fmt.Fprintf(os.Stderr, "Group %s does not exist", group)
    }
}

// Need to add error handling
func (n Network) GetGroup (p Person) string {
    var result string
    for group, people := range n.groups{
        for _, person := range people{
            if p.Equal(person){
                result = group
            }
        }
    }
    return result
}
