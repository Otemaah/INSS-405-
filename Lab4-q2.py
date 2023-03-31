# Hot = >= 50
# warm = 30 - 50
# cold = 0 - 30
# Extreme_cold = <0

temperature = 5

for i in range(temperature):
    temperature = int(input("enter temperature: "))
    if(int(temperature)) >= 50:
        print("Hot")
    elif(int(temperature) >=30 and int(temperature) <50):
        print("warm")
    elif(int(temperature) >=0 and int(temperature) <30):
        print("cold")
    elif(int(temperature) <0):
        print("Extreme cold")