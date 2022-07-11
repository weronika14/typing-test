import pygame
import english_words
import keyboard
import random
from english_words import english_words_set as highest_level
pygame.init()
words_on_screen_list = []
letters_on_screen = []
typed_letters = []
screen = pygame.display.set_mode((1000,800))
colour_before = (255,255,255)

def checking_key():
    pressed_key = keyboard.read_key()
    print(pressed_key)
    if pressed_key == 'space':
        pressed_key = ' '
    elif pressed_key == 'backspace':
        return 'remove'
    return pressed_key


def find_length(list): #returns the length of a 2d array
    length = 0
    for i in range(len(list)):
        length += len(list[i])
    return length


def random_words(list1): #the parameter list1 tells you what list you're chosing from, which depends on the level of the game
    word = random.choice(tuple(list1))
    return word


def displaying_words(list1,list2): #list 1 is the list of words that is to be deplplayed on the screen, list 2 is the list of words from which words are chosen
        total_length = 0
        if list1 != []:
            for i in range(len(list1)):
                total_length += len(list1[i])
            if total_length < 20: #so that new words are added only if they fit on the screen
                return random_words(list2)
        elif list1 == []:
            return random_words(list2)

        return False


def writingText(text, x, y, width, height, rect_colour, text_colour, size): #function for writing text. returns the width and height of text input
    textFont = pygame.font.SysFont('calibri', size)

    textsize = textFont.size(text)
    width = textsize[0]

    pygame.draw.rect(screen, rect_colour, (x,y, width, height))
    textDisplay = textFont.render(str(text), True, text_colour)
    textRect = textDisplay.get_rect()
    textRect.center = ((x + width/2), (y + height/2))
    screen.blit(textDisplay, textRect)

    return textsize


def main():
    screen.fill(0)
    typed_letter = 0

    result = displaying_words(letters_on_screen, highest_level)
    for j in range(len(letters_on_screen)):
        letters_on_screen.pop(0)

    if result != False: #false will be if the list alrady has enough words so it doesnt gett appended forever. if true then the list will get appended with another random word.
        words_on_screen_list.append(result)

    for i in range(len(words_on_screen_list)):
        letters_on_screen.append(list(words_on_screen_list[i])) #splits the words into letters
        letters_on_screen.append(' ')
        current_letter = letters_on_screen[0]


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            typed_letter = checking_key()
            typed_letters.append(typed_letter)

    #print(typed_letters)

    x = 0
    for i in range(len(letters_on_screen)): #displays the letters on the screen indivusually
        for j in letters_on_screen[i]:
            letter_width, letter_height = writingText(j, x, 0, 40, 50, 0, colour_before, 50)
            x += letter_width

    x = 0
    for i in typed_letters:
            letter_width, letter_height = writingText(i, x, 100, 40, 50, 0, colour_before, 50)
            x += letter_width



    pygame.display.flip()





while True:
    main()
