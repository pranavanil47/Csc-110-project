'''
this program is an example of multiple return
'''

def check_num(a, b):
    if a >= b:
        return a, b
    return b,
def main():
    age1 = input('Enter an age')
    age2 = input('enter an age')
    result_1, result_2 = check_num(age1, age2)

    print(result_1, result_2)

main()

