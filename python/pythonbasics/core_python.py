# ===== LIST =====
# List is ordered, allows duplicates, and is mutable/changeable.

from optparse import Values  # Imported module item. Not used in this program.
from turtle import st  # Imported module item. Not used in this program.

bounding_box = [10, 20, 100, 200]  # List with x, y, width, height values.
bounding_box[0] = 15  # ✅ Works because list is mutable/changeable.


# ===== TUPLE =====
# Tuple is ordered, allows duplicates, but is immutable/not changeable.

bounding_box = (10, 20, 100, 200)  # Tuple with x, y, width, height values.
# bounding_box[0] = 15  # ❌ Error because tuple cannot be changed.


# ===== SET =====
# Set is unordered, does not allow duplicates, and stores only hashable values.

student1 = ("kiran", 46, "Hyderabad")  # Tuple with hashable values.

studentset = set(student1)  # Convert tuple into set.
print(studentset)  # Print set values. Order may change because set is unordered.


# ===== SET WITH UNHASHABLE LIST =====
# A list cannot be stored inside a set because list is unhashable/changeable.

student2 = (["kiran", "Male"], 46, "Hyderabad")  # Tuple contains a list inside it.

# studentset = set(student2)
# ❌ Error: unhashable type: 'list'
# Set needs hashable elements only.
# Tuple is OK only when all its contents are hashable.


# ===== ENUMERATE =====
# enumerate() gives index and value together.

names = ["AI", "ML", "DL"]  # List of names.

for index, name in enumerate(names):  # Loop with index and value.
    print(index, name)  # Print index and name.


# ===== DICTIONARY =====
# Dictionary stores data as key-value pairs.

student = {"name": "kiran", "age": 45}  # Create dictionary.

print(student.keys())  # Print all keys: name, age.
print(student.values())  # Print all values: kiran, 45.
print(student.items())  # Print key-value pairs.

for key, value in student.items():  # Loop through dictionary key-value pairs.
    print(key, ": ", value)  # Print each key and value.


# ===== COMPREHENSIVE PYTHON LOOPING TUTORIAL =====

print("\n" + "=" * 50)
print("1️⃣  FOR LOOP - Basic Iteration")
print("=" * 50)

# ===== FOR LOOP WITH LIST =====
fruits = ["apple", "banana", "cherry"]  # List of fruits.

for fruit in fruits:  # Loop through each fruit.
    print(f"Fruit: {fruit}")  # Print current fruit.


print("\n" + "=" * 50)
print("2️⃣  FOR LOOP with range()")
print("=" * 50)

# ===== RANGE LOOP =====
# range(5) gives 0, 1, 2, 3, 4.

for i in range(5):  # Loop from 0 to before 5.
    print(f"Number: {i}")  # Print current number.


# ===== RANGE WITH START, STOP, STEP =====
# range(2, 8, 2) gives 2, 4, 6.

print("\nEven numbers from 2 to 8:")

for i in range(2, 8, 2):  # Start at 2, stop before 8, jump by 2.
    print(i, end=" ")  # Print on same line.

print()  # Print new line.


print("\n" + "=" * 50)
print("3️⃣  FOR LOOP with enumerate() - Index + Value")
print("=" * 50)

# ===== ENUMERATE LOOP =====
colors = ["red", "green", "blue"]  # List of colors.

for index, color in enumerate(colors):  # Get index and color together.
    print(f"Index {index}: {color}")  # Print index and color.


print("\n" + "=" * 50)
print("4️⃣  FOR LOOP with zip() - Multiple Lists")
print("=" * 50)

# ===== ZIP LOOP =====
# zip() combines two or more lists together.

names_list = ["Alice", "Bob", "Charlie"]  # List of names.
ages_list = [25, 30, 35]  # List of ages.

for name, age in zip(names_list, ages_list):  # Take one name and one age together.
    print(f"{name} is {age} years old")  # Print combined data.


print("\n" + "=" * 50)
print("5️⃣  NESTED FOR LOOPS")
print("=" * 50)

# ===== NESTED LOOP =====
# Nested loop means loop inside another loop.

print("Multiplication Table (3x3):")

for i in range(1, 4):  # Outer loop: 1, 2, 3.
    for j in range(1, 4):  # Inner loop: 1, 2, 3.
        print(f"{i}×{j}={i*j}", end="  ")  # Print multiplication result.
    print()  # Move to next line after inner loop.


print("\n" + "=" * 50)
print("6️⃣  WHILE LOOP - Loop Until Condition is False")
print("=" * 50)

# ===== WHILE LOOP =====
# while loop runs as long as condition is True.

count = 0  # Starting value.

while count < 5:  # Run loop while count is less than 5.
    print(f"Count: {count}")  # Print current count.
    count += 1  # Increase count by 1.


print("\n" + "=" * 50)
print("7️⃣  BREAK - Exit Loop Early")
print("=" * 50)

# ===== BREAK =====
# break stops the loop immediately.

for num in range(10):  # Loop from 0 to 9.
    if num == 5:  # Check if number is 5.
        print(f"Found 5! Breaking out...")  # Print message.
        break  # Stop the loop.
    print(num, end=" ")  # Print number on same line.

print("\n(Loop stopped at 5)")  # Print final message.


print("\n" + "=" * 50)
print("8️⃣  CONTINUE - Skip Current Iteration")
print("=" * 50)

# ===== CONTINUE =====
# continue skips current loop round and moves to next round.

print("Printing even numbers only:")

for num in range(1, 11):  # Loop from 1 to 10.
    if num % 2 != 0:  # If number is odd.
        continue  # Skip odd number.
    print(num, end=" ")  # Print even number.

print()  # Print new line.


print("\n" + "=" * 50)
print("9️⃣  LOOP with ELSE - Executes if Loop Completes")
print("=" * 50)

# ===== LOOP ELSE =====
# else runs only if loop finishes without break.

for i in range(3):  # Loop from 0 to 2.
    print(f"Loop iteration {i}")  # Print current loop number.
else:
    print("✅ Loop completed successfully!")  # Runs because loop completed normally.


print("\n" + "=" * 50)
print("🔟  LIST COMPREHENSION - Compact Loop")
print("=" * 50)

# ===== LIST COMPREHENSION =====
# List comprehension creates a new list in one line.

squares = [x**2 for x in range(1, 6)]  # Create squares of 1 to 5.
print(f"Squares: {squares}")  # Print squares list.

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]  # Square only even numbers.
print(f"Even squares: {even_squares}")  # Print even squares list.


print("\n" + "=" * 50)
print("🔄  DICTIONARY LOOPING - Different Ways")
print("=" * 50)

# ===== DICTIONARY LOOPING =====
person = {"name": "Kiran", "age": 45, "city": "Hyderabad"}  # Create dictionary.

print("\nLoop through keys:")

for key in person:  # Loop through dictionary keys.
    print(key, end=" ")  # Print each key.

print()  # Print new line.

print("\nLoop through values:")

for value in person.values():  # Loop through dictionary values.
    print(value, end=" ")  # Print each value.

print()  # Print new line.

print("\nLoop through items (key + value):")

for key, value in person.items():  # Loop through key-value pairs.
    print(f"{key}: {value}")  # Print key and value.


print("\n" + "=" * 50)
print("💡  LOOP SUMMARY")
print("=" * 50)
