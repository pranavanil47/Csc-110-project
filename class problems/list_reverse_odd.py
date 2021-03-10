def reverse_list(list_elements):
    reverse = list_elements[::-1]
    half_reverse = []
    for ele in range(len(reverse)):
        if ele % 2 == 1:
            half_reverse.append(reverse[ele])
    return half_reverse
def main():
    numbers =[1,2,3,4,5,6,7,8,9,10]
    half_reverse = reverse_list(numbers)
    print(half_reverse)

main()


