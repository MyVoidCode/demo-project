# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit**3
    temp //= 10

print("The sum of the cubes of the digits is:", sum)
print("The original number is:", num)

if num == sum:
    print("So the given number", num, "is an Armstrong number")
else:
    print("So the given number", num, "is not an Armstrong number")
