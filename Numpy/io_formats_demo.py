import pandas as pd

expenses = pd.DataFrame([
    {"category": "food",     "amount": 250,   "city": "Delhi"},
    {"category": "travel",   "amount": 1200,  "city": "Mumbai"},
    {"category": "shopping", "amount": 500,   "city": "Delhi"},
    {"category": "travel",   "amount": 1090,  "city": "Mumbai"}, 
    {"category": "food",     "amount": 290,   "city": "Delhi"},
    {"category": "travel",   "amount": 1900,  "city": "Mumbai"},
    {"category": "shopping", "amount": 1000,   "city": "Delhi"},
    {"category": "travel",   "amount": 1230,  "city": "Mumbai"}, 
])
expenses.index = range(1, len(expenses) + 1)
expenses.to_csv("expenses.csv",index=True,index_label="sl no.")
expenses.to_json("expenses.json",orient="records",indent=2)
expenses.to_parquet("expenses.parquet")