def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price*(discount_percent/100)
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
    #    Return the original price if the discount is less than 20%
       return price

# Prompting user
original_price = float(input("Enter original price of the item:"))
discount_percentage = float(input("Enter discount percentage:"))

# Calculating the final pice using the function
final_price = calculate_discount(original_price,discount_percentage)

# Printing the final price
if final_price == original_price:
    print(f"No discount applied. The original price is:ksh{original_price:.2f}")

else:
    print(f"The final price after applying the discount is: ksh{final_price:.2f}")
