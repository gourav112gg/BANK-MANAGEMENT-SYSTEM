from utils import new_balance, remove_balance

def mini_statement():
    print("\n--- MINI STATEMENT ---")

    print("\nDeposits:")
    for i in new_balance:
        print(f"+ ₹{i}")

    print("\nWithdrawals:")
    for i in remove_balance:
        print(f"- ₹{i}")