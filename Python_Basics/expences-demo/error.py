import json

def load_expenses(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data

def total_by_category(expenses, category):
    matched = [e["amount"] for e in expenses if e["category"] == category]
    return sum(matched)

if __name__ == "__main__":
    expenses = load_expenses("expenses.json")   # file doesn't exist yet!
    print(total_by_category(expenses, "food")) 