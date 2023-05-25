name = input('Enter name:')

#reverse_name = name[::1]
size=len(name)-1
print('Reversed Name:',end=' ')
for i in range(size):
    print(name[size-i], end="")
print(name[0])
#