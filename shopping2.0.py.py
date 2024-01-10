# Prompt the user to enter 5 items for shopping
shop1 = input('What would you like to shop? ')
shop2 = input('What else? ')
shop3 = input('One more grocery please: ')
shop4 = input('Another item for your shopping list: ')
shop5 = input('Last item for your shopping list: ')

# Function to validate and retrieve the price for the first item
def first_price():
    price1 = input(f"What is the price of {shop1}? Please remember to include 2 decimals in your answer: ")
    if len(str(price1)) > 2:
        print('Great choice')
        return price1
    else:
        print('ERROR: price must contain 2 decimals')
        exit()

# Function to validate and retrieve the price for the second item
def second_price():
    price2 = input(f"What is the price of {shop2}? Please remember to include 2 decimals in your answer: ")
    if len(str(price2)) > 2:
        print('Great choice')
        return price2
    else:
        print('ERROR: price must contain 2 decimals')
        exit()

# Function to validate and retrieve the price for the third item
def third_price():
    price3 = input(f"What is the price of {shop3}? Please remember to include 2 decimals in your answer: ")
    if len(str(price3)) > 2:
        print('Great choice')
        return price3
    else:
        print('ERROR: price must contain 2 decimals')
        exit()

# Function to validate and retrieve the price for the fourth item
def fourth_price():
    price4 = input(f"What is the price of {shop4}? Please remember to include 2 decimals in your answer: ")
    if len(str(price4)) > 2:
        print('Great choice')
        return price4
    else:
        print('ERROR: price must contain 2 decimals')
        exit()

# Function to validate and retrieve the price for the fifth item
def fifth_price():
    price5 = input(f"What is the price of {shop5}? Please remember to include 2 decimals in your answer: ")
    if len(str(price5)) > 2:
        print('Great choice')
        return price5
    else:
        print('ERROR: price must contain 2 decimals')
        exit()

# Main function to execute the program
def main():
    # Retrieve prices for each item
    price1 = first_price()
    price2 = second_price()
    price3 = third_price()
    price4 = fourth_price()
    price5 = fifth_price()

    # Store all prices in a list for easy math operations
    price_list = [float(price1), float(price2), float(price3), float(price4), float(price5)]
    sum_of_prices = round(sum(price_list), 2)
    ave_of_prices = round(sum(price_list) / len(price_list), 2)

    # Display the results
    print(f"The total cost of {shop1}, {shop2}, {shop3}, {shop4}, and {shop5} is R{sum_of_prices}, and the average price is R{ave_of_prices}.")

# Run the program
main()
