# Build an Apply Discount Function

def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return'The price should be a number'
    elif not isinstance(discount, (int, float)):
        return'The discount should be a number'
    elif price <=0:
        return'The price should be greater than 0'
    elif discount<0 or discount>100:
        return'The discount should be between 0 and 100'
    else:
        total_1 = (price * discount) / 100
        total = price - total_1
        return total

price = int( input("Enter the item price: "))
discount = int(input("Enter the discount of that item: "))

item_price = apply_discount(price, discount)
print(f'Your item price after passing the discount is {item_price}')
