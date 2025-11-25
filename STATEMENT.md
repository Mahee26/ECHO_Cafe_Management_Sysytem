## Problem Statement
To design and implement a program that simulates a basic ordering experience at a coffee shop named "ECHO." The system must allow customers to select up to two items from a fixed menu, customize their coffee with milk and latte art choices, calculate the total cost, offer a choice of complimentary games while they wait, and provide payment instructions based on the chosen method

Key Requirements Solved by the Code
The core functionalities the code was written to address include:
**Menu & Pricing: Maintain a fixed menu with corresponding prices and display it to the customer.
**Order Calculation**
 Accurately calculate and track the running order_total for all items purchased.
**Customization**
 Enable specific menu items (like "Flat White" or "Mocha") to be customized with four available milk types and    four latte art designs.
**Input Validation (Basic)**
 Handle cases where the customer requests an item, milk, or art that is not on the available lists.
**Second Item Logic**
 Allow the customer to optionally add a second item, applying the same validation and customization logic.
**Engagement**
 Offer a list of complimentary games for the customer to choose while waiting.
**Billing & Payment**
 Display the final total and generate tailored instructions for three payment methods: Cash, Card, or UPI.


## Scope
The code's scope is strictly limited to simulating an simple, interactive, ordering and billing operations for a coffee shop. 

**Order Limitation**
 The program is scoped to handle a maximum of two items per transaction. It does not allow for continuous ordering, multi-person orders, or bulk purchases.
**Fixed Data Set**
 All menu items, prices, customization options (milks, art), and games are hard-coded into the script (using dictionaries and tuples). The scope does not include reading data from external files (like CSVs or databases) or allowing staff to update the menu.
**Simple Flow Control**
 The logic uses basic sequential execution and conditional branching (if/else statements). The scope does not include advanced features like loops (for continuous ordering until a specific action is taken), functions (for code reuse), or object-oriented programming (for modeling items as objects).
**No Persistence**
 The transaction data (the order and the total) is lost immediately when the program ends. The scope does not include saving order history, customer data, or updating inventory levels.


## Target Users
1. The Coffee Shop Staff (Barista/Cashier)
The most direct and immediate user of this code is the person operating the system at the counter.
2. The Coffee Shop Customer
The system's logic models the experience of the actual customer. While they don't type into the system directly, the script's outputs and prompts are designed for their benefit.

## High-Level Features
1. Sequential Order Processing
The system enables a linear flow for processing transactions, ensuring staff follows a clear path from greeting to payment. This includes handling up to two distinct orders within a single session.
2. Customization and Personalization
The code allows for detailed personalization of coffee orders, which is a key value-add for the customer experience.
Milk Alternatives: The ability to select from four different milk types (Soy, Almond, Skimmed, Oat).
Latte Art: The option to choose from four coffee art designs (Heart, Tulip, Rosetta, Swan).
Name on Cup: Prompting for the customer's name to be added to the cup for preparation.
3. Basic Input Validation
It incorporates simple checks to ensure operational integrity. The system can verify if an entered coffee item, milk choice, or art design is valid (present in the hardcoded lists) before proceeding, providing feedback to the user if the input is incorrect.
4. Financial Calculation and Billing
The system's core function is to handle the monetary aspects of the transaction efficiently.
Automatic Tally: It automatically calculates and displays the final order_total based on the selected items.
Payment Instruction Generation: It provides clear, method-specific instructions for Cash, Card, or UPI payments.
5. Customer Engagement
Beyond the transaction, the code adds a soft feature to enhance the customer's waiting experience.
Complimentary Game Offering: It offers a selection of four board games, turning the waiting time into a service opportunity.

