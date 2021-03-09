

size = int(input('Enter the number of steps'))
print('')

index = 1
while index <= size:
    print('##' * index)                         ## for
                                                    ##
    index += 1                                      ####

index = 1
while index <= size:                                 ### for
    space = 2 * (size-(index))                              ##
    steps = index                                         ####

    print(' '* space +'##' * steps)

    index += 1

index = 1
while index <= size:                                 ### for pyramid
    space =  (size-index)                                ##
    steps = index                                         ####

    print(' '* space +'##' * steps)

    index += 1
