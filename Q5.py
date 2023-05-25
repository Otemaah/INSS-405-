#user input size of score
size=int(input("How many Score:"))
sum=0

for i in range (size):
    num = float(input("Enter Score"))
    sum+=num
avg=sum/size
print ("You''re average score is",avg, end='')
if avg>=90 and avg<=100:
    print("You're Average Score is A")
elif avg>=80:
    print("You're Average Score is B")
elif avg>=70:
    print("You're Average Score is C")
elif avg>=60:
    print("You're Average Score is D")
elif avg>=0 and avg <60:
    print("You're Average Score is F")
else:
    print("Invalid Grade")