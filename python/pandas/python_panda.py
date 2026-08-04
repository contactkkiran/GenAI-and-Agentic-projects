# Series  # One column in pandas.
# DataFrame  # A table with rows and columns.

import pandas as pd  # Import pandas library and give it the short name pd.

data = {  # Create data using a dictionary.
    "name": ["kiran", "Appu", "adi"],  # name column values.
    "age": [46, 20, 22],  # age column values.
    "city": ["hyerabad", "vizag", "Bhiravapatnam"],  # city column values.
}

df = pd.DataFrame(data)  # Convert dictionary data into a pandas DataFrame/table.
print(df)  # Print the full DataFrame.

print(
    "Prints all rows", df.head()
)  # Print first 5 rows. Here data has only 3 rows, so it prints all rows.

print(df.head(2))  # Print only the first 2 rows.

print(df.columns)  # Print all column names.

print(df["name"])  # Print only the name column. This is a Series.

print(df[["name", "city"]])  # Print multiple columns: name and city.

print(df.iloc[2])  # Print row at index position 2.
print(df.iloc[0:2])  # Print rows from index 0 to before index 2.
print(
    df["age"] > 20
)  # Check each age. Returns True if age is greater than 20, else False.

data = {  # Create new dictionary data.
    "name": ["Kiran", "Asha", "Rahul", "Meena"],  # name column values.
    "age": [30, 25, 28, 22],  # age column values.
    "salary": [50000, 45000, 60000, 40000],  # salary column values.
}

df = pd.DataFrame(data)  # Convert new dictionary data into a DataFrame.

print(df)  # Print full DataFrame.
print(
    df.head()
)  # Print first 5 rows. Here data has only 4 rows, so it prints all rows.
print(df["name"])  # Print only the name column.
print(df[["name", "salary"]])  # Print multiple columns: name and salary.
print(df[df["salary"] > 45000])  # Print only rows where salary is greater than 45000.

df["bonus"] = df["salary"] * 0.10  # Add a new bonus column with 10% of salary.

print(df)  # Print DataFrame after adding bonus column.


# practice code

data = {  # Create data using a dictionary.
    "name": ["Kiran", "Asha", "Rahul", "Meena"],  # Name column values.
    "age": [30, 25, 28, 22],  # Age column values.
    "salary": [50000, 45000, 60000, 40000],  # Salary column values.
}

df = pd.DataFrame(data)  # Convert dictionary into a pandas DataFrame.
df = pd.DataFrame(
    data
)  # This line repeats the same DataFrame creation. You can remove this duplicate line.

print(df[df["age"] > 25])  # Print rows where age is greater than 25.
print(df[df["salary"] >= 50000])  # Print rows where salary is 50000 or more.
print(df[df["name"] == "Asha"])  # Print rows where name is exactly "Asha".
print(df[df["age"] != 22])  # Print rows where age is not equal to 22.

print(
    df[(df["age"] > 25) & (df["salary"] > 50000)]
)  # AND: print rows where age > 25 and salary > 50000.
print(
    df[(df["age"] > 25) | (df["salary"] > 50000)]
)  # OR: print rows where age > 25 or salary > 50000.
