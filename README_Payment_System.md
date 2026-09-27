# Payment Tracking System

A simple Python-based payment management system that allows users to add, view, search, and track payment records with an interactive command-line interface.

## 📋 Overview

The Payment Tracking System is a beginner-friendly application designed to maintain payment records efficiently. It stores payment information in memory and provides essential functionality for managing customer payments.

**Student Name:** ISHAN SHARMA  
**Registration Number:** 26BAI10742  
**Program:** B.Tech CSE (AI & ML)  
**University:** VIT Bhopal University  
**Academic Year:** 2026-27

## ✨ Features

- **Add Payment Records** - Add new payment transactions with customer details
- **View Payment History** - Display all stored payment records with complete information
- **Search Payments** - Search for payment records by customer name (case-insensitive)
- **Calculate Total Paid Amount** - Get the sum of all paid transactions
- **Interactive Menu** - User-friendly command-line interface
- **Input Validation** - Basic validation for payment amounts

## 🛠️ Technologies Used

- **Language:** Python 3
- **Data Structure:** Lists and Dictionaries
- **Storage:** In-memory (during program execution)

## 📁 Project Structure

```
payment-tracking-system/
├── payment_system.py       # Main application file
└── README.md               # This file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.x installed on your system
- Terminal or Command Prompt

### Running the Application

1. **Save the code** as `payment_system.py`

2. **Run the program:**
   ```bash
   python payment_system.py
   ```

3. **Follow the menu** to perform desired operations

## 📖 Usage Guide

### Main Menu Options

```
===== PAYMENT TRACKING SYSTEM =====
1. Add Payment
2. Show Payment History
3. Search Payment
4. Show Total Paid Amount
5. Exit
```

### Operation Details

#### 1. Add Payment
- Select option `1` from the main menu
- Enter customer name
- Enter payment amount
- Enter payment method (e.g., UPI, Card, Cash, Cheque, etc.)
- Enter payment status (`Paid` or `Pending`)

**Example:**
```
Enter customer name: Amit
Enter amount: 500
Enter payment method: UPI
Enter payment status (Paid/Pending): Paid
Payment added successfully!
```

#### 2. Show Payment History
- Select option `2` from the main menu
- All payment records will be displayed in a formatted list
- Shows payment number, customer name, amount, method, and status

**Example Output:**
```
----- Payment History -----

Payment 1
Customer: Amit
Amount: Rs. 500
Method: UPI
Status: Paid

Payment 2
Customer: Priya
Amount: Rs. 1000
Method: Card
Status: Pending
```

#### 3. Search Payment
- Select option `3` from the main menu
- Enter the customer name to search
- If found, displays the payment details
- Search is case-insensitive (e.g., "amit", "AMIT", "Amit" all work)

**Example:**
```
Enter customer name: Amit

Payment Found
Customer: Amit
Amount: Rs. 500
Method: UPI
Status: Paid
```

#### 4. Show Total Paid Amount
- Select option `4` from the main menu
- Displays the sum of all payments with status "Paid"
- Only counts payments marked as "Paid", excludes "Pending" status

**Example Output:**
```
Total Paid Amount = Rs. 1500
```

#### 5. Exit
- Select option `5` to exit the program
- Program displays "Thank you!" and closes

## 📊 Data Structure

Each payment record is stored as a dictionary with the following structure:

```python
{
    "name": "Customer Name",
    "amount": 500,
    "method": "UPI",
    "status": "Paid"
}
```

### Payment Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| name | String | Customer or payer name | Amit |
| amount | Float | Payment amount in rupees | 500.00 |
| method | String | Payment method | UPI, Card, Cash, Cheque |
| status | String | Payment status | Paid, Pending |

## 💡 How It Works

1. **Main Loop** - The program runs in an infinite loop until user selects "Exit"
2. **Menu Display** - Shows 5 options to the user
3. **Function Calls** - Based on user choice, appropriate function is executed
4. **Data Storage** - Payments are stored in a global list during the session

### Program Flow Diagram

```
Start
  ↓
Display Menu
  ↓
Get User Choice
  ↓
  ├→ Choice 1: Add Payment → append to payments list
  ├→ Choice 2: Show History → display all payments
  ├→ Choice 3: Search → find by name
  ├→ Choice 4: Total Paid → sum paid amount
  ├→ Choice 5: Exit → break loop and exit
  └→ Invalid → display error
  ↓
Back to Menu (unless Exit)
  ↓
End
```

## 🔧 Function Descriptions

### `add_payment()`
- Prompts user for payment details
- Creates a dictionary with payment information
- Appends the payment to the payments list
- Confirms successful addition

### `show_payments()`
- Checks if payments list is empty
- Displays "No payment history available" if empty
- Otherwise, iterates through payments list
- Displays each payment with numbered format

### `search_payment()`
- Takes customer name as input
- Searches through payments list with case-insensitive matching
- Displays matching payment if found
- Shows "Payment not found" message if no match

### `total_paid()`
- Iterates through payments list
- Sums amounts where status is "Paid" (case-insensitive)
- Displays total in rupees format

## 📝 Example Workflow

```
===== PAYMENT TRACKING SYSTEM =====
1. Add Payment
2. Show Payment History
3. Search Payment
4. Show Total Paid Amount
5. Exit
Enter your choice: 1

Enter customer name: Amit
Enter amount: 500
Enter payment method: UPI
Enter payment status (Paid/Pending): Paid
Payment added successfully!

===== PAYMENT TRACKING SYSTEM =====
1. Add Payment
2. Show Payment History
3. Search Payment
4. Show Total Paid Amount
5. Exit
Enter your choice: 2

----- Payment History -----

Payment 1
Customer: Amit
Amount: Rs. 500
Method: UPI
Status: Paid

===== PAYMENT TRACKING SYSTEM =====
1. Add Payment
2. Show Payment History
3. Search Payment
4. Show Total Paid Amount
5. Exit
Enter your choice: 4

Total Paid Amount = Rs. 500

===== PAYMENT TRACKING SYSTEM =====
1. Add Payment
2. Show Payment History
3. Search Payment
4. Show Total Paid Amount
5. Exit
Enter your choice: 5

Thank you!
```

## ⚠️ Important Notes

### Data Persistence
- **Current Version:** Payments are stored in memory only
- Data is lost when the program terminates
- All records are reset on each new program run

### Limitations
- No duplicate prevention for customer names
- No payment ID system for individual transactions
- No data backup or file storage
- No delete or update functionality
- Amounts are stored as floats with precision issues for currency

## 🚀 Future Enhancements

The system can be improved with:

1. **File Storage** - Save payments to a JSON or CSV file
2. **Update Function** - Modify existing payment records
3. **Delete Function** - Remove payment records
4. **Payment ID** - Add unique identifiers for each payment
5. **Payment Dates** - Track when each payment was made
6. **Sorting** - Sort payments by amount, date, or name
7. **Statistics** - Show pending amount, payment count, average amount
8. **Input Validation** - Validate amount is positive, status is Paid/Pending
9. **GUI Interface** - Create graphical user interface using Tkinter
10. **Database** - Use SQLite for persistent storage

## 📚 Learning Concepts Covered

✓ Lists and Dictionaries  
✓ Functions and parameters  
✓ While loops and conditional statements  
✓ String methods (lower() for case-insensitive comparison)  
✓ Type conversion (float for amounts)  
✓ List iteration  
✓ User input handling  
✓ Basic program flow control  

## 🧪 Testing Recommendations

Test the following scenarios:

1. **Add Multiple Payments** - Verify all records are stored
2. **Search Existing Customer** - Check case-insensitive search works
3. **Search Non-existent Customer** - Verify "not found" message
4. **View Empty History** - Test with no payments added
5. **Calculate Total** - Verify only "Paid" status is counted
6. **Mixed Statuses** - Add both Paid and Pending, check total
7. **Invalid Menu Choice** - Verify error message for wrong input

## 🎓 Conclusion

The Payment Tracking System provides a foundation for understanding basic Python programming concepts including data structures, functions, and user interaction. While the current version operates with in-memory storage, it can serve as a starting point for building more sophisticated payment management applications.

## 👤 Author Information

**Name:** ISHAN SHARMA  
**Registration Number:** 26BAI10742  
**Institution:** VIT Bhopal University  
**Department:** Computer Science and Engineering (AI & ML)  
**Academic Year:** 2026-27

## 📄 License

This project is created for educational purposes as part of the B.Tech CSE curriculum.

## 💬 Feedback & Improvements

This is a beginner-level project designed to demonstrate fundamental Python concepts. For improvements or questions, please refer to the course instructor or teaching assistant.

---

**Last Updated:** 2026-27 Academic Year  
**Version:** 1.0
