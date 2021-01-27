from os import system, name
from random import randint


def clear():
    if name == 'nt': #Windows
        _ = system('cls')
    else: #Mac/Linux
        _ = system('clear')


def select_difficulty():
    choice = input("Please select the difficulty \
between: easy, medium, or hard...\n\
Input choice [e/m/h]: ")

    if choice.lower() == 'e':
        return('Easy.txt')
    elif choice.lower() == 'm':
        return('Medium.txt')
    elif choice.lower() == 'h':
        return('Hard.txt')
    else:
        return('Invalid')


def read_file(file_name):
    file = open(file_name, 'r')
    words = file.readlines()
    file.close()
    return(words)


def choose_word(words_list):
    index = randint(0, len(words_list)-1)
    return(words_list[index].strip())


def hide_chars(word):
    index = randint(0, len(word)-1)
    letter = word[index]
    ans = ''

    for x in range(len(word)):
        if letter == word[x]:
            ans += word[x]
        else:
            ans += '_'
    return(ans)


def run_game(word, answer):
    guesses_left = 4
    figure = '\n\n\n\n\n_______'
    message = 'Good Luck!!!'
    guessed_chars = []

    for char in answer:
        if char != '_':
            guessed_chars.append(char)

    while answer != word:
        if guesses_left < 0:
            clear()
            print("Sorry, you're out of guesses. ")
            print(figure)
            print(f"The word was: {word}")
            exit()

        clear()
        print(message)
        print(figure)    
        print(f"The word is: {answer}")    
        guess = input('Guess the missing letter: ').lower()

        if guess != 'quit' and guess != 'exit':
            if (guess in list(word)) and (guess not in list(answer)):
                message = 'Correct!'
                answer = fill_in_char(word, answer, guess)
                guessed_chars.append(guess)
            elif (guess not in guessed_chars) and (guess not in list(answer)):
                message = (f'Wrong! Number of guesses left: {guesses_left}')
                figure = draw_figure(guesses_left)
                guesses_left -= 1
                guessed_chars.append(guess)
            else:
                message = "That letter was already used! try again."
        else:
            print("Bye")
            exit()
    else:
        clear()
        print(f"Congratulations! You've completed the word.")
        print(figure)    
        print(f"The word is: {answer}") 


def fill_in_char(word, answer, char):
    for x in range(len(word)):
        if char == word[x]:
            answer = answer[:x] + char + answer[x+1:]
    return(answer)


def draw_figure(number):
    if number == 4:
        return('\n/----\n|\n|\n|\n|\n_______')
    elif number == 3:
        return('\n/----\n|   0\n|\n|\n|\n_______')
    elif number == 2:
        return('\n/----\n|   0\n|   |\n|   |\n|\n_______')
    elif number == 1:
        return('\n/----\n|   0\n|  /|\\\n|   |\n|\n_______')
    elif number == 0:
        return('\n/----\n|   0\n|  /|\\\n|   |\n|  / \\\n_______')


if __name__ == "__main__":
    clear()
    print("Welcome to Hangman.")
    words_file = select_difficulty()

    while words_file == 'Invalid':
        clear()
        print("Invalid choice. Please try again!")
        words_file = select_difficulty()

    words_list = read_file(words_file)
    chosen_word = choose_word(words_list)
    hidden_word = hide_chars(chosen_word)

    run_game(chosen_word, hidden_word)