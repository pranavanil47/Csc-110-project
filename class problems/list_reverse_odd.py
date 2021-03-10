def main():
    numbers =[1,2,3,4,5,6,7,8,9,10]

    length = len(numbers)-1

    for i in range(0,len(numbers)//2):
        numbers[i],numbers[length-i] = numbers[length - i],numbers[i]
    '''
    for i in range(0,len(numbers)-1):
        if i % 2 != 0:
            numbers.pop(i)
        
   '''
    print(numbers[9])
    print(len(numbers))    
    print(type(numbers))
    print(numbers)

main()

