from check_balance import balance
from deposit import deposit
from withdrawal import withdraw
from statement import mini_statement

def ATM():
    print("\n" + "═" * 50)
    print(f"{'WELCOME TO ATM MACHINE':^50}")
    print("═" * 50)

    while True:
        print("\n  [1] Display Balance")
        print("  [2] Withdraw Money")
        print("  [3] Deposit Money")
        print("  [4] Mini Statement")
        print("  [5] Exit")

        choice = input("  Select an option : ")

        if choice == "1": balance()
        elif choice == "2": withdraw()
        elif choice == "3": deposit()
        elif choice == "4": mini_statement()
        elif choice == "5":
            print("\nThank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid option. choose from 1–5.")

ATM()