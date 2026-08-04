import pandas as pd  # Import pandas library and give it the short name pd.

df = pd.read_csv(
    "employees.csv"
)  # Read employees.csv file and convert it into a DataFrame.
print(df)  # Print the employees DataFrame.

df.to_csv(
    "output.csv", index=False
)  # Save the DataFrame into output.csv without row index.

data = {  # Create employee data using a dictionary.
    "name": ["Kiran", "Asha", "Rahul"],  # Name column values.
    "age": [30, 25, 28],  # Age column values.
    "salary": [50000, 45000, 60000],  # Salary column values.
}

df = pd.DataFrame(data)  # Convert dictionary data into a DataFrame/table.
df.to_csv(
    "output2.csv", index=False
)  # Save this DataFrame into output2.csv without row index.

high_salary = df[
    df["salary"] > 45000
]  # Filter rows where salary is greater than 45000.
high_salary.to_csv(
    "high_salary_employees.csv", index=False
)  # Save filtered high salary rows to CSV.

data = {  # Create product data using a dictionary.
    "product": ["Laptop", "Mouse", "Keyboard"],  # Product column values.
    "price": [50000, 800, 1500],  # Price column values.
    "stock": [5, 20, 12],  # Stock column values.
}

df = pd.DataFrame(data)  # Convert product dictionary into a DataFrame/table.

df.to_csv(
    "products.csv", index=False
)  # Save product DataFrame to products.csv without row index.

products_df = pd.read_csv(
    "products.csv"
)  # Read products.csv and store it as a new DataFrame.

print(products_df)  # Print all products from products.csv.

expensive_products = products_df[
    products_df["price"] > 1000
]  # Filter products where price is greater than 1000.

expensive_products.to_csv(
    "expensive_products.csv", index=False
)  # Save expensive products to a new CSV file.

print(expensive_products)  # Print only expensive products.
