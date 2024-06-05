# <<<<<<< VARIABLES >>>>>>>>>
User = "ODAI LARRY-NOBLE NII LARYEA";
PIN = 2004;
Balance = 300;
Data_Bundle = 200;
Airtime = 20000;
MoMo = 2000;

Menu = """
Menu
1) Transfer Money
2) Airtime & Bundles
3) Financial Services
4) My Wallet
0) Exit
"""

Wallet_menu = """
My Wallet
1) Check Balance & Data & PIN
2) Change & Reset PIN
0) Back
"""
AirtimeMenu = """
Airtime & Bundles
1) Internet Bundles
0) Back
"""
personel = """
1) Self
0) Back
"""
Dataoptions = """
1) GHc10 (13000.12GB)
2) Ghc15 (20000.30GB)
0) Back
"""
TransferMenu = """
Transfer Money
1) MoMo User
2) Other Networks
0) Back
"""
Networks = """
Networks
1) AirtelTigo
2) Vodafone
"""






# <<<<<<<<<<<<<< SYSTEM OPERATIONS >>>>>>>>>>>>>>>
# <<<<< KEYPAD TO MENU >>>>>>>
Keypad = int(input("Enter Keypad Number: "))

if Keypad == 170:
    while True:
        print(Menu)
        Option = int(input("Select An Option: "))

        # <<<<<<<<<<<<<<<<< TRANSFER MONEY >>>>>>>>>>>>>>>>>>>>
        if Option == 1:
            while True:
                print(TransferMenu);
                MenuOption = int(input("Option: "));
        
                if (MenuOption ==  1):
                    Number = int(input("Enter Mobile Number: "));
                    ReNumber = int(input("ReEnter Mobile Number: "));
                    if (Number == ReNumber):
                        Amt = int(input("Enter The Amount: Ghc"));
                        MoMo = MoMo - Amt;  
                        reference = input("Enter Reference: ");
                        print(f"Payment to be made to {User},\nof Ghc{Amt}- Reference: {reference}\n")
                        key = int(input("Enter your PIN to verify transaction: \n"));
                        if (key == PIN):
                            print(f"Payment made to {User}\nof Ghc{Amt}- Reference: {reference}\nCurrent Balance: Ghc{MoMo}");
                        else:
                            break
                    else: 
                        print("Number does not match!! ");
                    back_option = int(input("Select 0 to go back: "))
                    if back_option == 0:
                        continue  # Goes back to the main menu loop
                elif MenuOption == 0:
                    break  # Exit to main menu

                if (MenuOption ==  2):
                    print(Networks);
                    NetworkOption = int(input("Select Network: "));
                    if NetworkOption == 1 or 2:
                        Number = int(input("Enter Mobile Number: "));
                        ReNumber = int(input("ReEnter Mobile Number: "));
                    if (Number == ReNumber):
                        Amt = int(input("Enter The Amount: Ghc"));
                        MoMo = MoMo - Amt;  
                        reference = input("Enter Reference: ");
                        print(f"Payment to be made to {User},\nof Ghc{Amt}- Reference: {reference}\nNumber: {Number}\n")
                        key = int(input("Enter your PIN to verify transaction: \n"));
                        if (key == PIN):
                            print(f"Payment made to {User}\nof Ghc{Amt}- Reference: {reference} - Number: {Number}\nCurrent Balance: Ghc{MoMo}");
                        else:
                            break
                    else: 
                        print("Number does not match!! ");
                    back_option = int(input("Select 0 to go back: "))
                    if back_option == 0:
                        continue  # Goes back to the main menu loop
                elif MenuOption == 0:
                    break  # Exit to main menu

                
        elif Option == 0:
            break




        # <<<<<<<<<< AIRTIME & BUNDLES >>>>>>>>>>>>
        if Option == 2:
            while True:
                print(AirtimeMenu)
                Airtimepad = int(input("Option: "))
                    
                if Airtimepad == 1:
                    while True:
                        print(personel)
                        person = int(input("Option: "))
                            
                        if person == 1:
                            while True:
                                print(Dataoptions);
                                Data = int(input("Option: "))
                                if (Data == 1):
                                    Balance -= 10;
                                    Data_Bundle += 13000.12;
                                    print(f"You have purchased {13000.12}MB for Ghc{10}");
                                    back_option = int(input("Select 0 to go back: "))
                                    if back_option == 0:
                                        continue  # Goes back to the main menu loop
                                    

                                elif (Data == 2):
                                    Balance -= 15;
                                    Data_Bundle += 2000.30;   
                                    print(f"You have purchased {2000.30}MB for Ghc{15}");
                                    back_option = int(input("Select 0 to go back: "))
                                    if back_option == 0:
                                        continue  # Goes back to the main menu loop
                                
                                
                                elif (Data == 0):
                                    break  # Exit to PersonelMenu

                                else:
                                    print("Invalid option, please try again."); 
                           
                                
                        elif person == 0:
                                break  # Exit to AirtimeMenu
                            
                        else:
                                print("Invalid option, please try again.")
                                
                elif Airtimepad == 0:
                    break  # Exit to main menu
                    
                else:
                    print("Invalid option, please try again.")
                        
        elif Option == 0:
            break
                
        # else:
        #     print("Invalid option, please try again.")
        







        # <<<<<<<<<< FINANCIAL SERVICE >>>>>>>>>>>>>>>
        if Option == 3:
            print("Financial Services Not Available Now, Please Try Again Later \n0) Back")
            back_option = int(input("Select 0 to go back: "))
            if back_option == 0:
                continue
        elif Option == 0:
            break  # Return to the main menu
       
            





        # <<<<<<<<<< WALLET OPTION >>>>>>>>>>>>>>
        if Option == 4:
            while True:
                print(Wallet_menu)
                Walletpad = int(input("Option: "))

                if (Walletpad == 1):
                    print(f"Your Balance is: {Balance}\nYour Current Data: {Data_Bundle}MB\nYour current PIN: {PIN}");
                    back_option = int(input("Select 0 to go back: "))
                    if back_option == 0:
                        continue  # Goes back to the wallet menu
                elif (Walletpad == 2):
                    new_pin = int(input("Enter your new PIN: "))
                    PIN = new_pin;  # Correct assignment
                    print(f"Your New PIN is: {PIN}");
                    back_option = int(input("Select 0 to go back: "));
                    if back_option == 0:
                        continue  # Goes back to the wallet menu
                elif (Walletpad == 0):
                    break  # Exit the wallet menu and return to the main menu
                else:
                    print("Error, Try Again")
        elif Option == 0:
            break  # Return to the main menu
        
else:
    print("Invalid Keypad Number")
