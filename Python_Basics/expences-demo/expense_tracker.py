import argparse           # command-line argument parsing ke liye
import json                # expenses ko JSON file mein save/load karne ke liye
import sys                 # sys.exit() use karne ke liye (program exit karna)
from dataclasses import dataclass, asdict   # dataclass -> simple class banane ke liye, asdict -> dataclass ko dict mein convert karta hai
from pathlib import Path   # file paths handle karne ke liye (OS-independent)

DEFAULT_FILE = Path(__file__).parent / "expenses.json"
# is script ke folder ke andar "expenses.json" ka default path bana rahe hain


@dataclass
class Expense:              # ek single expense entry ka structure
    category: str            # e.g. "Food", "Rent"
    amount: float             # e.g. 250.0
    note: str = ""             # optional note, default empty string


class ExpenseTracker:
    def __init__(self, filepath):
        self.filepath = Path(filepath)   # jo file path diya gaya usse Path object banate hain
        self.expenses = self._load()      # object banate hi file se purane expenses load kar lete hain

    def _load(self):
        if not self.filepath.exists() or self.filepath.stat().st_size == 0:
            return []
            # agar file exist nahi karti YA empty (0 bytes) hai, to khaali list return karo
            # (empty file par json.load() error deta, isliye ye check zaroori hai)
        with open(self.filepath) as f:
            data = json.load(f)          # file se JSON data (list of dicts) parse karo
        return [Expense(**e) for e in data]
        # har dict ko Expense object mein convert kar rahe hain (**e = dict unpack karke fields fill karta hai)

    def save(self):
        with open(self.filepath, "w") as f:
            json.dump([asdict(e) for e in self.expenses], f, indent=2)
            # sabhi Expense objects ko wapas dict mein convert karke JSON file mein likh rahe hain
            # indent=2 -> file readable format mein save hoti hai

    def add_expense(self, category, amount, note=""):
        self.expenses.append(Expense(category, amount, note))
        # naya Expense object bana kar list mein add kar diya
        self.save()
        # add karte hi file mein turant save kar do (taaki data lost na ho)

    def total(self):
        return sum(e.amount for e in self.expenses)
        # sabhi expenses ke amount ka sum nikal rahe hain

    def total_by_category(self, category):
        return sum(e.amount for e in self.expenses if e.category == category)
        # sirf usi category ke expenses ka sum (filter karke)

    def list_expenses(self, category=None):
        if category:
            return [e for e in self.expenses if e.category == category]
            # agar category diya gaya hai to sirf usi category ke expenses return karo
        return self.expenses
        # nahi to sabhi expenses return karo


def build_parser():
    parser = argparse.ArgumentParser(prog="expense_tracker", description="Track expenses by category")
    # main parser banaya - ye "-h" pe help aur program ka naam/description dikhata hai

    parser.add_argument("-f", "--file", default=DEFAULT_FILE, help="path to the expenses JSON file")
    # global option: -f/--file se koi bhi custom JSON file specify kar sakte ho

    subparsers = parser.add_subparsers(dest="command")
    # subcommands ke liye container banaya (jaise git ke "add", "commit" commands hote hain)
    # args.command mein pata chalega user ne kaunsa subcommand choose kiya

    add_parser = subparsers.add_parser("add", help="add a new expense")
    # "add" subcommand define kiya
    add_parser.add_argument("category", help="expense category, e.g. Food")
    # positional argument -> "add Food 250" mein "Food" yahan aayega
    add_parser.add_argument("amount", type=float, help="expense amount")
    # positional argument -> "250" yahan aayega, type=float se automatically number mein convert hoga
    add_parser.add_argument("-n", "--note", default="", help="optional note")
    # optional flag -> "-n 'lunch'" jaisa use hota hai

    list_parser = subparsers.add_parser("list", help="list expenses")
    # "list" subcommand define kiya
    list_parser.add_argument("-c", "--category", help="filter by category")
    # optional filter -> "-c Food" se sirf Food ke expenses dikhenge

    total_parser = subparsers.add_parser("total", help="show total expenses")
    # "total" subcommand define kiya
    total_parser.add_argument("-c", "--category", help="totals for a single category")
    # optional filter -> "-c Food" se sirf Food ka total dikhega

    return parser
    # complete parser wapas bhej diya


def main():
    parser = build_parser()       # parser taiyaar kiya
    args = parser.parse_args()    # terminal se diye gaye arguments parse kiye

    if args.command is None:
        parser.print_help()        # agar koi command hi nahi diya (sirf "python expense_tracker.py") to help dikhao
        sys.exit(0)                 # aur program yahin band kar do (exit code 0 = success)

    tracker = ExpenseTracker(args.file)
    # ExpenseTracker object banaya, jo file se purana data load kar lega

    if args.command == "add":
        tracker.add_expense(args.category, args.amount, args.note)
        # naya expense add karo aur file mein save karo
        print(f"Added {args.category}: ₹{args.amount}")
        # confirmation message print karo

    elif args.command == "list":
        expenses = tracker.list_expenses(args.category)
        # saare (ya filtered) expenses nikalo
        if not expenses:
            print("No expenses found.")
            # agar list khaali hai to bata do
        for e in expenses:
            note = f" ({e.note})" if e.note else ""
            # agar note hai to use bracket mein dikhao, warna kuch mat dikhao
            print(f"{e.category}: ₹{e.amount}{note}")
            # har expense ek line mein print karo

    elif args.command == "total":
        if args.category:
            print(f"Total for {args.category}: ₹{tracker.total_by_category(args.category)}")
            # ek specific category ka total dikhao
        else:
            print(f"Total expenses: ₹{tracker.total()}")
            # sabhi expenses ka grand total dikhao


if __name__ == "__main__":
    main()
    # ye check ensure karta hai ki main() sirf tabhi chale jab file directly run ki jaaye
    # (agar kahin import ki jaaye to main() apne aap nahi chalega)
