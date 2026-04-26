from utils import remove_balance, current_balance

def withdraw():
    global current_balance

    amount = int(input("Enter amount to withdraw: ₹"))

    if amount <= current_balance:
        remove_balance.append(amount)
        current_balance -= amount
        print(f"₹{amount} withdrawn successfully.")
    else:
        print("Insufficient balance.")