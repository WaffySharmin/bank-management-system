

#Only class (Logic/Structure)
class Menu:
    def __init__(self, dev_name):
        self.name = dev_name
    

   
    def heading(Self):
        print(f"{'-'*60}")
        print("\n---------BANK ACCOUNT MANAGEMENT SYSTEM ---------")
        print("\n---------       Developed by- Waffy     ---------")
        print(f"{'-'*60}")

    def main_menu(self):
        self.heading()

        print("\n---------MAIN MENU---------")
        print("1. Create New Account ")
        print("2. Deposit Money")
        print("3. Withdraw Money ")
        print("4. Transfer Money ")
        print("4. View Account Details ")
        print("6. Display All Accounts ")
        print("7. Delete Account ")
        print("8. Exit ")


# #object create
# main_menu = Menu("Waffy")

# #method call
# main_menu.main_menu()
