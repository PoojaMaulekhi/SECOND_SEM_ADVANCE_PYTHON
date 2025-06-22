# ATM PIN WITH HELP OF constructor 
class Atm:

    def __init__(self):
        self.pin=' '
        self.balance=0
        self.menu()
    
    def menu(self):
        user_input=input("""
                         Hi How can I help you?
                         1.Press 1 to create pin.
                         2.Press 2 to change Pin.
                         3.Press 3 to check Balance.
                         4.Press 4 to withdraw money.""")
        
        if user_input=='1':
            self.create_pin()
    
        elif user_input=='2':
            self.change_pin()
    
        elif user_input=='3':
            self.check_balance()
    
        elif user_input=='4':
            self.withdraw()
    
        else:
            exit()

    def create_pin(self): #pin create 
        user_pin = input('enter your pin')
        self.pin=user_pin
        
        user_balance = input('enter your balance')
        self.balance=user_balance

        print('pin created succesfully')

        self.menu()



    def change_pin(self):
        old_pin = input("Enter old pin")
        if old_pin ==  self.pin: # main condition to check pin change.
            new_pin=input("Enter new pin")
            self.pin = new_pin
            print("Pin change successfully")
            self.menu()

        else:
            print("nai karna de sakta")
            self.menu()



    def check_balance(self):
        user_pin = input('Enter your pin')
        if user_pin == self.pin:
            print("Your balance is " , self.balance)
        else:
            print('Chal nikal yahan seh')

        def withdraw(self):
            user_pin=input("Enter the pin")
            if user_pin== self.pin:
                amount = int(input("Enter your Amount"))
                if amount<= self.balance:
                    self.balance = self.balance - amount
                    print("withdrawal successfully balance is", self.balance)

                else:   
                    print("garib")
            else:
                print('Chor')
            self.menu()


obj1=Atm()