# How to Parse a String to a Float or Integer

string = "12345"
print(type(string))

int_str = int(string)
print(type(int_str), int_str)

float_str = float(string)
print(type(float_str), float_str)

int_float_str = int(float(string))
print(type(int_float_str), int_float_str)

set_str = set(string)
print(type(set_str), set_str)

list_str = list(string)
print(type(list_str), list_str)

tuple_str = tuple(string)
print(type(tuple_str), tuple_str)