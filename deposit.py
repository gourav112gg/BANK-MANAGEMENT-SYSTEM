from utils import new_balance, current_balance

def deposit():
    global current_balance

    amount = int(input("Enter amount to deposit: ₹"))

    if amount > 0:
        new_balance.append(amount)
        current_balance += amount
        print(f"₹{amount} deposited successfully.")
    else:
        print("Invalid amount.")