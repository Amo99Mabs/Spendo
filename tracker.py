expenses = []

# 🎉 Initial Welcome Message
print("\n🎉 Welcome to Spendo: Your Personal Expense Tracker 🎉\n")

def printMenu():
    print("==================== Spendo Expense Tracker ====================")
    print("Please choose from one of the following options...")
    print("1. ➕ Add a new Expense")
    print("2. 🗑️ Remove an Expense")
    print("3. 📋 List All Expenses")
    print("===============================================================\n")

def listExpenses():
    print("\n📋 Here is a list of your expenses...")
    print("------------------------------------")
    if not expenses:
        print("You currently have no recorded expenses.\n")
    else:
        for counter, expense in enumerate(expenses):
            print(f"#{counter} - R{expense['amount']} - {expense['category']}")
        total = sum(float(exp['amount']) for exp in expenses)
        print(f"\n💰 Total Expenses: R{total:.2f}\n")

def removeExpenses():
    while True:
        listExpenses()
        print("🗑️ What expense would you like to remove? (Enter the number)")
        try:
            expenseToRemove = int(input("> "))
            del expenses[expenseToRemove]
            print("✅ Expense successfully removed!\n")
            break
        except (ValueError, IndexError):
            print("\n😅 Hmm, that wasn’t one of the options. Let’s try again!\n")

def addExpense(amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)
    print(f"✅ Expense of R{amount} for '{category}' successfully added!\n")

# 🚀 Main Program Loop
if __name__ == "__main__":
    while True:
        printMenu()
        optionSelected = input("> ")

        if optionSelected == "1":
            print("💸 How much was this expense?")
            amountToAdd = input("> ")
            print("🏷️ What category was this expense?")
            category = input("> ")
            addExpense(amountToAdd, category)

        elif optionSelected == "2":
            removeExpenses()

        elif optionSelected == "3":
            listExpenses()

        else:
            print("\n😅 Hmm, that wasn’t one of the options. Let’s try again!\n")
