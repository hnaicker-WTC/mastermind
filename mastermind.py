import random

def create_code():
    """Function that creates the 4 digit code, using random digits from 1 to 8"""

   #global code
    code = [0, 0, 0, 0]

    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value

    return code


def show_instructions():
    """Shows instructions to the user"""

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def show_results(tup_of_clues):

    print('Number of correct digits in correct place:     ' + str(tup_of_clues[0]))
    print('Number of correct digits not in correct place: ' + str(tup_of_clues[1]))


def get_answer_input():

    answer = input("Input 4 digit code: ")
    while len(answer) < 4 or len(answer) > 4: #only checks length of user input
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")

    return answer


def take_turn(answer, code):

    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1

    tup_of_clues = (correct_digits_and_position, correct_digits_only)
    #print (tup_of_clues)

    show_results(tup_of_clues)

    return tup_of_clues


def show_code(code):
    """Show Code that was created to user"""

    print('The code was: '+str(code))


def check_correctness(turns, correct_digits_and_position):
    """Checks correctness of answer and show output to user"""

    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        correct = False
        print('Turns left: ' + str(12 - turns))

    return correct


def run_game():
    
    code = create_code()
    #print (code)
    show_instructions()
    correct = False
    
    turns = 0
    while not correct and turns < 12:
        answer = get_answer_input()
        correct_digits_and_position = take_turn(answer, code)[0]
        turns += 1
        correct = check_correctness(turns, correct_digits_and_position)

    show_code(code)

if __name__ == "__main__":
    run_game()
