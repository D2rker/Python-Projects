print("Welcome to the tip calculator")
bill = float(input("what was the total bill: "))
tip = int(input("how much tip would you like to give? 0,10,15 :  "))
people = int(input("how many people to spilit the bill: "))

bill_with_tip = tip/100*bill+bill
bill_with_person = bill_with_tip/people
final_bill = round(bill_with_person, 2)
print(f"each person should pay ${final_bill}")
final_bill = "{:.2f}".format(bill_with_person)