def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    print(str(bmi))

    if bmi < 18.5:
        print("Overweight")
    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
    else:
        print("Overweight")

calculate_bmi(1.73, 57)


