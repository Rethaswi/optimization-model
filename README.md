# optimization-model
*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: TEMURA RETHASWI

*INTERN ID*: CT04WM103

*DOMAIN*: optimization model

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

#DESCRIPTION: The given Python script utilizes the PuLP library to solve a linear programming problem focused on profit maximization for a manufacturing company that produces two products, A and B. It begins by ensuring that the necessary libraries, pulp and pandas, are installed using subprocess.check_call(), making the script more robust and ensuring smooth execution. The optimization model is defined using pulp.LpProblem with the goal of maximizing profit. Two decision variables, product_A and product_B, represent the number of units to be produced and are defined using pulp.LpVariable with a lower bound of zero to ensure non-negative production values. The objective function aims to maximize profit, considering $50 profit per unit of Product A and $40 per unit of Product B, which is then added to the model. Constraints are introduced to limit production based on available labor and material resources. Specifically, Product A requires 2 labor hours and 3 material units per unit, while Product B requires 3 labor hours and 2 material units per unit. Given the total available labor hours of 100 and material units of 90, two constraints are imposed using the += operator in PuLP. The model is then solved using model.solve(), and its status is checked via pulp.LpStatus[model.status] to ensure a feasible solution is found. The optimal production values of Product A and Product B are extracted from product_A.varValue and product_B.varValue, respectively, and the maximum achievable profit is obtained using pulp.value(model.objective). These results are then printed and stored in a Pandas DataFrame for better visualization, making it easier to analyze the outcomes. The approach highlights how linear programming can be effectively utilized in business decision-making to allocate resources optimally and maximize profitability while considering operational constraints. This problem formulation can be extended to other industries and scenarios, such as supply chain management, workforce allocation, and financial planning, making linear programming a crucial tool in optimization. Additionally, the script structure makes it highly adaptable; constraints and objective functions can be modified to fit different business needs. By automating the installation of dependencies and maintaining a structured approach to defining and solving the optimization problem, the script ensures that users can quickly execute and interpret the results without needing extensive manual setup. The use of Pandas also facilitates potential extensions where the results can be further analyzed, stored, or visualized in graphical formats, allowing stakeholders to make data-driven decisions effectively. The modular nature of the script makes it easy to integrate into larger business applications, such as enterprise resource planning (ERP) systems or production scheduling software. Furthermore, this implementation of linear programming through PuLP exemplifies how Python can be leveraged for solving real-world optimization problems with minimal computational complexity. In practice, this approach can be scaled to accommodate multiple constraints, additional variables, and dynamic inputs, making it a powerful tool for strategic planning in manufacturing and operations research.

#OUTPUT:

![Image](https://github.com/user-attachments/assets/3e5d2145-b7e0-475c-a822-0134218c3e0d)
