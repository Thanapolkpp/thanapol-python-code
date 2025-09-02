weight = float(input("What is your weight (KG) :"))
height = float(input("What is your height  (M) :"))

bmi = weight/(height**2)

if bmi >=30.00 :
    print("above: Obese")
elif bmi>25.5 and bmi<=29.9  :
    print("Overweight")
elif bmi>=18.50 and bmi <=24.9 :
    print("Normal weight")
else :
    print("Underweight")

print(f"You Bmi is {bmi:.1f}")


