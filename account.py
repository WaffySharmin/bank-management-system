

accounts = []
class Account:
    account_no = 0
    def __init__(self, name, phone, email, address, Initial_Balance):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.Initial_Balance = Initial_Balance
        self.account_no = Account.account_no + 1
        Account.account_no = Account.account_no + 1




    def print_account_details(self):
        print("AC No", self.account_no)
        print("Name", self.name)
        print("phone", self.phone)
        print("email", self.email)
        print("address", self.address)
        print("Initial_Balance", self.Initial_Balance)

new_account = Account("Waffy", "01876543318", "waffysharmin@gmail.com", "Dhaka", "500")
new_account.print_account_details()

new_account2 = Account("Waffy2", "01876543318", "waffysharmin@gmail.com", "Dhaka", "500")
new_account2.print_account_details()

# list 
accounts.append(new_account)
accounts.append(new_account2)

for account in accounts:
    print(account)


# #object create
# main_menu = Menu("Waffy")

# #method call
# main_menu.main_menu()

