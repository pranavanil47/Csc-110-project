def multiply(numbers):
    count = 1
    i = 0
    while i < len(numbers):
        count *= numbers[i]
        i+=1
    return count
    