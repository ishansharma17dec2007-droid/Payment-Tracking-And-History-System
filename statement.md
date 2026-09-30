# Project Statement: Payment Tracking and History

**Student Name:** Ishan Sharma
**Reg No:** 26BAI10742
**Program:** B.Tech CSE (AI & ML), VIT Bhopal University
**Academic Year:** 2026-27

---

## Problem Statement

When a person has to manage many payments, it becomes hard to find a specific payment or to work out the total amount paid and pending without a computer. Most people rely on notebooks or Excel sheets, which are slow to search, easy to get wrong, and tiring to maintain by hand.

## Proposed Solution

A Python program that lets a user record payments, view the full payment history, search for specific payments, and calculate the total paid and pending amounts. All records are stored in a JSON file so the data is saved and does not disappear when the program is closed.

## Objectives

- Add payment records
- View the complete payment history
- Search for specific payments
- Calculate total paid and pending amounts
- Practise functions, loops, file handling and validation in Python
- Add update and delete features (optional, if time permits)

## Scope

**In scope**
- Command-line, menu-driven program (Add Payment, Show Payment History, Search Payment, Show Total Paid Amount, Exit)
- Each payment stores the customer name, amount, payment method and status (Paid / Pending)
- Input validation for wrong or invalid entries (empty names, zero or negative amounts, incorrect payment method)
- Local storage in JSON, suitable for about 100 to 500 payments
- Basic unit testing

**Out of scope (possible future work)**
- Login system
- Database support
- Graphical user interface
- Payment reminders
- Reports and charts
- Export options
- Online version

## Target Users

- Individuals and small business owners who track payments manually and want something faster than notebooks or spreadsheets (the project was inspired by my father's need to keep track of his payments)
- Users with no technical background, since the program is meant to be easy to understand and use

## High-Level Features

| Feature | Description |
|---|---|
| Add payment | Enter customer name, amount, payment method and status |
| Payment history | Display all saved payment records |
| Search payment | Find a specific payment |
| Payment summary | Show the total paid amount and pending amounts |
| Input validation | Rejects invalid data and asks the user to re-enter it |
| Persistent storage | Records are saved in `Payments.json` |

## Non-Functional Requirements

- Easy to understand and use
- Handles incorrect input without crashing
- Data is saved permanently
- Acceptable performance for up to about 500 payments

## Technologies Used

- **Python 3**: main programming language
- **JSON**: local storage of payment records
- **Python unittest**: basic testing
- **VS Code**: writing and running the code
- **Git and GitHub**: version control

## Project Structure

| File | Purpose |
|---|---|
| `Main.py` | Entry point of the program |
| `Payment_manager.py` | Handles adding, searching and other payment operations |
| `Storage.py` | Saves and loads data from JSON |
| `Validation.py` | Checks whether the input is valid |
| `Payments.json` | Stores the payment data |
| `Test_payment.py` | Basic tests |

## Workflow

User opens the program → menu is shown → user picks an option (1 to 5) → program performs the action → data is saved if needed → returns to the menu → user exits.
