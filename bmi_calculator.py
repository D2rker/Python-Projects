height = input("enter your hieght in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight)/float(height)**2
bmi_as_int = int(bmi)
print(bmi_as_int)
if bmi_as_int < 18.5:
    print("you are under weight")
elif bmi_as_int < 25:
    print("you are normal weight")
elif bmi_as_int < 30:
    print("you are slightly over weight")
elif bmi_as_int < 35:
    print("you are obese")
else:
    print("you are clinically obese")