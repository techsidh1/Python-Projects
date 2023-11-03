def get_user_info():
    """
        input user details 
    """
    print("Welcome to the PyPy World Bank")
    name = input("Enter your name: ")
    saving = int(input("Enter a initial amount to set up your saving account: "))
    checking = int(input("Enter a initial amount to set up your checking account: "))

    back_account = {
        "Name": name,
        "Saving": saving,
        "Checking": checking

    }

    return back_account


def make_deposites(bank_account, account_type, deposite_amount):
    """
        Add money to the account
    """
    bank_account[account_type] += deposite_amount
    print(f"\nDeposited ${deposite_amount} into {bank_account['Name']}'s {account_type.lower()} account")


def make_withdrawal(bank_account, account_type, withdrawal_amount):
    if bank_account[account_type] - withdrawal_amount  >= 0:
        bank_account[account_type] -= withdrawal_amount
        print(f"\nWithdraw of ${withdrawal_amount} from {bank_account['Name']}'s {account_type.lower()}")
    else:
        print(f"You can not withdraw ${withdrawal_amount}. Your current balance is low!")


def display_account_details(bank_account):
    print("\nCurrent Account Details")
    for key, value in bank_account.items():
        if key == 'Name':
            print(f"{key} : {value}")    
        else:
            print(f"{key} : ${value}")




my_account = get_user_info()
status = True 
while status:
    display_account_details(my_account)

    account_type = input("Which account would you like to access (saving / checking):  ").title()
    action = input("Would you like to withdraw or deposite: ").title()

    amount = float(input("Please enter your amount: "))

    if account_type == 'Saving' or account_type == 'Checking':
        if action == 'Deposite':
            make_deposites(my_account, account_type, amount)
        elif action == 'Withdrawal':
            make_withdrawal(my_account, account_type, amount)
        else:
            print("\nWe can not perfor this operation. Try Again!")

    else:
        print("\n Invaid enrty. Try again")

    user_choice = input("\nwould you like to continue (y/n):  ").lower()
    if user_choice != 'y':
        print("\nYour current Summary")
        display_account_details(my_account)
        print("\nThank You")

        status=False