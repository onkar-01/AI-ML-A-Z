import pandas as pd

expences = pd.DataFrame([
    {"category": "food",     "amount": 250,   "city": "Delhi"},
    {"category": "travel",   "amount": 1200,  "city": "Mumbai"},
    {"category": "shopping", "amount": 500,   "city": "Delhi"},
    {"category": "travel",   "amount": None,  "city": "Mumbai"},   # missing!
])

budgets = pd.DataFrame([
    {"category": "food", "monthly_budget": 1000},
    {"category": "travel", "monthly_budget": 3000},
])
merged = expences.merge(budgets, on="category",how="left")
pivot = expences.pivot_table(values="amount",index="category",columns="city")
print(merged);