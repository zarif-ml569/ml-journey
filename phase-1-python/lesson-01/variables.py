age = 23
print(f"age = {age}")
print(f"id(age) = {id(age)}")
print(f"type(age) = {type(age)}")

age = 24
print(f"After reassigning: id(age) = {id(age)}")

numbers = [1,2,3]
print(f"Before: id(numbers) = {id(numbers)}")
numbers.append(4)
print(f"After: id(numbers) = {id(numbers)}")
print(f"numbers = {numbers}")

list_a = [1,2,3]
list_b = list_a
list_b.append(99)
print(f"list_a = {list_b}")
print(f"list_b = {list_b}")
print(f"Same object? {id(list_a) == id(list_b)}")

list_c = [1, 2, 3]
list_d = list_c.copy()
list_d.append(99)
print(f"list_c = {list_c}")
print(f"list_d = {list_d}")
print(f"Same object? {id(list_c) == id(list_d)}")
