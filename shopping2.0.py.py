shop1 = input('What would you like to shop?')
shop2 = input('What else?')
shop3 = input('One more grocery please:')

#check each requested price if there is at least 2 decimals by using the length of string
#if there are not any deciamls, program terminates
def first_price():
    price1 = input(f"What is the price of {shop1}? Please remember to include 2 decimals to your answer." )
    if len(str(price1)) > 2:
        print('Great choice')
        return price1
    else:
        print('ERROR: price must contain 2 decimals')
        exit()


def second_price():
    price2 = input(f"What is the price of {shop2}? Please remember to include 2 decimals to your answer." )
    if len(str(price2)) > 2:
        print('Great choice')
        return price2
    else:
        print('ERROR: price must contain 2 decimals')
        exit()

def third_price():
    price3 = input(f"What is the price of {shop3}? Please remember to include 2 decimals to your answer." )
    if len(str(price3)) > 2:
        print('Great choice')
        return price3
    else:
        print('ERROR: price must contain 2 decimals')
        exit()

def main():

    price1 = first_price()
    price2 = second_price()
    price3 = third_price()

    #store all prices in a list to use easy math functions
    price_list = [float(str(price1)), float(str(price2)), float(str(price3))]
    sum_of_prices = round(sum(price_list), 2)
    ave_of_prices = round(sum(price_list) / 3, 2)


    print(sum_of_prices)
    print(ave_of_prices)
    print(f"The Total of {shop1}, {shop2}, {shop3} is R{sum_of_prices} and the average price of the items are R{ave_of_prices}.")

main()