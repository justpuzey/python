my_list = ["first","second","third","fourth"]
print(len(my_list))
my_list.remove("fourth") #remove() allows you to remove the first occurance of a value, rather than using the index

print(my_list)
print(my_list.pop(0))

print(my_list)
my_list.append("fifth")
my_list.insert(0,"sixth")
print(my_list)

print(sorted(my_list))#sorted() function allows you to sort your list alphabetically without permanently changing the order of your original list

my_list.sort(reverse=True)
print(my_list)

list_slice = my_list[0:3]
print(list_slice)

numbers = list(range(1,15,2))
print(numbers)
min = min(numbers)
max = max(numbers)
sum = sum(numbers)

print(sum)

#Checking to see if a value is in a list
all_toppings = ["pepperoni","sausage","bell pepper"]
requested_topping = 'mushrooms'
if requested_topping not in all_toppings:
    print(f"sorry, we do not have {requested_topping}.")
else:
    print(f"sure, we have {requested_topping}.")

requested_toppings = ["sausage","bell pepper","mushrooms"]
for topping in requested_toppings:
    if topping in all_toppings:
         print(f"add {topping}")
    else:
        print(f"{topping} not added")



