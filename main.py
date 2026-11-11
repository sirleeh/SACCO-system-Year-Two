from member import Member
from staff import Staff
from account import Account, SavingsAccount, FixedDepositAccount
from savings import SavingsDeposit
from loan import Loan
from guarantor import Guarantor
from loan_payment import LoanPayment
from storage import Storage


# Helper functions to find objects in lists by their ID
def find_member(members, member_id):
    for member in members:
        if member.get_member_id() == member_id:
            return member
    return None


def find_staff(staff_list, staff_id):
    for staff in staff_list:
        if staff.get_staff_id() == staff_id:
            return staff
    return None


def find_account(accounts, account_id):
    for account in accounts:
        if account.get_account_id() == account_id:
            return account
    return None


def find_loan(loans, loan_id):
    for loan in loans:
        if loan.get_loan_id() == loan_id:
            return loan
    return None


# Load all records from JSON and create class objects
def load_all_data(storage):
    data = storage.load()

    # Set class counters to match existing records in JSON
    Member.count = len(data["members"])
    Staff.count = len(data["staff"])
    Account.count = len(data["accounts"])
    SavingsDeposit.count = len(data["savings"])
    Loan.count = len(data["loans"])
    Guarantor.count = len(data["guarantors"])
    LoanPayment.count = len(data["payments"])

    members = []
    staff_list = []
    accounts = []
    savings_list = []
    loans = []
    guarantors = []
    payments = []

    # Load Members
    for row in data["members"]:
        m = Member(
            row["first_name"],
            row["last_name"],
            row["gender"],
            row["phone"],
            row["national_id"],
            row["join_date"],
            row["member_id"]
        )
        m.set_status(row["status"])
        members.append(m)

    # Load Staff
    for row in data["staff"]:
        st = Staff(
            row["first_name"],
            row["last_name"],
            row["gender"],
            row["phone"],
            row["national_id"],
            row["position"],
            row["staff_id"]
        )
        staff_list.append(st)

    # Load Accounts
    for row in data["accounts"]:
        member = find_member(members, row["member_id"])
        if row["account_type"] == "Savings":
            acc = SavingsAccount(member, row["date_opened"], row["account_id"])
        else:
            acc = FixedDepositAccount(member, row["date_opened"], row["account_id"])

        if row["balance"] > 0:
            acc.deposit(row["balance"])
        accounts.append(acc)

    # Load Savings Deposits
    for row in data["savings"]:
        account = find_account(accounts, row["account_id"])
        sd = SavingsDeposit(
            account,
            row["amount_saved"],
            row["payment_method"],
            row["savings_date"],
            row["savings_id"]
        )
        savings_list.append(sd)

    # Load Loans
    for row in data["loans"]:
        member = find_member(members, row["member_id"])
        loan = Loan(
            member,
            row["loan_amount"],
            row["payment_period"],
            row["payment_method"],
            row["loan_purpose"],
            row["start_date"],
            row["loan_id"]
        )
        loans.append(loan)

    # Load Guarantors
    for row in data["guarantors"]:
        member = find_member(members, row["member_id"])
        loan = find_loan(loans, row["loan_id"])
        g = Guarantor(
            member,
            loan,
            row["amount_guaranteed"],
            row["guarantor_id"]
        )
        loan.add_guarantor(g)
        guarantors.append(g)

    # Restore Loan approval or rejection status
    for row in data["loans"]:
        loan = find_loan(loans, row["loan_id"])
        staff = find_staff(staff_list, row["approved_by"])
        if row["status"] == "Approved" or row["status"] == "Cleared":
            loan.approve(staff)
        elif row["status"] == "Rejected":
            loan.reject(staff)

    # Load Loan Payments
    for row in data["payments"]:
        loan = find_loan(loans, row["loan_id"])
        lp = LoanPayment(
            loan,
            row["amount_paid"],
            row["payment_method"],
            row["payment_date"],
            row["payment_id"]
        )
        lp.make_payment()
        payments.append(lp)

    return members, staff_list, accounts, savings_list, loans, guarantors, payments


# Convert a list of objects into a list of dictionaries
def to_dict_list(object_list):
    records = []
    for obj in object_list:
        records.append(obj.to_dict())
    return records


# Save all object lists to the JSON file
def save_all_data(storage, members, staff_list, accounts, savings_list, loans, guarantors, payments):
    data = {
        "members": to_dict_list(members),
        "staff": to_dict_list(staff_list),
        "accounts": to_dict_list(accounts),
        "savings": to_dict_list(savings_list),
        "loans": to_dict_list(loans),
        "guarantors": to_dict_list(guarantors),
        "payments": to_dict_list(payments)
    }
    storage.save(data)


# Display records in the terminal when main.py is run directly
if __name__ == "__main__":
    storage = Storage("sacco_data.json")
    members, staff_list, accounts, savings_list, loans, guarantors, payments = load_all_data(storage)

    print("--- MEMBERS ---")
    for member in members:
        print(member)

    print("\n--- STAFF ---")
    for staff in staff_list:
        print(staff)

    print("\n--- ACCOUNTS ---")
    for account in accounts:
        print(account)

    print("\n--- LOANS ---")
    for loan in loans:
        print(loan)
