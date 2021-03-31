grades = {}

numbers = [70,55,91,95,92,80]

for g in numbers:
    key = int((g-50)/10)
    if key not in grades:
        grades[key] = 0
    grades[key]+=1
print(grades)