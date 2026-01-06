height = 1.75
weight = 80.5
BMI = weight / (height **2)
if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal weight")
elif 25 <= BMI < 28:
    print("Overweight")
elif 28 <= BMI < 32:
    print("Obesity Class I")
else:
    print("Obesity")

