#Function to collect atleast 10 numbers
def input_numbers(size):
    Array = []
    for i in range (size):
        num = float(input('Enter a number:'))
        Array.append(num)
    return Array


#Function to sum numbers
def sum(array):
  Sum=0
  for i in array:
    Sum+=i
  return Sum

#Function to compute mean
def mean(array):
  avg= sum(array) / len(array)
  return avg

#Function to compute median
def median(array):
    ArraySort = sorted(array)
    size = len(ArraySort)
    #Even Array
    if size % 2 == 0:
        mid1 = ArraySort[int(size/2) - 1]
        mid2 = ArraySort[int(size/2) ]
        median = (mid1 + mid2) / 2
    else:
        median = ArraySort[int(size/ 2)]
    return median

#Invoke the Function
size=int(input('How many number you want to input to the array?: '))

#Printing the resultsCalculate mean, sum and median
print("\n***FUNCTION INPUT_NUMBER***")
array= input_numbers(size)
print("The Array is :", array)

print("\n***FUNCTION SUM***")
total = sum(array)
print("Total value in the array is:", total)


print("\n***FUNCTION MEAN***")
mean_value= mean(array)
print("Mean of the Array is:", mean_value)
print("\n***FUNCTION MEDIAN***")
median_value= median(array)
print("Median", median_value)
