# helloFunctions!

## helloFunctions.py

### Functions signature:
    - `def func_name(param_1, ... param_n):`
    - Python uses spaces (instead of brackets) to define scope.
    - functions can return one or multiple values.
      - In the case that nothing is expicitly returned, then "None" is returned

### Formatting strings:
    There are a few ways to go about formating strings in Python, but the
    prefered way is the use the str.format method.

    - In Python's interactive help, see topics STRINGMETHODS and FORMATTING.

### Lists:
    Lists are mutable sequences, typically used to store collections of
    homogeneous items. For immutable sequences, see tuples.

    - In Python's interactive help, see topics LISTS and TUPLPES.
      - The TUPLES ducumentation is more informative...

### Cool Points:
    `if __name__ == "__main__":` Is called when you execute the file, but it 
     is not called when you import that file. For more details, see 
     https://docs.python.org/3/library/__main__.html

##helloFunctions.go

### Function signature
    - func funcName(param1 type1, ..., paramN typeN) (returnA typeA, ... returnZ typeZ){/*function body */}
        - Returning from a function is optional, and I have only seen the 
          parathesis around the return values when there is more than one
          return value.

      - Variable Declaration:
      	- The generic way to declare a variable is follow the below syntax:
      		- `var name type = expression`
      	- However, when you are within the scope of a function or a method, you may use the
      	  short hand version:
          	- `name := expression`
          	- The type of the variable is determined by the type of the expression
        - The name variable naming converntion in Go is to use CamelCase.

### Pointer
	I mentioned pointers because they exist in Go and you should know of them, but, in terms
    of this presentation, they are not important. For more quick tutorial on pointers in Go,
    see https://tour.golang.org/moretypes/1

### Cool Points
    - Must use whatever you import or declare!
    	- In Go, if you import or declare and object and do not use it, your code will not
    	  compile. However, if you have to import or declare something that you know that you
          are not going to use, then you can assign that object to `_` and Go will compile.
    - Go run vs go build
		- Go run will compile the program and then run it whereas Go build will complile the
		  program once and create a binary that you can execute. See `go doc build` for
          information about how to build binaries for multiple platforms.