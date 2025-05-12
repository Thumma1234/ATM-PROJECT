
💳 ATM Web Application using Flask & MySQL

A fully functional **ATM simulation web application** developed using **Python (Flask)** for the backend and **MySQL** as the database. This project mimics real-world ATM operations like withdrawing and depositing money, generating a PIN, and viewing account balances — all through a clean, browser-based interface.

🌐 Project Overview

This web-based ATM system allows users to:

* Withdraw money securely using account number and PIN
* Deposit money directly into their account
* Generate a PIN for first-time users
* View mini statements with their name, email, and balance
* Handle common ATM errors like wrong PIN, insufficient balance, and invalid account numbers

All interactions are handled via HTML forms and rendered dynamically using Flask's Jinja2 templating engine.

⚙️ Functional Modules

🔐 **User Authentication**

* No login page required.
* Users authenticate with `Account Number` and `PIN` in each transaction.

💵 **Withdraw**

* Users enter account number and PIN.
* PIN validation is performed.
* Balance check ensures sufficient funds before transaction.
* If valid, the balance is updated and confirmation is shown.

💰 **Deposit**

* Account number-based deposit.
* Amount is added to the current balance.
* Confirmation shown after successful deposit.

📄 **Mini Statement**

* Shows the user's name, email, and current balance.
* Requires account number and correct PIN.

🔑 **PIN Generation**

* Allows users with no PIN to create one.
* Prevents re-generation if a PIN already exists.

🧠 Technologies Used

| Technology | Description                           |
| ---------- | ------------------------------------- |
| Python     | Programming Language                  |
| Flask      | Lightweight web framework             |
| MySQL      | Relational Database                   |
| PyMySQL    | Connector between Python and MySQL    |
| HTML/CSS   | Frontend templating and basic styling |
| Jinja2     | Template rendering for HTML pages     |


📸 UI Pages

| Page              | Description                            |
| ----------------- | -------------------------------------- |
| `/`               | Landing Page                           |
| `/withdraw1`      | Enter Account Number & PIN to Withdraw |
| `/withdraw2`      | Enter Amount to Withdraw               |
| `/deposit`        | Deposit to Account                     |
| `/ministatement1` | Input for Mini Statement               |
| `/ministatement2` | Shows Mini Statement                   |
| `/pingeneration1` | Input for PIN Generation               |
| `/pingeneration2` | PIN Generation Form                    |

🔐 Error Handling & Validation

* ✅ Account does not exist ➜ User is notified.
* 🔒 PIN not generated ➜ Prompted to create a PIN first.
* ❌ Wrong PIN ➜ Error message shown.
* ⚠️ Insufficient balance ➜ Transaction declined.

📦 Future Improvements

* Add Login System (Admin/User roles)
* Transaction History Table
* Security enhancements (hashed PINs)
* Responsive UI with Bootstrap
* API integration for real banking systems


