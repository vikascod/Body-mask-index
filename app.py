weigth = float(input("Enter your weigth here : "))
heigth = float(input("Enter your heigth here : "))

bmi = weigth/(heigth/100)**2

print("Your body marsk index is", bmi)

if bmi <=18.5:
    print("Your are underweight")
elif bmi <= 24.5:
    print("Your are normal")
elif bmi <=29.5:
    print("Your are overweigth")
elif bmi <=35.5:
    print("Your are obese.Start doing exsecise")
else:
    print("Your are near to die.")