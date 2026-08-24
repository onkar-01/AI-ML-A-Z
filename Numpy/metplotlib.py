import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

expences = pd.DataFrame([
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
ax.hist(expences["amount"], bins=6, color="#ff0000", edgecolor="#fff")
ax.set_xlabel("Amount (₹)")
ax.set_ylabel("Count")
ax.set_title("Distribution of Expense Amounts")
fig.savefig("hist_matplotlib.png")