# Expected Output
# Purchased Items:
#  - apple: 2 @ $1.20 = $2.40
#  - banana: 2 @ $0.50 = $1.00

# Subtotal: $3.40
# Sales Tax (8%): $0.27
# Final Total: $3.67

# Not Carried: ['coffee']
# Out of Stock: ['bread']
# Shortages: {'apple': 1}


inventory = {
    "apple": {"price": 1.20, "stock": 2},
    "banana": {"price": 0.50, "stock": 5},
    "milk": {"price": 3.50, "stock": 1},
    "bread": {"price": 2.20, "stock": 0},
}
customer_order = {
    "apple": 3,
    "banana": 2,
    "bread": 1,
    "coffee": 1,
}

not_carried = []
out_of_stock = []
shortages = {}
sub_total = 0
def display_output(name,amount,price,sub_total):
    print(f" - {name}: {amount} @ ${price:.2f} = ${sub_total:.2f}")
if customer_order:
    print("Purchased Items:")
    for item, quantity in customer_order.items():
        if item in inventory:
            stock = inventory[item]["stock"]
            price = inventory[item]["price"] 
            if quantity <= stock:
                cost = (price * quantity)
                sub_total += cost
                display_output(item,quantity,price,cost)
                cost = 0
                stock -= quantity
            elif quantity > stock:
                if stock > 0 :
                    cost = (price * stock)
                    sub_total += cost
                    display_output(item,stock,price,cost)
                    shortages[item] = (quantity - stock)
                    cost = 0
                    stock = 0
                else:
                    out_of_stock.append(item)

        else:
            not_carried.append(item)
else:
    print("Customer Order is Empty")
print(f"Subtotal: ${sub_total:.2f}")
sales_tax = (sub_total * 0.08)
print(f"Sales Tax (8%): ${sales_tax:.2f}")
total = sub_total + sales_tax
print(f"Final Total: ${total:.2f}")

print("Not Carried: ",not_carried)
print("Out of Stock: ",out_of_stock)
print("Shortages: ",shortages)
