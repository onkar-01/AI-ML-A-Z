import pandas as pd

amount = pd.Series([20,30,40],name="amount")

data = pd.DataFrame([
    {"category": "food",     "amount": 250,  "city": "Delhi"},
    {"category": "travel",   "amount": 1200, "city": "Mumbai"},
    {"category": "food",     "amount": 90,   "city": "Delhi"},
    {"category": "shopping", "amount": 500,  "city": "Delhi"},
    {"category": "travel",   "amount": 300,  "city": "Mumbai"},
])

data["amount"]                     # column selection
data.loc[1]                          # row by label
data[data["amount"] > 200]        # boolean filter
data.groupby("category")["amount"].sum()

# print(data)
print(data["amount"])
print("\n")
print(data.loc[1])
print("\n")
print(data[data["amount"] > 200])