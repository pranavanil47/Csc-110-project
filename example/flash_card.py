'''
Run this programe in mu
'''

import random
def get_card(words,definitions,card_num):
    word =input('word for card' + str(card_num)+':')
    definition=input('defintion for a card'+str(card_num)+':')
    words.append(word)
    definitions.append(definition)

def print_card(content):
    length = len(content)
    print('+--'+ '-' * length +'--+')
    print('|  '+ content +'  ')
    print('+--'+ '-' * length +'--+')


def quiz(words,definitions):
    ri = random.randint(0,int(len(words)-1))
    word = words[ri]
    definition = definitions[ri]
    print_card(word)
    input('Press Enter to continue....')
    print_card(definition)
    input('Press Enter to continue....')


def main():
    words=[]
    definitions=[]
    num_cards = int(input('Enter number of flash cards to create: '))

    i = 1
    while i<=num_cards:
        get_card(words,definitions,i)
        i+=1
    while True:
        quiz(words,definitions)

main()
