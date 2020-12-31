import random

numbers = [random.randrange(1, 100, 1) for i in range(100)]#giving random numbers to the prisoners
mission_numbers = list(range(100))#giving each prisoner a mission number
sum = sum(numbers)#calculating the total sum 
partial_sums =[]
for num in numbers:
    partial_sums.append(sum - num)#each prisoner calculate the sum of all the numbers accept his own

guess =[]
for i, num in enumerate(numbers):
    x = mission_numbers[i] - partial_sums[i] % 100#each prisoner calculate what number he should guess
    if x < 0:
        x += 100
    guess.append(x)
    
for i, num in enumerate(numbers):#checking if one prisoner guessed right
    if num == guess[i]:
        print("prisoner {} got the number {} and guessed {}".format(i, num, guess[i]))