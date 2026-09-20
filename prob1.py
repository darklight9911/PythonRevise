# Requirements

# 1.     Calculate the total cost of all items in customer_cart that exist in price_catalog.
# 2.     Keep track of any items that the store does not carry in a separate list called unstocked_items.
# 3.     Print:
#     ⚬         The final total formatted to two decimal places.
#     ⚬         The list of items that could not be purchased.

# Expected Output


# Total Bill: $5.07
# Unstocked Items: ['chocolate', 'coffee']

price_catalog = {
    "apple": 0.99,
    "banana": 0.59,
    "milk": 3.49,
    "bread": 2.50,
    "eggs": 4.25,
}
customer_cart = ["apple", "banana", "apple", "chocolate", "milk", "coffee"]

total_bill = 0.0
unstocked_item = []
for i in set(customer_cart):
    if i in price_catalog:
        # print(price_catalog[i])
        total_bill = total_bill + price_catalog[i]
              
    else:
        unstocked_item.append(i)

print(f"Total Bill: ${total_bill:.2f}\n Unstocked Items: {unstocked_item}")