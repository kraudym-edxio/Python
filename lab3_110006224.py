#Variables and user inputs
wattage = float (input("Enter wattage of device: "))
hours = float (input("Enter number of hours device was used for: "))
price_kWh = float (input("Enter the price per kWh in cents: "))

calculation = float ((wattage * hours) / (1000 * price_kWh))

#Displaying the final cost of electricity
print("Cost of electricity is: $%.2f" %calculation)
