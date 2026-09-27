# Payment Tracking and History System

payments = []


def add_payment():
    name = input("Enter customer name: ")
    amount = float(input("Enter amount: "))
    method = input("Enter payment method: ")
    status = input("Enter payment status (Paid/Pending): ")

    payment = {
        "name": name,
        "amount": amount,
        "method": method,
        "status": status
    }

    payments.append(payment)
    print("Payment added successfully!")


def show_payments():
    if len(payments) == 0:
        print("No payment history available.")
    else:
        print("\n----- Payment History -----")

        for i in range(len(payments)):
            print("\nPayment", i + 1)
            print("Customer:", payments[i]["name"])
            print("Amount: Rs.", payments[i]["amount"])
            print("Method:", payments[i]["method"])
            print("Status:", payments[i]["status"])


def search_payment():
    name = input("Enter customer name: ")
    found = False

    for payment in payments:
        if payment["name"].lower() == name.lower():
            print("\nPayment Found")
            print("Customer:", payment["name"])
            print("Amount: Rs.", payment["amount"])
            print("Method:", payment["method"])
            print("Status:", payment["status"])
            found = True

    if found == False:
        print("Payment not found.")


def total_paid():
    total = 0

    for payment in payments:
        if payment["status"].lower() == "paid":
            total = total + payment["amount"]

    print("Total Paid Amount = Rs.", total)


while True:

    print("\n===== PAYMENT TRACKING SYSTEM =====")
    print("1. Add Payment")
    print("2. Show Payment History")
    print("3. Search Payment")
    print("4. Show Total Paid Amount")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_payment()

    elif choice == "2":
        show_payments()

    elif choice == "3":
        search_payment()

    elif choice == "4":
        total_paid()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")

