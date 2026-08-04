import pandas as pd  # Import pandas library and give it the short name pd.

data = {  # Create data using a dictionary.
    "name": ["Kiran", "Asha", "Rahul", "Meena"],  # Name column values.
    "age": [30, None, 28, 22],  # Age column values. None means missing value.
    "salary": [
        50000,
        45000,
        None,
        40000,
    ],  # Salary column values. None means missing value.
}

df = pd.DataFrame(data)  # Convert dictionary data into a pandas DataFrame/table.

print(df)  # Print the full DataFrame.

print(
    df.isnull
)  # This prints the isnull method reference, not the missing-value result.

print(df.isnull().sum())  # Count missing values in each column.

print(df.dropna())  # Print rows after removing rows that contain missing values.

df = df.fillna(10)  # Replace all missing values in the DataFrame with 10.
print(df)  # Print DataFrame after filling missing values with 10.

df["salary"] = df["salary"].fillna(30000)  # Fill missing salary values with 30000.
print("salary", df)  # Print DataFrame after trying to fill missing salary values.

df["salary"] = df["salary"].fillna(
    df["salary"].mean()
)  # Fill missing salary values with average salary.
print(df)  # Print final DataFrame.


# Small important note: after this line:
df = df.fillna(10)
# there are no missing values left. So these later lines will not change anything:
df["salary"] = df["salary"].fillna(30000)
df["salary"] = df["salary"].fillna(df["salary"].mean())
