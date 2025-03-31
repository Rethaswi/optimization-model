import subprocess
import sys

# Ensure required packages are installed
subprocess.check_call([sys.executable, "-m", "pip", "install", "pulp", "pandas"])

import pulp
import pandas as pd

# Define the Linear Programming Problem
model = pulp.LpProblem("Profit_Maximization", pulp.LpMaximize)

# Decision Variables
product_A = pulp.LpVariable("Product_A", lowBound=0, cat='Continuous')
product_B = pulp.LpVariable("Product_B", lowBound=0, cat='Continuous')

# Objective Function (Profit Maximization)
profit_A = 50  # Profit per unit of Product A
profit_B = 40  # Profit per unit of Product B
model += profit_A * product_A + profit_B * product_B, "Total_Profit"

# Constraints
labor_hours_A = 2  # Labor hours required per unit of A
labor_hours_B = 3  # Labor hours required per unit of B
available_labor = 100  # Total available labor hours

material_A = 3  # Material required per unit of A
material_B = 2  # Material required per unit of B
available_material = 90  # Total available material

model += (labor_hours_A * product_A + labor_hours_B * product_B <= available_labor, "Labor_Constraint")
model += (material_A * product_A + material_B * product_B <= available_material, "Material_Constraint")

# Solve the Model
model.solve()

# Output the Results
print("Status:", pulp.LpStatus[model.status])
print("Optimal Production Plan:")
print(f"Product A: {product_A.varValue}")
print(f"Product B: {product_B.varValue}")
print("Total Profit:", pulp.value(model.objective))

# Store results in a DataFrame for better visualization
results = pd.DataFrame({
    'Variable': ['Product_A', 'Product_B', 'Total_Profit'],
    'Optimal Value': [product_A.varValue, product_B.varValue, pulp.value(model.objective)]
})
print(results)
