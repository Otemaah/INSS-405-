subjects= 11
sum=0.00
for i in range(subjects):
    score=input("Enter final score")
    sum=sum+int(score)
average=sum/11
print('Total sum', sum)
print('Average', average)

if(float(average)>90):
    print('A')
elif(float(average)>80):
    print('B')
elif(float(average)>75 and float(average)<=79):
    print('C')
elif(float(average)<60):
    print('D')
elif(float(average)<59):
    print('F')