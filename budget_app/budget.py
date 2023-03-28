class Category:
    withdrawals = 0

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
      self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        total = 0
        for item in self.ledger:
            total += item['amount']
        if float(amount) <= total:
            return True
        else:
            return False

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            d = {"amount": float(-amount), "description": description}
            self.ledger.append(d)
            self.withdrawals += amount
            return True
        return False

    def get_balance(self):
      bal = 0
      for item in self.ledger:
        bal += float(item["amount"])
      return bal

    def transfer(self, amount, category):
        if self.check_funds(amount):
            d1 = {"amount": float(-amount), "description": f'Transfer to {category.name}'}
            self.ledger.append(d1)
            d2 = {"amount": float(amount), "description": f'Transfer from {self.name}'}
            category.ledger.append(d2)
            self.withdrawals += amount
            return True
        return False
      
    def __str__(self):
      title_name = f"{self.name:*^30}\n"
      total_items = ""
      total_amount = 0
      for item in self.ledger:
        total_items += f"{item['description'] [:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
        total_amount += item["amount"]
      return title_name  + total_items + f"Total: {total_amount}"

def create_spend_chart(categories):
    category = Category
    expenditure = {}
    pct_exp = {}
    total_exp = 0
  
    expenditure = {cat.name: cat.withdrawals for cat in categories}
    total_exp = sum(cat.withdrawals for cat in categories)
    pct_exp = {key: value/total_exp*100 for key, value in expenditure.items()}
    row = "Percentage spent by category\n" + "\n".join([f"{str(i).rjust(3)}|" + "".join([" o " if j > i else "   " for j in pct_exp.values()]) + " " for i in range(100, -1, -10)]) + "\n    ----------"

    length_list = []
    for category in categories:
        length_list.append(len(category.name))
    max_len = max(length_list)

    for i in range(0, max_len):
        row += "\n" + "    "
        for j in range(len(categories)):
            if i < length_list[j]:
                row += " " + categories[j].name[i] + " "
            else:
                row += " " * 3
        row += " "

    return row
