#SUM OF NATURAL NUMBERS

no = int(input("enter of how many number you want sum: ")) #Take input from user for which number h/she want to do sum
sum = 0 #Initialize variable sum which everytime changes after loop
for i in range(1,no): #using for loop iterate from no 1 to input given by user
    sum = sum+i #add every no number with sum at each iteration and store that value again in sum
print(sum) #Finally print sum 


# SUM OF SQUARES OF NATURAL NUMBERS

no = int(input("enter of how many number you want sum: ")) #Take input from user for which number h/she want to do sum
sum = 0 #Initialize variable sum which everytime changes after loop
for i in range(1,no): #using for loop iterate from no 1 to input given by user
    sum = sum+i*i #add every no number with sum at each iteration and store that value again in sum
print(sum)

# #SUM OF EVEN NUMBER
no = int(input("enter of how many number you want sum: "))
sum = 0
for i in range(1,no):
    if i%2==0:
        sum = sum+i
print(sum)

#SUM OF ODD NUMBER
no = int(input("enter of how many number you want sum: "))
sum = 0
for i in range(1,no):
    if i%2!=0:
        sum = sum+i
print(sum)

