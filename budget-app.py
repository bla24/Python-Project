# Build a Budget App
# A simple budget app that tracks spending in different categories and can show the relative spending percentage on a graph.

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        title = self.name.center(30, '*')
        lines = ""
        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"[:7]
            lines += f"{description:<23}{amount:>7}\n"
        total = self.get_balance()
        return f"{title}\n{lines}Total: {total}"

def create_spend_chart(categories):
    # Total spent per category (withdrawals only, stored as negative amounts)
    spent = []
    for category in categories:
        total = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spent.append(total)

    total_spent = sum(spent)

    # Percentage of the total, rounded down to the nearest 10
    percentages = [int((s / total_spent) * 100) // 10 * 10 for s in spent]

    chart = "Percentage spent by category\n"

    # Y-axis labels and bars
    for level in range(100, -1, -10):
        chart += f"{level:>3}|"
        for p in percentages:
            chart += " o " if p >= level else "   "
        chart += " \n"

    # Horizontal line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Vertical category names
    names = [category.name for category in categories]
    longest = max(len(name) for name in names)
    for i in range(longest):
        chart += "     "
        for name in names:
            chart += (name[i] if i < len(name) else " ") + "  "
        if i < longest - 1:
            chart += "\n"

    return chart
        


