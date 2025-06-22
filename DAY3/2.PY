# atm code with getter and setters

class Atm:
    def __init__(self):
        self.__pin = ''       #attribute ko private banane ka liya => double underscore.
        self.__balance = 0   
        self.menu()

    def pin(self):
        return self.__pin

    def pin(self, new_pin):
        if isinstance(new_pin, str) and new_pin.isdigit() and len(new_pin) == 4:
            self.__pin = new_pin
        else:
            raise ValueError("PIN must be a 4-digit string.")

    def balance(self):
        return self.__balance

    def balance(self, amount):
        if isinstance(amount, (int, float)) and amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance must be a positive number.")

    def menu(self):
        user_input = input("""
            Hi! How can I help you?
            1. Press 1 to create PIN.
            2. Press 2 to change PIN.
            3. Press 3 to check balance.
            4. Press 4 to withdraw money.
            5. Exit.
            """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("Enter your 4-digit PIN: ")
        self.pin = user_pin  # Uses the setter (validates PIN)

        user_balance = float(input("Enter your initial balance: "))
        self.balance = user_balance  # Uses the setter (validates balance)

        print("PIN created successfully!")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter old PIN: ")
        if old_pin == self.pin:  # Uses the getter
            new_pin = input("Enter new 4-digit PIN: ")
            self.pin = new_pin    # Uses the setter
            print("PIN changed successfully!")
        else:
            print("Incorrect PIN. Access denied.")
        self.menu()

    def check_balance(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:  # Uses the getter
            print(f"Your balance is: {self.balance}")  # Uses the getter
        else:
            print("Incorrect PIN. Access denied.")
        self.menu()

    def withdraw(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:  # Uses the getter
            amount = float(input("Enter amount to withdraw: "))
            if amount <= self.balance:  # Uses the getter
                self.balance -= amount  # Uses the setter
                print(f"Withdrawal successful! New balance: {self.balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Incorrect PIN. Access denied.")
        self.menu()


# Run the ATM
atm = Atm()