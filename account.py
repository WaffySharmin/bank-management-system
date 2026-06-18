import re
class Account:
    account_no = 0
    accounts = []
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

    def save(self):
        Account.accounts.append({
       "account_no": self.account_no,
        "name": self.name,
        "phone": self.phone,
        "email": self.email,
        "address": self.address,
        "Initial_Balance": self.Initial_Balance

        })

    def print_account_list(self):
        print(Account.accounts)

new_account1 = Account("Waffy", "01800000000", "waffysharmin@gmail.com", "Dhaka", "500")
new_account1.print_account_details()
new_account1.save()
new_account1.print_account_list()

new_account2 = Account("Illin", "01700000000", "illin@gmail.com", "Dhaka", "1000")
new_account2.print_account_details()
new_account2.save()
new_account2.print_account_list()

input_name = input("Please enter your full name: ")
input_phone = input("Please enter your phone number : ")
 



while True:
    if re.match(r"^01\d{9}$", input_phone):
        break
    else:
        print("Invalid Phone Number")
        input_phone = input("Please enter your phone number: ")

input_email = input("Please enter your email: ")

while True:
    if re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", input_email):
        break

    else:
        print("Invalid Email")
        input_email = ("Please enter your email: ")

input_address = input("Please enter your address: ")
input_balance = float(input("Please enter your initial_balance: "))

new_account1 = Account(input_name, input_phone, input_email, input_address, input_balance)
new_account1.print_account_details()
new_account1.save()
new_account1.print_account_list()

# new_account2 = Account(input_name, input_phone, input_email, input_address, input_balance)
# new_account2.print_account_details()
# new_account2.save()
# new_account2.print_account_list()