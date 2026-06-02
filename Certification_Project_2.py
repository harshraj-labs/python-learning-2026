# Building a Budget App
class Category:
    
    def __init__(self,name):
        self.name = name
        self.ledger = []
    
    def deposit(self,amount,description = ''):
        self.ledger.append({'amount':amount, 'description': description})

    def withdraw(self,amount,description =''):
        if self.check_funds(amount):
            self.ledger.append({'amount':-amount, 'description':description})
            return True
        return False

    def get_balance(self):
        total = 0
        for items in self.ledger:
            total += items['amount']    
        
        return total

    def check_funds(self,amount):
        return self.get_balance() >= amount

    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {category.name}')
            category.deposit(amount,f'Transfer from {self.name}')
            return True
        
        return False

    def __str__(self):
        output = self.name.center(30,'*') + '\n'

        for item in self.ledger:
            desc = item['description'][:23]
            amt = f"{item['amount']:.2f}"

            output += f"{desc:<23}{amt:>7}\n"
        
        output += f"Total: {self.get_balance()}"
        return output

def create_spend_chart(categories):
    spent = []
    total_spent = 0

    for category in categories:
        category_spent = 0

        for item in category.ledger:
            if item['amount']<0:
                category_spent += -item['amount']
    
        spent.append(category_spent)
        total_spent += category_spent
    
    percentage = []

    for amount in spent:
        percentage.append(int((amount/total_spent)*100)//10*10)
    
    chart = "Percentage spent by category\n"
    for level in range(100, -1, -10):
        chart += f"{level:>3}| "

        for percent in percentage:
            if percent >= level:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"


    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"


    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)

    for i in range(max_length):
        chart += "     "

        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "

        if i != max_length - 1:
            chart += "\n"

    return chart.rstrip("\n")

