# groupby() is used to group same category values together.

import pandas as pd  # Import pandas library and give it the short name pd.

data = {  # Create data using a dictionary.
    "department": ["IT", "HR", "IT", "HR", "Sales"],  # Department column values.
    "name": ["Kiran", "Asha", "Rahul", "Meena", "Dev"],  # Employee name column values.
    "salary": [50000, 40000, 60000, 45000, 30000],  # Salary column values.
}

df = pd.DataFrame(data)  # Convert dictionary data into a pandas DataFrame/table.

print(
    df.groupby("department")["salary"].sum()
)  # Group by department and print total salary for each department.

# Average
print(
    df.groupby("department")["salary"].mean()
)  # Group by department and print average salary for each department.

print(
    df.groupby("department")["salary"].max()
)  # Group by department and print highest salary in each department.

print(
    df.groupby("department")["name"].count()
)  # Group by department and print number of employees in each department.
