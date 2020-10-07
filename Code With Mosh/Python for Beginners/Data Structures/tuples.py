my_tuple = ("Red", "Blue", "Green")
print(my_tuple)
# Tuples are imutable. This function destroys the original and recreates with additional element. Element must be followed by "," and surrounded in "()" to make it a tuple
my_tuple = my_tuple.__add__(("Purple",))
print(my_tuple)
# Recrete tuple using concatenation rather than __add__() function
my_tuple = ("Magenta",) + my_tuple
print(my_tuple)
# Tuples allow the ability to nest one Tuple inside another
my_tuple = my_tuple.__add__(("Yellow", ("Orange", "Black")))
print(my_tuple)
print(my_tuple[5][0])
