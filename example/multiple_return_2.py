def compute(number):
    i = 1
    a_sum = 0
    while i <= number:
        a_sum += i
        i +=2

    return number, i , a_sum

def main():
    integer = int(input('Enter a value'))
    r1, r2, r3 = compute(integer)
    print(r1, r2, r3)

main()