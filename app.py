from datetime import datetime
from member import Member
from staff import Staff
from account import SavingsAccount, FixedDepositAccount
from flask import Flask, render_template, request
from savings import SavingsDeposit
from loan import Loan
from guarantor import Guarantor
from loan_payment import LoanPayment
from storage import Storage
from main import (
    load_all_data,
    save_all_data,
    find_member,
    find_staff,
    find_account,
    find_loan
)

# Initialize Flask application and JSON storage
app = Flask(__name__)
storage = Storage("sacco_data.json")


# Home page route
@app.route("/")
def index():
    return render_template("index.html")


# Route to register and view SACCO members
@app.route("/members", methods=["GET", "POST"])
def members_page():
    members, staff_list, accounts, savings_list, loans, guarantors, payments = load_all_data(storage)

    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        gender = request.form["gender"]
        phone = request.form["phone"]
        national_id = request.form["national_id"]
        status = request.form["status"]
        today = str(datetime.now().date())

        # Create new Member object and save to JSON
        m = Member(first_name, last_name, gender, phone, national_id, today)
        m.set_phone(phone)
        m.set_status(status)
        members.append(m)
        save_all_data(storage, members, staff_list, accounts, savings_list, loans, guarantors, payments)

    return render_template("members.html", members=members)


# Route to register and view staff members
@app.route("/staff", methods=["GET", "POST"])
def staff_page():
    members, staff_list, accounts, savings_list, loans, guarantors, payments = load_all_data(storage)

    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        gender = request.form["gender"]
        phone = request.form["phone"]
        national_id = request.form["national_id"]
        position = request.form["position"]

        # Create new Staff object and save to JSON
        st = Staff(first_name, last_name, gender, phone, national_id, position)
        st.set_phone(phone)
        staff_list.append(st)
        save_all_data(storage, members, staff_list, accounts, savings_list, loans, guarantors, payments)

    return render_template("staff.html", staff_list=staff_list)


# Route to create accounts and make withdrawals
@app.route("/accounts", methods=["GET", "POST"])
def accounts_page():
    members, staff_list, accounts, savings_list, loans, guarantors, payments = load_all_data(storage)

    if request.method == "POST":
        action = request.form["action"]
        today = str(datetime.now().date())

        # Create a Savings or Fixed Deposit account
        if action == "create":
            member_id = request.form["member_id"]
            account_type = request.form["account_type"]
            member = find_member(members, member_id)

            if account_type == "Savings":
                acc = SavingsAccount(member, today)
            else:
                acc = FixedDepositAccount(member, today)

            accounts.append(acc)
            save_all_data(storage, members, staff_list, accounts, savings_list, loans, guarantors, payments)

        # Withdraw from an account (Polymorphism: FixedDepositAccount blocks withdrawal)
        elif action == "withdraw":
            account_id = request.form["account_id"]
            amount = int(request.form["amount"])
            account = find_account(accounts, account_id)
            account.withdraw(amount)
            save_all_data(storage, members, staff_list, accounts, savings_list, loans, guarantors, payments)

    return render_template("accounts.html", accounts=accounts, members=members)


# Route to record savings deposits
@app.route("/savings", methods=["GET", "POST"])
def savings_page():
    members, staff_list, accounts, savings_list, loans, guarantors, payments = load_all_data(storage)

    if request.method == "POST":
        account_id = request.form["account_id"]
        amount_saved = int(request.form["amount_saved"])
        payment_method = request.form["payment_method"]
        today = str(datetime.now().date())

        # Create SavingsDeposit object and update account balance
        account = find_account(accounts, account_id)
        sd = SavingsDeposit(account, amount_saved, payment_method, today)
        if sd.record_savings():
            savings_list.append(sd)
            save_all_data(storage, members, staff_list, accounts, savings_list, loans, guarantors, payments)

    return render_template("savings.html", savings_list=savings_list, accounts=accounts)


# Route to apply for loans and approve or reject loans
@app.route("/loans", methods=["GET", "POST"])
def loans_page():
    members, staff_list, accounts, savings_list, loans, guarantors, payments = load_all_data(storage)
    error = None

    if request.method == "POST":
        action = request.form["action"]
        today = str(datetime.now().date())

        # Create a new loan application
        if action == "apply":
            member_id = request.form["member_id"]
            loan_amount = int(request.form["loan_amount"])
            payment_period = request.form["payment_period"]
            payment_method = request.form["payment_method"]
            loan_purpose = request.form["loan_purpose"]

            member = find_member(members, member_id)
            limit = Loan.calculate_loan_limit(member, accounts)
            if not Loan.is_within_limit(member, loan_amount, accounts):
                error = (f"Loan of UGX {loan_amount} rejected. {member.get_full_name()}'s loan limit "
                         f"is UGX {limit} (3 x account balance).")
            else:
                loan = Loan(member, loan_amount, payment_period, payment_method, loan_purpose, today)
                loans.append(loan)
                save_all_data(storage, members, staff_list, accounts, savings_list, loans, guarantors, payments)

        # Staff approves or rejects a pending loan
        elif action == "decision":
            loan_id = request.form["loan_id"]
            staff_id = request.form["staff_id"]
            decision = request.form["decision"]

            loan = find_loan(loans, loan_id)
            staff = find_staff(staff_list, staff_id)

            if decision == "Approve":
                staff.approve_loan(loan)
            elif decision == "Reject":
                staff.reject_loan(loan)
            save_all_data(storage, members, staff_list, accounts, savings_list, loans, guarantors, payments)

    return render_template("loans.html", loans=loans, members=members, staff_list=staff_list, error=error)


# Route to add guarantors to a loan
@app.route("/guarantors", methods=["GET", "POST"])
def guarantors_page():
    members, staff_list, accounts, savings_list, loans, guarantors, payments = load_all_data(storage)
    error = None

    if request.method == "POST":
        loan_id = request.form["loan_id"]
        member_id = request.form["member_id"]
        amount_guaranteed = int(request.form["amount_guaranteed"])

        loan = find_loan(loans, loan_id)
        member = find_member(members, member_id)

        # A guarantor's balance must be at least a quarter of the loan amount
        if not loan.can_be_guaranteed_by(member):
            error = (f"{member.get_full_name()} cannot guarantee loan {loan.get_loan_id()}. "
                     f"Balance must be at least UGX {loan.get_required_guarantor_balance():.0f} "
                     f"(1/4 of the loan amount).")
        else:
            # Create Guarantor object and attach to the loan
            g = Guarantor(member, loan, amount_guaranteed)
            if loan.add_guarantor(g):
                guarantors.append(g)
                save_all_data(storage, members, staff_list, accounts, savings_list, loans, guarantors, payments)

    return render_template("guarantors.html", guarantors=guarantors, loans=loans, members=members, error=error)


# Route to record loan repayments
@app.route("/payments", methods=["GET", "POST"])
def payments_page():
    members, staff_list, accounts, savings_list, loans, guarantors, payments = load_all_data(storage)

    if request.method == "POST":
        loan_id = request.form["loan_id"]
        amount_paid = int(request.form["amount_paid"])
        payment_method = request.form["payment_method"]
        today = str(datetime.now().date())

        # Create LoanPayment object and update loan balance
        loan = find_loan(loans, loan_id)
        lp = LoanPayment(loan, amount_paid, payment_method, today)
        if lp.make_payment():
            payments.append(lp)
            save_all_data(storage, members, staff_list, accounts, savings_list, loans, guarantors, payments)

    return render_template("payments.html", payments=payments, loans=loans)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
