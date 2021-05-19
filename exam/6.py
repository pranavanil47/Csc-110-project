import random
result = int(random.random() * 3)
numbers = {15:27, 4:7, 3:14}
for number in numbers:
    result += random.randint(number, numbers[number])
    result += 1
print(result)

number = random.randint(1, 2)
print(number)