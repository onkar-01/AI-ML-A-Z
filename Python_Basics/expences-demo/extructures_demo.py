from data import expences

expences.append({"amount":2000, "category":"Food"})

# first expences from dict
first_expences = expences[0]
print(first_expences["category"]) # food
first_expences["amount"] = 100 # mutable it is updated
print(first_expences.get("amount")) # use get to prevent errors
print(expences[0])

# Set unique values no order guaranteed
categories = {e["category"] for e in expences}
print(categories)  # {'Rent', 'Food'} 


# touple : immutable, fixed shape, good for: "value never changes"
budget_range = (0,500)
low, high = budget_range;
print(low,high)

try:
    budget_range[0] = 1000
except TypeError as e:
    print(f"Tuples are immutable : {e}")

# Dict : key-value pair used to 
