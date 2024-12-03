#First Item added
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

#Price assigned for our Item
lovely_loveseat_price = 254.00

#Second Item added
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

#Price assigned for our second item
stylish_settee_price = 180.50

#Third Item
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

#Price assigned to third item
luxurious_lamp_price = 52.15

#Sales Taxes variable that's 8.8%
sales_tax = .088

#First Customer
customer_one_total = 0

#Descriptions of the items that is purchasing
customer_one_itemization = ""

#Add Items
customer_one_itemization += lovely_loveseat_description + "\n"
customer_one_itemization += luxurious_lamp_description

#First purchase
customer_one_total = lovely_loveseat_price + luxurious_lamp_price

#Calculating sales tax
customer_one_tax = customer_one_total * sales_tax

#Add the sales tax to the customer’s total cost.
customer_one_total += customer_one_tax

print("Customer One Items:\n")
print(customer_one_itemization)
print("\nCustomer One Total:")
print(customer_one_total)
