import random
import itertools as it
from numpy import array
import copy

def userinput():
    choosecode = bool(input("who chooses the secret combination? no input = pc any input = you: "))
    whoguesses = bool(input("who guesses the secret combination? no input = pc, any input = you: "))
    visiblecode = bool(input("do you want the secret code to be visable? any input = yes, no input = no: "))

    print(choosecode, whoguesses, visiblecode)

    if choosecode:
        print("1 = red 2 = blue 3 = yellow 4 = green 5 = purple 6 = orange")
        int_code = input("give a 4 digit integer using the single digits from 1 to 6: ")
        if not int_code.isdigit():
            print("you entered aan invalid combination")
            return -1
        secret_code = list(map(int, str(int_code)))
        if len(secret_code) != 4:
            print("you entered aan invalid combination")
            return -1
        for i in secret_code:
            if i < 1:
                print("you entered aan invalid combination")
                return -1
            elif i > 6:
                print("you entered aan invalid combination")
                return -1

    else:
        num1 = random.randrange(1, 6, 1)
        num2 = random.randrange(1, 6, 1)
        num3 = random.randrange(1, 6, 1)
        num4 = random.randrange(1, 6, 1)
        secret_code = [num1, num2, num3, num4]

    if whoguesses:
        None
    else:
        None
    return [choosecode, whoguesses, visiblecode, secret_code]

def possiblecodes(colors, boardwidth):
    seq = range(1, colors + 1)
    possible_codes = list(it.product(seq, repeat=boardwidth))
    possible_codes_list = [list(x) for x in possible_codes]
    return possible_codes_list

def black_white(guess, secret_code, board_width):
    secretcp = secret_code.copy()
    guesscp = guess.copy()
    black = 0
    white = 0
    for i in range(board_width):
        if secretcp[i] == guesscp[i]:
            secretcp[i] = -1
            guesscp[i] = -1
            black +=1
    for i in range(board_width):
        for j in range(board_width):
            if guesscp[i] != -1:
                if guesscp[i] == secretcp[j]:
                    guesscp[i] = -1
                    secretcp[j] = -1
                    white += 1
                    j += 1
    return [black, white]

def filterpossiblecodes(guess, score, secret_code, possible_code):
    guess_cp = copy.deepcopy(guess)
    possible_cp = copy.deepcopy(possible_code)
    guess_black = score[0]
    guess_white = score[1]
    lblack = 0
    lwhite = 0
    pos_filtered = []
    for code in range(len(possible_code)):
        for num in range(4):
            if possible_cp[code][num] == guess_cp[num]:
                # print(possible_cp[code], guess_cp)
                lblack += 1
                possible_cp[code][num] = -1
                guess_cp[num] = -1
        for num_1 in range(4):
            for num_2 in range(4):
                if possible_cp[code][num_1] != -1:
                    if possible_cp[code][num_1] == guess_cp[num_2]:
                        lwhite += 1
                        possible_cp[code][num_1] = -1
                        guess_cp[num_2] = -1
        # print(possible_cp[i], guess_black, lblack, guess_white, lwhite)
        if guess_black == lblack:
            if guess_white == lwhite:
                pos_filtered.append(possible_code[code])
        lblack = 0
        lwhite = 0
        guess_cp = copy.deepcopy(guess)
    return pos_filtered



def alphabetical_guess(secret_code, possible_inputs):
    tries = 1
    while tries < 10:
        guess = possible_inputs[0]
        score = black_white(guess, secret_code, 4)
        print("score = ", score)
        if score != [4, 0]:
            possible_inputs = filterpossiblecodes(guess, score, secret_code, possible_inputs)
            tries += 1
        else:
            print(f"you have won with {tries} tries")
            print(f"the code was{secret_code}")
            return 1



def userguesses(secret_code):
    number_of_guesses = 8
    while number_of_guesses > 0:
        guess = str(input("enter a 4 digit integer to guess"))
        if not guess.isdigit():
            print("you entered aan invalid combination")
            return -1
        guess = list(map(int, str(guess)))
        if len(guess) != 4:
            print("you entered aan invalid combination")
            return -1
        for i in guess:
            if i < 1:
                print("you entered aan invalid combination")
                return -1
            elif i > 6:
                print("you entered aan invalid combination")
                return -1
        guess_rating = black_white(guess, secret_code, 4)
        print(f"{guess_rating[0]} pin(s) are placed in the correct place with the correct color")
        print(f"{guess_rating[1]} pin(s) are placed in the wrong place with the correct color")
        if guess_rating[0] == 4:
            print("you won!")
            return 0
        number_of_guesses -= 1




def main():
    NUMBER_OF_COLORS = 6
    BOARD_WIDTH = 4
    uinput = userinput()
    pos = possiblecodes(NUMBER_OF_COLORS, BOARD_WIDTH)
    if uinput[1]:
        userguesses(uinput[3])
    else:
        alphabetical_guess(uinput[3], pos)
main()

