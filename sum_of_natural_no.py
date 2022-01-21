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
    sum = sum+i*i #square every no number and add with sum at each iteration and store that value again in sum
print(sum)

# #SUM OF EVEN NUMBER
no = int(input("enter of how many number you want sum: ")) #Take input from user for which number h/she want to do sum
sum = 0  #Initialize variable sum which everytime changes after loop
for i in range(1,no):  #using for loop iterate from no 1 to input given by user 
    if i%2==0:  #perform operation to get even number
        sum = sum+i  #add every number with sum
print(sum)  #print sum

#SUM OF ODD NUMBER
no = int(input("enter of how many number you want sum: ")). #Take input from user for which number h/she want to do sum
sum = 0  #Initialize variable sum which everytime changes after loop
for i in range(1,no):  #using for loop iterate from no 1 to input given by user 
    if i%2!=0:  #perform operation to get odd number
        sum = sum+i  #add every number with sum
print(sum)  #print sum

