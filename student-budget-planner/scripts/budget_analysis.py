import pandas as pd
import matplotlib.pyplot as plt

# Load budget Excel file
df = pd.read_excel("../data/sample_budget.xlsx")

# Show total spending by category
category_summary = df.groupby("Category")["Amount"].sum()

print("💰 Spending Summary:")
print(category_summary)

# Plot chart
category_summary.plot(kind="bar", title="Expenses by Category")
plt.ylabel("Amount (PKR)")
plt.show()
