def expences_by_category(expences,category):
    matched = [e["amount"] for e in expences if e["category"] == category] 
    return sum(matched)
