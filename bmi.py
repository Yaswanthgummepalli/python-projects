weight=int(input("enter the your weight:"))
height=int(input("enter the height in cm:"))
def bmicalculator(height,weight):
    height=height/100
    bmi=weight/(height)**2
    if bmi>18.5 and bmi<24.9:
        return (f"your bmi={bmi}\n you are having normal weight")
    elif bmi<18.5:
        return (f"your bmi={bmi}\n you are underweight")
    else:
        return (f"your bmi={bmi} \nyou are overweight")
print(bmicalculator(height,weight))    