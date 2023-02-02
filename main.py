print("""Bill Calculator
---------------

* * * This will calculate your tip and split the bill evenly between friends. Press the ENTER key after each entry (no symbols.) * * *

---------------""")
#Loop the program while 'again' is true, allowing the user to calculate multiple times
again = True
while (again == True):
    amount = float(input("\nHow much is the total bill? $"))
    percent = float(input("\nWhat percentage do you want to tip? "))
    #Divide percent by 100 to get percentage in decimal form
    percent = percent / 100
    #Calculate tip amount by multiplying tip percent by total bill
    tip = round(amount * percent, 2)
    #Set tip to string so it can be concatenated to other string
    tipInStr = str(tip)
    print("\nYour tip is $" + tipInStr)
    total = round(amount + tip, 2)
    #Set total to string so it can be concatenated to other string
    totalInStr = str(total)
    print("\nYour total including tip is $" + totalInStr)
    people = int(input("\nHow many people are in your group? "))
    owed = round(total / people, 2)
    #Set owed to string so it can be concatenated to other string
    owedInStr = str(owed)
    print("\nYou each owe $" + owedInStr)
    print("\nThank you for using my Bill Calculator!")
    #Input Y or N to calculate again, capitalize input in case lower case is used. If yes then 'oneMore' is true and loops back to beginning. If no, then 'oneMore' is false and program ends. All other entries are invalid and program ends.
    oneMore = input("\nWould you like to calculate another bill? (Y/N): ").capitalize()
    if (oneMore == "Y"):
      print("\n--------------------")
      again = True
    elif (oneMore == "N"):
      again = False
      print("\nHave a nice day.")
    else:
      again = False
      print("\nInvalid entry, good bye!")
