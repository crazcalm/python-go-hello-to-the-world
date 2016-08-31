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
        for _, p :=range group {
            result += fmt.Sprintf("\t%s\n", p)
        }
    }
    return result
}

func (n Network) HasGroup (group string) bool {
    _, ok := n.groups[group]
    return ok
}

func (n Network) AddGroup (group string, value []Person) error {
    var err error
    if !n.HasGroup(group){
        n.groups[group] = value
    }else{
        errMsg := fmt.Sprintf("Group %s already exists", group)
        fmt.Fprintf(os.Stderr, errMsg)
        err = fmt.Errorf(errMsg)
    }
    return err
}

func (n Network) RemoveGroup (group string) error {
    var err error
    if n.HasGroup(group){
        delete(n.groups, group)
    }else{
        errMsg := fmt.Sprintf("Group %s does not exist", group)
        fmt.Fprintf(os.Stderr, errMsg)
        err = fmt.Errorf(errMsg)
    }
    return err
}

// Need to add error handling
func (n Network) GetGroup (p Person) (string, error) {
    var result string
    var err error
    for group, people := range n.groups{
        for _, person := range people{
            if p.Equal(person){
                result = group
            }
        }
    }

    //Need to check that the result is real
    _, ok := n.groups[result]
    if !ok{
        errMsg := fmt.Sprintf("Person %s is not in any groups", p)
        err = fmt.Errorf(errMsg)
    }

    return result, err
}
