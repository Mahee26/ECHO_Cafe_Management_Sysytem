# ECHO Coffee Ordering System

# OVERVIEW
This is a  simple, interactive ordering and billing system for a coffee shop. It allows customers to place upto 2 orders. They can personalize their coffee by selecting preferred milk and coffee art. This also allows consumers to choose a complimentary game. They can see their final bill and make payment through different options.


# FEATURES
**Menu Display**
Displays menu with fixed prices

**Personalization**
Allows selection of preferred milk (Soy, Almond, Oat, Skimmed).
Allows selection of coffee art desing (Swan, Heart, Tulip, Rosetta).

**Second Item**
Allows adding an optional second item to order.

**Game Selection**
Offers choice of complimentary games to choose from (Chess, Jenga, Scrabble, Hangman).

**Billing**
Calculates total and provide payment option (Cash, Card, UPI).

**Validation**
Includes basic input checks, if the preferred items are in options or not.





# CODE STRUCTURE AND VARIABLES
This program is structured sequentially, handling up to two potential orders, game selection and final billing

## 1.Data Intialization
|  Variable      |  Type    |  Descripton                                                  | 
|  “menu”        |Dictionary|  Stores coffee names and prices (in Rs)                      |
|  “coffee”      |  Tuple   |  List of items that can be personalized                      |
|  “milk"        |  Tuple   |  List of available milk options                              |
|  “coffee_art”  |  Tuple   |  List of available coffee art designs                        |
|  “games”       |  Tuple   |  List of complimentary boards games available                |
|  “order_total” |  integer |  Running total cost of all the ordered items(starting from 0)|


## 2. Order 1  Logic
This sections handles the consumers first order, checks for order validation and then branches it based on option selected. Also adds the price of selected item to variable “order_total” which can be later used while billing.

**Long Black**   Only asks input fir name on the cup

**Other item**  Asks user input for milk, coffee art design, and name. Includes basic checks for validation for user’s input

## 3. Order 2 Logic
**User Input**  Asks user if they would like to add a second order(“another_order”).
**Logic**   If the user enters “Yes”, the entire ordering and personalization logic from order 1 is repeated.

## 4. Games
**User input**  Prints the list of available games and takes their input for the preferred game. Checks for validation, if the game is available or not.

## 5. Billing
**Total Bill**  Prints finalized calculated  “order_total”
**Payment**  Asks for preferred method for payment(“method_pay”) (Cash,Card or UPI) and then prints corresponding payment instructions.


# CODE AND OUTPUTS

<img width="2983" height="1312" alt="image" src="https://github.com/user-attachments/assets/67179184-7275-4262-be1d-e9735999bbf5" />

<img width="3000" height="1594" alt="image" src="https://github.com/user-attachments/assets/0f1cff90-6c9c-4ae7-8c6f-0a0c39ae2408" />

<img width="3000" height="1594" alt="image" src="https://github.com/user-attachments/assets/aa356887-1c48-4220-9098-a58b9ab8b367" />

<img width="1578" height="1395" alt="image" src="https://github.com/user-attachments/assets/ac42184b-0af4-4bfa-816d-a0692f65511c" />

<img width="1572" height="1024" alt="image" src="https://github.com/user-attachments/assets/20c49797-b54b-45ac-8ce8-03dd84d39484" />


<img width="1566" height="876" alt="image" src="https://github.com/user-attachments/assets/d9ada616-2b68-4265-8562-8ee6494bae5b" />


<img width="1560" height="947" alt="image" src="https://github.com/user-attachments/assets/7d55ca3c-8f58-4245-824b-1850e2ede26e" />


# HOW TO RUN (SETUP INSTRUCTIONS)
*1.Clone to repository*
    git clone <https://github.com/Mahee26/VITyarthiproject-Cafe-management-system.git>














