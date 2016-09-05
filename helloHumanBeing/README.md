#helloHuman
## Python Topics
### classes
### special methods
	These are the underlining methods that make python mogical. To learn about this magic, see the interactive
    help (SPECIALMETHODS).
### del
	In terms of dcitionaries,`del` removes a key from the dictionary. `del` does have other uses
    (deconstructor methods), but I have rarely seen them used. See interactive help for details (DICTIONARIES,
    such for "del").
### cool points
	1. implementing special methods saves lives!
    2. python -m unittest discover -b
        - The "-m" allows you to call python modules
        - Discover is a unittest feature that allows you to "discover" and run
          the tests in your project.

## Go Topics
### Struct
	A struct is an aggregate data type that groups together zero or more named values of arbitrary types as a single
    entity. Each value is called a field.
### Methods
	You can add functions to structs (methods). Basic syntax:
    func (s StrunctNAme) methodName (parms...) returns...{/*Do stuff*/}`
### Interfaces
	An interface is an abstract type. It doesn't expose the representation or interal structure of its values,
    or the set of basic operations they support; it reveals only some of their methods.

    I did not write any interfaces in the code, but we have been implicitly using them because Go uses them.
    For example, the fmt package can print strings to the screen. In order for fmt to be able to print an
    arbitrary struct to the screen (and for you to have control over what is printed), That struct must satisfy
    the Stringer interface (go doc fmt.Stringer). That interface states that my struct must have a method with
    this signature, String() string. Given that this method exists, my struct now satifies and thus fmt can call
    the String method on my struct.
### Testing
	Go's testing is minimalistic in the sense that there is no assert framework for you to use, but it is also
    really rich in the sense that test, profile, benchmark, and check your code coverage. For examples on how to
    test in go see `go doc testing`
### Cool points
	Go has tools to format your go files (go fmt, see `go doc gofmt`), and it has a tool to check for errors
    that might not get found when compiling (go vet, see `go doc vet`).
