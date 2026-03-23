import csv
import matplotlib.pyplot as plt


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("Expense added successfully!")


def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            print("\nDate       | Category | Amount | Note")
            print("--------------------------------------")
            for row in reader:
                if len(row) == 4:
                    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    except FileNotFoundError:
        print("No expenses found.")


def total_expense():
    total = 0
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 4:
                    total += float(row[2])
        print("Total Expense:", total)
    except FileNotFoundError:
        print("No data found.")


def category_expense():
    data = {}
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 4:
                    category = row[1]
                    amount = float(row[2])
                    if category in data:
                        data[category] += amount
                    else:
                        data[category] = amount

        for category, amount in data.items():
            print(category, ":", amount)

    except FileNotFoundError:
        print("No data found.")


def plot_expense():
    data = {}
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 4:
                    category = row[1]
                    amount = float(row[2])
                    if category in data:
                        data[category] += amount
                    else:
                        data[category] = amount

        categories = list(data.keys())
        amounts = list(data.values())

        plt.bar(categories, amounts)
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.title("Expenses by Category")
        plt.show()

    except FileNotFoundError:
        print("No data to display.")


def main():
    while True:
        print("\n------ Expense Tracker ------")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category-wise Expense")
        print("5. Show Graph")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_expense()
        elif choice == "5":
            plot_expense()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


main()