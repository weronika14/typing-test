import pygame
import english_words
import keyboard
import random
from english_words import english_words_lower_set as highest_level
pygame.init()
words_on_screen_list = []
global letters_on_screen
letters_on_screen = []
typed_letters = []
word_colours = []
letter_colours = []
rect_colours = []
screen = pygame.display.set_mode((1000,800))
white = (255,255,255)
index = 0
correct_key = False
total_width = 0
letter_width = []

def find_length(list): #returns the length of a 2d array
    length = 0
    for i in range(len(list)):
        length += len(list[i])
    return length


def random_words(list1): #the parameter list1 tells you what list you're chosing from, which depends on the level of the game
    word = random.choice(tuple(list1))
    return word


def displaying_words(list1,list2,i): #list 1 is the list of words that is to be deplplayed on the screen, list 2 is the list of words from which words are chosen
        if list1 != []:
            if (len(list1)-i) < 20: #so that new words are added only if they fit on the screen
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


def checking_letter(event, letter):
    try:
        pressed_key = chr(event)
        if pressed_key == letter:
            return True
        elif event == 8:
            return 'back'
    except:
        pass

global x
x = 100
total_width = 0
def main():
    global letters_on_screen
    global index
    global x
    global total_width
    screen.fill(0)
    typed_letter = 0
    correct_key = False


    #this section of code is resonsible for appending the list of words if needed and changing it to a list of letters
    result = displaying_words(letters_on_screen, highest_level, index)
    if result != False: #false will be if the list alrady has enough words so it doesnt gett appended forever. if true then the list will get appended with another random word.
        words_on_screen_list.append(result)
        word_colours.append(white)
        repeat = len(words_on_screen_list)-1
        repeat = len(words_on_screen_list[repeat])
        for i in range(repeat):
            letter_colours.append(white)
            rect_colours.append(0)
        letter_colours.append(white)
        rect_colours.append(0)
    words = ' '.join(words_on_screen_list)
    letters_on_screen = list(words)

    current_letter = letters_on_screen[index]
    if index != 0:
        letter_colours[(index-1)] = (101,100,100)
        rect_colours[(index-1)] = (0)
    rect_colours[index] = (100,0,0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            correct_key = checking_letter(event.key, current_letter)


    if correct_key == True:
        index += 1

    elif correct_key == 'back':
        index -= 1
        rect_colours[(index+1)] = (0)
        letter_colours[index+1] = white
        letter_colours[index] = white


    x -= total_width #so that all the letters move to the left by the width of all the letters that have already been typed.
    letter_width = []
    for i in range(len(letters_on_screen)): #displays the letters on the screen indivusually
        letter_width.append(writingText(letters_on_screen[i], x, 0, 40, 50, rect_colours[i], letter_colours[i], 50)[0])
        x += letter_width[i]
    x = 100 #x is the coordinate of the first letter in the sequence
    total_width = 0
    for i in range(len(letters_on_screen)):
        if letter_colours[i] != (255,255,255): #so that for every letter that has already been typed, its colours won't be white so all the eltters will move by its width to the left.
            total_width += letter_width[i]


    pygame.display.flip()


'''
while True:
    main()
'''
