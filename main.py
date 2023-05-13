import api_project as app

print("\nWELCOME TO GERON'S CITY API !\n")

continueLoop = True
while continueLoop:
    
    app.runApp()
    
    continueChoice = input("Do you want to continue? (Y/N) ").upper()
    if continueChoice == "N":
        print("\nThank you for taking part. Goodbye!")
        continueLoop = False