# Talking Points:

## helloWorld.py:

	Beautifully simple. No imports, no packages, just builtins.

##helloWorld.go

	Still simple, but there is some boilier plate.

	1. Each Go file has to have a package. Package "main" is special. It defines a
    standalone executable program, not a library.

	2. Go does not have function that allows you to print to screen. In order to 
	accomplish that, you must import the "fmt" package. The fmt package contains 
	functions for printing formatted output and scanning input.

	3. We create a function called "main" to run our program. This main function is 
	special because the "main" function gets called when we run a Go program.

### Cool Points:
	* "fmt.Println"
  		- In Go, encapulation (public vs private) is done by capitalizing or
		lowercasing the first letter of the name. So, "Println" is a public function in
		the fmt package.
