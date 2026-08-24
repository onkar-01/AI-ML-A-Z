from dataclasses import dataclass

@dataclass
class Expense:
    category: str
    amount: float

class ExpenseTracker:
    def __init__(self):
        self.expences = []
    
    def add_expense(self, category, amount):
        self.expences.append(Expense(category,amount))
    
    def total_expense(self):
        return sum(e.amount for e in self.expences)
    
    

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense("food",250)
    tracker.add_expense("festival",2000)
    amount = [{"category":e.category,"amount":e.amount} for e in tracker.expences]
    print(amount)
    print(tracker.total_expense())