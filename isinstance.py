def string_or_not(value):
    result = isinstance(value, str)
    print(f"is {value}; represents a string class: {result}")
    response = ("no", "yes")[result]
    print(response)


string_or_not(123)
string_or_not("Hello World")
ыыыы