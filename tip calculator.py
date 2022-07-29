print("Welcome to the tip calculator")
bill = float(input("What was the total bill?  $"))
tip = int(input("How much tip would you like to give? 10, 12, 15?"))
people = int(input("How many people to split the bill?"))
total_tip = tip / 100 * bill + bill
total_bill = total_tip / people 
final_amount = round(total_bill, 2)
print(f"Each person should pay: ${final_amount}")
