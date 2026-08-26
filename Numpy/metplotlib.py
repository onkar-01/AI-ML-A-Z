import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

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

# matplotlib raw histogram
fig, ax = plt.subplot(figsize=(6,4))
ax.hist(expenses["amount"], bins=6, color="#ff0000", edgecolor="#fff")
ax.set_xlabel("Amount (₹)")
ax.set_ylabel("Count")
ax.set_title("Distribution of Expense Amounts")
fig.savefig("hist_matplotlib.png")

# seaborn histogram
total = expenses.groupby("category")["amount"].sum().reset_index()
fig2, ax2 = plt.subplot(figsize=(6,4))
sns.barplot(data=total,x="category",y="amount",hue="category",ax=ax2,legend=False)
ax2.set_title("Total spend by Category")
fig2.savefig("bar_seaborn.png")
plt.show()


total2 = expenses.groupby("city")["amount"].sum().reset_index()
fig3, ax3 = plt.subplots(figsize=(6,4))
sns.barplot(data=total2,x="city",y="amount",hue="city",ax=ax3,legend=False)
ax3.set_title("Total spend by city")
fig3.savefig("bar_city_seaborn.png")
plt.show()