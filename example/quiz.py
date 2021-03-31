import random
def load_questions_answers(file_name):
    qa = {}
    file = open(file_name)
    for line in file:
        line = line.strip('\n')
        components = line.split('|||')
        question  = components[0]
        answer = components[1]
        qa[question] = answer
    return qa

def get_random_question(qa):
    keys = list(qa.keys())
    index = random.randint(0,len(keys)-1)
    key = keys[index]
    return key

def ask_question(qa):
    question = get_random_question(qa)
    print(question)
    response = input('Enter your answer')
    if response == qa[question]:
        del qa[question]
        print('correct!')
        return True
    else:
        print('Wrong')
        return False

def main():
    number_of_questions = int(input('How many questions'))
    file_name = input('Enter quiz file')
    question_answers = load_questions_answers(file_name)
    marks = 0
    for i in range(number_of_questions):
        correct = ask_question(question_answers)
        if correct:
            marks +=1
    
    print('You got', marks, 'out of', number_of_questions)

main()


