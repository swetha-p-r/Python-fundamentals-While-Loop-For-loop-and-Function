def calculate_bmi(weight, height):
    bmi=weight/(height*height)
    return bmi
a=float(input("Enter weight in kg "))
b=float(input("Enter height in meters "))
c=calculate_bmi(a,b)
print("BMI = ",round(c,2))
