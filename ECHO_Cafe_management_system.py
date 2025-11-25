#Welcome Message
print("Welcome to ECHO.Where good vibes resonate")

menu={"Flat White":230,"Mocha":260,"Piccolo Latte":240,"Cafe Latte":220,"Long Black":180,"Cappucino":200}    #MENU(Dictionary)
coffee=("Flat White","Mocha","Piccolo Latte","Cafe Latte","Cappucino")                                       #COFFEE OPTIONS THAT OFFERS PERSONALIZATION(Tuple)
milk=("Soy Milk","Almond Milk","Skimmed Milk","Oat Milk")                                                    #MILK OPTIONS(Tuple)
coffee_art=("Heart","Tulip","Rosetta","Swan")                                                                #COFFEE ART DESIGN OPTONS(Tuple)
games=("Chess","Jenga","Hangman","Scrabble")                                                                 #COMPLIMENTARY BOARD GAME OPTIOBS(Tuple)
print("--Dive into delicious—check out our menu!--")
print("Flat White: Rs 230\nPiccolo Latte: Rs 240\nCafe Latte: Rs 220\nLong Black: Rs 180\nCappucino: Rs 200") #PRINTING MENU

order_total=0                                                                                                #INTIALIZING VARIABLE FOR TOTAL BILL

#First item
item_1=input("What would you like us to prepare for you?")                                                   #TAKING INPUT FOR FIRST ITEM
if item_1 in menu:                                                                                           #USING IF STATEMENT FOR CHECKING VALIDATION OF INPUT
    order_total+=menu[item_1]                                                                                #ADDING THE PRICE OF PREFERERD ITEM TO VARIABLE
    if item_1=="Long Black":                                                                                 #CHECKING IF SELECTED ITEM NEEDS PERSONALIZATION OR NOT
        name1=input("What name should we write on your cup?")                                                #TAKING INPUT FOR NAME
        print(f"--{item_1} for {name1} will be prepared shortly--")                                          #PRINTING ORDER SUMMARY
        
    if item_1 in coffee:                                                                                     #CHECKING IF SELECTED ITEM NEEDS PERSONALIZATION OR NO                           
        print("--Personalize your brew with your preferred milk!--")
        print("Skimmed Milk\nSoy Milk\nAlmond Milk\nOat Milk")                                               #PRINTING AVAILABLE MILK OPTIONS
        milk1=input("Which milk would you like?")                                                            #TAKING INPUT FOR PREFERRED MILK
        if milk1 not in milk:                                                                                #USING IF STATEMENT TO CHECK VALIDATION OF INPUT
            print("Sorry! That milk option isn’t available. Please choose from our menu options.")           #PRINT STATEMENT
            
        print("--Time to decorate! Choose your coffee art pattern.--")
        print("Heart\nTulip\nRosetta\nSwan")                                                                 #PRINTING COFFEE ART DESIGN AVAILABLE
        art_1=input("Which coffee art design would you like?")                                               #TAKING INPUT FOR PREFERREF DESIGN
        if art_1 not in coffee_art:                                                                          #USING IF STATEMENT TO CHECK INPUT VALIDATION
            print("Sorry! That design isn’t available. Please choose one from our menu")                     #PRINT STATEMENT
          
        name1=input("What name should we write on your cup?")                                                #INPUT FOR NAME
        print(f"Your {item_1} with {milk1} and {art_1} design for {name1} will be served shortly")           #PRINTING ORDER SUMMARY
            
if item_1 not in menu:                                                                                       #USING IF STATEMENT TO CHECK INPUT VALIDATION 
    print("Sorry! We don’t have that coffee available. Please choose an option from our menu.")              #PRINT STATEMENT
  
    
#Second item
another_order=input("Would you like to add anything else?(Yes/No):")                                         #TAKING INPUT IF ANOTHER COFFEE NEEDED
if another_order=="Yes":                                                                                     #USING IF STATEMENT 
    item_2=input("What would you like us to prepare for you?")                                               #TAKING INPUT FOR SECOND ORDER
    if item_2 in menu:                                                                                       #USING IF STATEMENT FOR CHECKING VALIDATION OF INPUT
        order_total+=menu[item_2]                                                                            #ADDING THE PRICE OF PREFERERD ITEM TO VARIABLE

        if item_2=="Long Black":                                                                             #CHECKING IF SELECTED ITEM NEEDS PERSONALIZATION OR NOT
            name2=input("What name should we write on your cup?")                                            #TAKING INPUT FOR NAME
            print(f"Your {item_2} for {name2} will be served shortly")                                       #PRINTING ORDER SUMMARY
        if item_2 in coffee:
            print("--Personalize your brew with your preferred milk!--")
            print("Skimmed Milk\nSoy Milk\nAlmond Milk\nOat Milk")                                           #PRINTING AVAILABLE MILK OPTIONS
            milk2=input("Which milk would you like?")                                                        #TAKING INPUT FOR PREFERRED MILK
            if milk2 not in milk:                                                                            #USING IF STATEMENT TO CHECK VALIDATION OF INPUT
                print("Sorry! That milk option isn’t available. Please choose from our menu options.")       #PRINT STATEMENT

            print("--Time to decorate! Choose your coffee art pattern.--")
            print("Heart\nTulip\nRosetta\nSwan")                                                             #PRINTING COFFEE ART DESIGN AVAILABLE
            art_2=input("Which coffee art design would you like?")                                           #TAKING INPUT FOR PREFERREF DESIGN        
                                                      
            if art_2 not in coffee_art:                                                                      #USING IF STATEMENT TO CHECK INPUT VALIDATION
                print("Sorry! That design isn’t available. Please choose one from our menu")                 #PRINT STATEMENT
            name2=input("What name should we write on your cup?")                                            #TAKING INPUT FOR NAME
            print(f"Your {item_2} with {milk2} and {art_2} design for {name2} will be served shortly")       #PRINTING ORDER SUMMARY
    if item_2 not in menu:
        print("Sorry! We don’t have that coffee available. Please choose an option from our menu.")          #PRINT STATEMENT
        

      
#GAMES
print("--Enjoy our complimentary games while you wait.--")
print("Chess\nJenga\nHangman\nScrabble")                                                                    #PRINTING AVAILABLE GAMES
game=input("Which game would you like to play?")                                                            #TAKING USER INPUT FOR PREFERRED GAME
if game in games:                                                                                           #USING IF STATEMENT TO CHECK USER INPUT
    print("Please collect your board game from the counter by showing your receipt.")                       #PRINT STATEMENT WITH INSTRUCTIONS
if game=="No":                                                                                              #USING PRINT STATEMENT TO CHECK USER INPUT
    print("That’s okay! Let us know if you want to play later.")                                            #PRINT STATEMENT
if game not in games:                                                                                       # USING PRINT STATEMENT TO CHECK USER INPUT
    print("Sorry! That game isn’t available. Please choose one from the options below.")                    #PRINT STATEMENT

#BILL
print(f"--The total amount is Rs{order_total}--")                                                           #PRINTING OREDER TOTAL
method_pay=input("How would you like to pay? Cash, Card, or UPI?")                                          #TAKING INPUT FOR METHOD OF PAYMENT
if method_pay=="Cash":                                                                                      #USING IF STATEMENT TO CHECK USER INPUT
    print(f"Please pay the cashier Rs{order_total}")                                                        #PRINT STATEMENT WITH INSTRUCTIONS
if method_pay=="Card":                                                                                      #USING IF STATEMENT TO CHECK USER INPUT
    print(f"Please swipe or tap your card to pay Rs{order_total}")                                          #PRINT STATEMENT WITH INSTRUCTIONS
if method_pay=="UPI":                                                                                       #USING IF STATEMENT TO CHECK USER INPUT
    print(f"Please scan the QR to pay Rs{order_total}")                                                     #PRINT STATEMENT WITH INSTRUCTIONS                        

print("--Thank you for ordering.Hope you have good time at ECHO--")                                         #PRINT STATEMENT WITH GREETING
    