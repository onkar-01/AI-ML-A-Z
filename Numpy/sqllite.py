import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:") # temporary in-memory database
cur = conn.cursor()

cur.execute("""
            CREATE TABLE expenses (
                id INTEGER PRIMARY KEY,
                category TEXT, amount REAL, city TEXT
                )""")
cur.execute("INSERT INTO expenses (category, amount, city) VALUES ('groceries', 250, 'Delhi')")
expenses = pd.read_csv("expenses.csv")

expenses.to_sql("expenses", conn, if_exists="append", index=False)

cur.execute("""
            CREATE TABLE budgets (
                category TEXT PRIMARY KEY, monthly_budget REAL
                )""")
cur.executemany(
    "INSERT INTO budgets (category, monthly_budget) VALUES (?, ?)",
    [("food", 1000), ("travel", 5000), ("shopping", 2000)],
)

cur.execute("SELECT * FROM expenses WHERE amount > 200")
print("expenses over 200:")
for row in cur.fetchall():
    print(row)

cur.execute("""
    SELECT category, SUM(amount) as total FROM expenses
    GROUP BY category ORDER BY total DESC""")
print("\ntotal by category:")
for row in cur.fetchall():
    print(row)

cur.execute("""
    SELECT e.category, e.amount, b.monthly_budget
    FROM expenses e LEFT JOIN budgets b ON e.category = b.category""")
print("\nexpenses with budgets:")
for row in cur.fetchall():
    print(row)
    
df = pd.read_sql("SELECT category, SUM(amount) as total FROM expenses GROUP BY category", conn)
print("\nDataFrame from SQL query:")
print(df)