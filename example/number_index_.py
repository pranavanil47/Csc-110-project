digits = input('enter any value\n')

count = 0
i = 0
while i < len(digits):
    value = int(digits[i])
    count += value
    i += 1

print('count is', count)