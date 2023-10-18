import random

product_list = []
user_list = []

def generate_random_products():
    random.seed()
    user_list.append({'username': 'dyh', 'password': '123456'})
    random_name_sequence = ['Banana', 'Apple', 'iPhone', 'Huawei', 'Xiaomi', 'Lenovo', 'Watermelon', 'Seawater']
    random.shuffle(random_name_sequence)
    for i in range(1, 9):
        product_list.append({'name': random_name_sequence[i-1], 'price': random.randint(1,100)})

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        if product not in self.items:
            self.items.append(product)
            print(f"Product added successfully: {product['name']}")

    def calculate_total_price(self):
        total_price = sum(item["price"] for item in self.items)
        return total_price

    def print_receipt(self):
        print("Shopping Cart Receipt:")
        for item in self.items:
            print(f"Product: {item['name']}, Price: {item['price']} USD")
        print(f"Total Price: {self.calculate_total_price()} USD")

def user_login():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    for user in user_list:
        if user['username'] == username and user['password'] == password:
            return True
    return False

def print_product_list():
    print("Available products:")
    for i, product in enumerate(product_list):
        print(f"{i+1}. {product['name']} - {product['price']} USD")

def main_program():
    generate_random_products()

    shopping_cart = ShoppingCart()

    login_success = user_login()
    if login_success:
        print("Login successful!")
    else:
        print("Invalid username or password. Unable to login.")
        return

    while True:
        print("\nPlease select an operation:")
        print("1. Add product to the shopping cart")
        print("2. Print shopping cart receipt")
        print("3. Exit the program")
        option = input("Please enter the option number: ")

        if option == "1":
            print_product_list()
            product_index = input("Please enter the product number: ")
            if product_index.isnumeric():
                product_index = int(product_index)
                if 1 <= product_index <= len(product_list):
                    selected_product = product_list[product_index - 1]
                    shopping_cart.add_item(selected_product)
                else:
                    print("Invalid product number. Please try again.")
            else:
                print("Invalid product number. Please try again.")
        elif option == "2":
            shopping_cart.print_receipt()
        elif option == "3":
            print("Program has exited.")
            break
        else:
            print("Invalid option. Please choose again.")

# Program entry point
main_program()