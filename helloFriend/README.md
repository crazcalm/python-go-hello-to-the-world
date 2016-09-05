# HelloFriends

## helloFriends.py
### Dictionary
	A *mapping* object maps *hashable* values to arbitrary objects.
    Mappings are mutable objects. See interactive help (DICTIONARIES).

### isinstance
	Is a useful way of checking if an object is of a certain type.
    See interactive help (isinstance)
### Exceptions
	Exceptions are raised, and python has a number of builtin exceptions that you can choose
    from, but, if you want, you can always make your own.See https://docs.python.org/3/library/exceptions.html?highlight=baseexception for the information about python's builtin exceptions.

### Testing
	Unittest, the testing library in python's standard library, is amazing! It has
    everything that you would every want or need in a generic testing framework. See https://docs.python.org/3/library/unittest.html?highlight=testing for more information about how to use it.

### namedTuples
	Are tuples that have names for their items. I like using namedtuples for clarity. For instruction on how to use them, see the interactive help (collections.namedtuple)

## Cool points:
	- The python unittest framework has the ability to capture standard output so that you can test against it. When I first learned about this, my mind was blown.

## helloFriends.go
### map
	Maps are the hash tables of Go. They are unordered collections of key/value pairs in which all the keys are
    distinct, and the value associated with a given key can be retrieved, updated, or removed. The keys have to
    be hashable and the same type. Creating a map: `name := make(map[type1]type2)` or
    `name := map[type1]type2{type1a: type2a, ..., type1n:type2n}`.

	- For more information on "make" see `go doc builtin.make`

### range
	This is the function used to interate over iterable objects in Go. When iterating over a slice, range returns two
    values: index and value. When iterating over maps, range returns two values: key and value. Basic usage:
    `returned1, returned2 := range slice/map {/*do stuff*/}`

### fmt.Sprintf
	This is what you use to fotmate strings. Go does have a string package, but it has nothing for formatting
    strings. See `go doc fmt.Sprintf` and `go doc strings`

### append
	This is a builtin function used to add items to slices. See go doc builtin.append