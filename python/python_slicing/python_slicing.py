# What Is Slicing?
# Slicing means taking a part of a sequence.
# It works with strings, lists, tuples, NumPy arrays, and pandas data.
# Basic syntax: sequence[start:stop:step]
# start is included.
# stop is excluded.
# step means how many indexes to jump.

# Example 1: list slicing
nums = [10, 20, 30, 40, 50]  # Create a list of numbers.
print(nums[1:4])  # Print items from index 1 to before index 4: [20, 30, 40].

# Example 2: string slicing
text = "Python"  # Create a string.

print(text[0:2])  # Print from index 0 to before index 2: Py.
print(text[2:6])  # Print from index 2 to before index 6: thon.
print(text[:3])  # Print from start to before index 3: Pyt.
print(text[3:])  # Print from index 3 to the end: hon.
print(text[:])  # Print the full string: Python.

# Negative slicing examples
# Positive indexes:  P  y  t  h  o  n
#                   0  1  2  3  4  5
# Negative indexes: -6 -5 -4 -3 -2 -1

# print(text[-3:])  # Print from index -3 to the end: hon.
print(text[:-3])  # Print from start to before index -3: Pyt.
print(text[:3])  # Print from start to before index 3: Pyt.
print(text[-2:])  # Print from index -2 to the end: on.
print(text[:-4])  # Print from start to before index -4: Py.
print(text[-4:])  # Print from index -4 to the end: thon.

# Step slicing examples
print(text[::2])  # Print every 2nd character from start: Pto.
print(text[1::2])  # Print every 2nd character starting from index 1: yhn.
print(text[2::2])  # Print every 2nd character starting from index 2: to.
print(text[::-2])  # Print every 2nd character in reverse: nhy.
print(text[::2])  # Again print every 2nd character from start: Pto.

# These lines calculate slices but do not print them.
text[:2]  # From start to before index 2: Py.
text[2:]  # From index 2 to the end: thon.
text[2:5]  # From index 2 to before index 5: tho.
text[::2]  # Forward jump by 2: Pto.
text[::-2]  # Reverse jump by 2: nhy.
text[::-1]  # Full reverse: nohtyP.


nums = [1, 2, 3, 4, 5]  # Create a list of numbers.
nums[1:4] = [20, 30, 40]  # Replace index 1 to before index 4 with new values.
print(nums)  # Print the updated list: [1, 20, 30, 40, 5].

nums = [1, 2, 3, 4, 5]  # Create the list again.

del nums[2:]  # Delete everything from index 2 to the end.
print(nums)  # Print remaining list: [1, 2].

text = "I love Python"  # Create a string.
print(text.find("Python"))  # Find starting index of "Python": 7.
print(text.find("Java"))  # "Java" is not found, so result is -1.

filename = "report.pdf"  # Create a filename string.
print(filename.startswith("report"))  # Check if filename starts with "report": True.

filename = "report.pdf"  # Create a filename string.
print(filename.endswith(".pdf"))  # Check if filename ends with ".pdf": True.

text = "  Hello Python  "  # Create a string with spaces at start and end.
print(text.strip())  # Remove spaces from start and end: Hello Python.
print(text.lower())  # Convert all letters to lowercase.
print(text.upper())  # Convert all letters to uppercase.
print(text.strip().upper())  # First remove outside spaces, then convert to uppercase.

text = " banana "  # Create a string with spaces around banana.
print(text.count("a"))  # Count how many times "a" appears: 3.

print(text.strip())  # Remove spaces from start and end: banana.
text = "  Hello Python  "  # Store a new string in text.

text = "banana"  # Store banana in text.
text = text.replace("a", "o")  # Replace every "a" with "o".
print(text)  # Print updated text: bonono.

text = "I love Python"  # Create a sentence.
words = text.split()  # Split the sentence by spaces into a list.
print(words)  # Print list: ['I', 'love', 'Python'].

text = "apple,banana,mango"  # Create comma-separated text.
fruits = text.split(",")  # Split text by comma into a list.
print(fruits)  # Print list: ['apple', 'banana', 'mango'].

words = ["I", "love", "Python"]  # Create a list of words.
sentence = " ".join(words)  # Join words using a space between each word.
print(sentence)  # Print sentence: I love Python.

fruits = ["apple", "banana", "mango"]  # Create a list of fruits.
text = ", ".join(fruits)  # Join fruits using comma and space.
print(text)  # Print text: apple, banana, mango.

letters = ["P", "y", "t", "h", "o", "n"]  # Create a list of letters.
word = "".join(letters)  # Join letters with no space.
print(word)  # Print word: Python.

" ".join(["I", "am", "Kiran"])  # Join using spaces: I am Kiran.
"-".join(["2026", "07", "27"])  # Join using hyphen: 2026-07-27.
"".join(["P", "y", "t", "h", "o", "n"])  # Join with no space: Python.
