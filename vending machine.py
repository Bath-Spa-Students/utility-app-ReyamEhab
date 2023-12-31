# Menu of the things that will be purchased.
class VendingMachine:
    def __init__(self):
        self.menu = {
            'drinks ☕ ': {
                'A1': {'name': 'Arabian Coffee', 'price': 3.00, 'quantity': 5},
                'A2': {'name': 'Cappuccino', 'price': 2.00, 'quantity': 10},
                'A3': {'name': 'Coffee', 'price': 1.00, 'quantity': 20},
                'A4': {'name': 'Karak tea', 'price': 1.50, 'quantity': 31},
            },
# Nested dictionary for Snacks.
            'snacks 🍫 ': {
                'B1': {'name': 'Popcorn', 'price': 1.00, 'quantity': 5},
                'B2': {'name': ' Dark Chocolate', 'price': 1.25, 'quantity': 7},
                'B3': {'name': 'Chips', 'price': 3.50, 'quantity': 10},
                'B4': {'name': 'Cup cake', 'price': 2.00, 'quantity': 5},
            },
# Nested dictionary to store items in the stock.
            'Soft drinks 🥤 ': {
                'C1': {'name': 'Cola', 'price': 3.00, 'quantity': 3},
                'C2': {'name': 'Fanta', 'price': 3.00, 'quantity':  4},
                'C3': {'name': 'orange juice', 'price': 1.50, 'quantity': 10},
                'C4': {'name': 'Apple juice', 'price': 1.50, 'quantity': 10},
            },
        }
        self.balance = 0.0


        # Welcoming message.
    def display_items(self, category):
        print(f"""

▒█░░▒█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 　 █▀▄▀█ █░░█ 　 ▀█░█▀ █▀▀ █▀▀▄ █▀▀▄ ░▀░ █▀▀▄ █▀▀▀ 
▒█▒█▒█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀ 　 ░░█░░ █░░█ 　 █░▀░█ █▄▄█ 　 ░█▄█░ █▀▀ █░░█ █░░█ ▀█▀ █░░█ █░▀█ 
▒█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀ 　 ░░▀░░ ▀▀▀▀ 　 ▀░░░▀ ▄▄▄█ 　 ░░▀░░ ▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀ ▀░░▀ ▀▀▀▀ 

█▀▄▀█ █▀▀█ █▀▀ █░░█ ░▀░ █▀▀▄ █▀▀ 
█░▀░█ █▄▄█ █░░ █▀▀█ ▀█▀ █░░█ █▀▀ 
▀░░░▀ ▀░░▀ ▀▀▀ ▀░░▀ ▀▀▀ ▀░░▀ ▀▀▀
              
    """)
        print("Available Items:")
        # Iterate through items in the specified category and display their details
        for code, item in self.menu[category].items():
            print(f"{code}: {item['name']} - 💵 {item['price']:.2f} (Qty: {item['quantity']})")
        print("""\nＹｏｕｒ ｃｕｒｒｅｎｔ ｂａｌａｎｃｅ: 💵 {:.2f}""".format(self.balance))


    # Define a method to insert money into the vending machine
    def insert_money(self):
        while True:
            try:
                # Prompt the user to input the amount of money
                amount = float(input("""Ｉｎｓｅｒｔ ｍｏｎｅｙ (ｅｎｔｅｒ ０ ｔｏ ｃａｎｃｅｌ): 💵"""))
                # Check if the amount is positive
                if amount < 0:
                    print("""Ｐｌｅａｓｅ ｅｎｔｅｒ ａ ｐｏｓｉｔｉｖｅ ａｍｏｕｎｔ.""")
                # Check if the user wants to cancel the operation
                elif amount == 0:
                    break
                else:
                    # Update the balance and display the updated balance
                    self.balance += amount
                    print("Balance updated. Your current balance: 💵 {:.2f}".format(self.balance))
                    break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")


    # Define a method to purchase an item from the vending machine
    def purchase_item(self, category, code):
        # Check if the item code is valid
        if code in self.menu[category]:
            # Retrieve the item details
            item = self.menu[category][code]
            # Check if the item is in stock and the balance is sufficient
            if item['quantity'] > 0 and self.balance >= item['price']:
                # Update the balance, reduce the quantity, and inform the user of the successful purchase
                self.balance -= item['price']
                item['quantity'] -= 1
                print("""Ｙｏｕ'ｖｅ ｓｕｃｃｅｓｓｆｕｌｌｙ ｐｕｒｃｈａｓｅｄ {}. Enjoy!""".format(item['name']))
            # If the item is out of stock, inform the user
            elif item['quantity'] == 0:
                print(""" 😢 Ｓｏｒｒｙ, {} ｉｓ ｏｕｔ ｏｆ ｓｔｏｃｋ.""".format(item['name']))
            # If the balance is insufficient, prompt the user to insert more money
            else:
                print("Insufficient funds. Please insert more money.❌ ")
        else:
            # If the item code is invalid, inform the user
            print("Invalid item code. Please try again. ❌ ")


    # Define a method to start the vending machine
    def start(self):
        while True:
            # Display the category options to the user
            print("""Ｓｅｌｅｃｔ ｃａｔｅｇｏｒｙ:""")
            print("""１. Ｄｒｉｎｋｓ ☕ """)
            print("""２. Ｓｎａｃｋｓ 🍫 """)
            print("""３. Ｓｏｆｔ ｄｒｉｎｋｓ 🥤 """)
            print("""Ｅｎｔｅｒ 'ｅｘｉｔ' ｔｏ ｅｎｄ.""")
            # Prompt the user to enter their choice
            choice = input("Ｅｎｔｅｒ ｙｏｕｒ ｃｈｏｉｃｅ (１, ２, ３ ｏｒ 'ｅｘｉｔ'): ")
            # Check the user's choice and set the category accordingly
            if choice.lower() == 'exit':
                print("""𝚃𝚑𝚊𝚗𝚔 𝚢𝚘𝚞 𝚏𝚘𝚛 𝚞𝚜𝚒𝚗𝚐 𝚝𝚑𝚎 𝙲𝚛𝚎𝚊𝚝𝚒𝚟𝚎 𝚅𝚎𝚗𝚍𝚒𝚗𝚐 𝙼𝚊𝚌𝚑𝚒𝚗𝚎. 𝙷𝚊𝚟𝚎 𝚊 𝚐𝚛𝚎𝚊𝚝 𝚍𝚊𝚢! 👋 """)
                break
            elif choice == '1':
                category = 'drinks ☕ '
            elif choice == '2':
                category = 'snacks 🍫 '
            elif choice == '3':
                category = 'Soft drinks 🥤 '
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 'exit'.")
                continue


            # Display the items in the selected category
            self.display_items(category)
            # Allow the user to insert money
            self.insert_money()
            # Prompt the user to enter the code of the item they want to purchase
            item_code = input("Enter the code of the item you want to purchase: ")
            # Process the purchase based on the selected category and item code
            self.purchase_item(category, item_code)


# Check if the script is being run as the main program
if __name__ == "__main__":
    # Create an instance of the VendingMachine class
    vending_machine = VendingMachine()
    # Start the vending machine
    vending_machine.start()







