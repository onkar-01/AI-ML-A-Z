from data import expences
from expences_by_category import expences_by_category

if __name__ == "__main__":
    category = input("Enter the category of expences: ")
    totalExpences = expences_by_category(expences, category)
    print(f"Total Expences for {category}: ₹{totalExpences}")