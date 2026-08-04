import pandas as pd  # Import pandas library and give it the short name pd.

data = {  # Create data using a dictionary.
    "name": ["Kiran", "Asha", "Rahul", "Meena"],  # Name column values.
    "age": [30, 25, 28, 22],  # Age column values.
    "salary": [50000, 45000, 60000, 40000],  # Salary column values.
}

df = pd.DataFrame(data)  # Convert dictionary data into a pandas DataFrame/table.

print(
    df.sort_values("salary")
)  # Sort rows by salary from low to high and print the result.

print(
    df.sort_values("salary", ascending=False)
)  # Sort rows by salary from high to low and print the result.
