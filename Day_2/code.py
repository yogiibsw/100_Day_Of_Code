print("Day_2_Project_Tip_cal")


#convert input data into float
bill = float (input("What is ur tot bill: "))

#conver input data into int
tip = int(input("HOw much tip: "))

people = int(input("HOw many people to split thr bill: "))



tip_as_per = tip / 100
total_tip_amt = bill * tip_as_per
total_bill  = bill + total_tip_amt

bill_per_person = total_bill / people

final_amt = round (bill_per_person, 2)

print(f"Each should pay {final_amt} ")