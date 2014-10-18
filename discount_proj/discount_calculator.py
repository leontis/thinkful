def calculate_discount(item_price,relative_discount,absolute_discount):

    discounted_price = item_price - item_price*relative_discount - absolute_discount

    if discounted_price < 0:
        raise ValueError("Price less than $0.00")
        discounted_price = 0

    return discounted_price

def main():
    item_price = 200
    relative_discount = .10
    absolute_discount = 30
    discounted_price = calculate_discount(item_price, relative_discount, absolute_discount)
    print "For original price ${:.2f} and discount rate {:.2f} and discount ${:.2f} price is ${:.2f} ".format(item_price, relative_discount, absolute_discount, discounted_price)

if __name__ == "__main__":
    main()
