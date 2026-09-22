from member import Member
from account import Account
from savings import Savings
from loan import Loan
from guarantor import Guarantor
from staff import Staff
from loan_payment import LoanPayment

def main():
    while True:
        print("\n--- SACCO SYSTEM ---")
        print("1. Register Member")
        print("2. Create Account")
        print("3. Record Savings")
        print("4. Apply for Loan")
        print("5. Register Guarantor")
        print("6. Approve Loan (Staff)")
        print("7. Make Loan Payment")
        print("8. Check Account Balance")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            gender = input("Gender: ")
            phone = input("Phone no: ")
            national_id = input("National ID no: ")
            m = Member(first_name, last_name, gender, phone, national_id)
            m.register_member()

        elif choice == "2":
            member_id = input("Member ID: ")
            balance = int(input("Balance: "))
            account_type = input("Account Type: ")
            acc = Account(member_id, balance, account_type)
            acc.create_account()

        elif choice == "3":
            member_id = input("Member ID: ")
            account_id = input("Account ID: ")
            amount = int(input("Amount: "))
            method = input("Payment Method: ")
            s = Savings(member_id, account_id, amount, method)
            s.record_savings()

        elif choice == "4":
            member_id = input("Member ID: ")
            amount = int(input("Loan Amount: "))
            period = input("Period: ")
            method = input("Payment Method: ")
            purpose = input("Purpose: ")
            guarantor_id = input("Guarantor ID: ")
            l = Loan(member_id, amount, period, method, purpose, guarantor_id)
            l.apply_for_loan()

        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Guarantor Name: ")
            phone = input("Phone: ")
            amount = int(input("Amount Guaranteed: "))
            loan_id = input("Loan ID: ")
            g = Guarantor(member_id, name, phone, amount, loan_id)
            g.register_guarantor()

        elif choice == "6":
            staff_id = input("Staff ID: ")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            gender = input("Gender: ")
            position = input("Position: ")
            loan_id = input("Loan ID: ")
            st = Staff(staff_id, first_name, last_name, gender, position)
            st.approve_loan(loan_id)

        elif choice == "7":
            loan_id = input("Loan ID: ")
            amount = int(input("Amount: "))
            method = input("Payment Method: ")
            lp = LoanPayment(loan_id, amount, method)
            lp.make_payment()

        elif choice == "8":
            account_id = input("Account ID: ")
            acc = Account("")
            acc._Account__account_id = account_id
            acc.check_balance()

        elif choice == "0":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()