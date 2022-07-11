import pygame
import english_words
import keyboard
from keyboard import main_keyboard
from keyboard import characters
from keyboard import key_colours
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
screenwidth = 1000
keyboard.screenwidth = screenwidth
ScreenHeight = 800
keyboard.ScreenHeight = ScreenHeight
screen = pygame.display.set_mode((screenwidth,ScreenHeight))
white = (255,255,255)
index = 0
correct_key = False
total_width = 0
letter_width = []
starting_point = 200


class Timer:

    def __init__(self, minutes, adder): #starts the timer
        self.timer_seconds = 0
        self.timer_minutes = minutes
        self.timer = str(self.timer_minutes) + ':' + str(self.timer_seconds)
        self.timer_event = pygame.USEREVENT + adder

        pygame.time.set_timer(self.timer_event, 1000)

    def decreasing_timer(self): #so that when it gets to zero seconds the number of minutes goes down
        self.timer = str(self.timer_minutes) + ':' + str(self.timer_seconds)
        if self.timer_seconds == 0 and self.timer_minutes != 0:
            self.timer_seconds = 60
            self.timer_minutes -= 1
        elif self.timer_minutes == 0 and self.timer_seconds <= 0:
            self.timer = 'stop'


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
            if (len(list1)-i) < 40: #so that new words are added only if they fit on the screen
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


def checking_letter(event, letter, characters):
    new_colour = 0
    try:
        pressed_key = chr(event)
        for j in range(64):
            keyboard.key_colours[j] = ((100,100,100))
        print(event)
        if event == 8: #backspace
            keyboard.key_colours[13] = (new_colour)
        elif event == 32: #spacebar
            keyboard.key_colours[57] = (new_colour)
        elif event == 13: #enter
            keyboard.key_colours[40] = (new_colour)
        elif event == 9: #tab key
            keyboard.key_colours[14] = (new_colour)
        else:
            for i in range(len(keyboard.characters)):
                if keyboard.characters[i] == pressed_key:

                    keyboard.key_colours[i] = (new_colour)
        if pressed_key == letter:
            return True
        elif event == 8:
            return 'back'
    except:
        pass

global x
x = starting_point
total_width = 0

def main():
    global letters_on_screen
    global index
    global x
    global total_width
    screen.fill(3118019)
    typed_letter = 0
    correct_key = False
    main_keyboard()
    timer.decreasing_timer()
    writingText(('time: '+timer.timer), 0, 0, 100, 50, (0), (255,255,255), 50)


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


    for event in pygame.event.get():
        if event.type == timer.timer_event:
            timer.timer_seconds -= 1
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            correct_key = checking_letter(event.key, current_letter, keyboard.characters)

    if index != 0:
        letter_colours[(index-1)] = (101,100,100)

    if correct_key == True:
        index += 1
    elif correct_key == 'back':
        if index > 0:
            letter_colours[index-1] = white
            index -= 1

    if index == 1:
        print(index)
        pygame.time.set_timer(timer.timer_event, 1000)



    x -= total_width #so that all the letters move to the left by the width of all the letters that have already been typed
    letter_width = []
    line = 0
    for i in range(len(letters_on_screen)): #displays the letters on the screen indivusually
        if i == index:
            line = pygame.Rect(starting_point, (ScreenHeight/2), 2, 50)
        if x < 900:
            letter_width.append(writingText(letters_on_screen[i], x, (ScreenHeight/2), 40, 50, rect_colours[i], letter_colours[i], 50)[0])
            x += letter_width[i]
        if line != 0:
            pygame.draw.rect(screen, (200,0,0), line)
    x = starting_point #x is the coordinate of the first letter in the sequence
    total_width = 0
    for i in range(len(letters_on_screen)):
        if letter_colours[i] != (255,255,255): #so that for every letter that has already been typed, its colours won't be white so all the eltters will move by its width to the left.
            total_width += letter_width[i]


    pygame.draw.rect(screen, (0,0,255), (95, (ScreenHeight/2 - 30), (screenwidth-190), 110), 5)
    pygame.draw.rect(screen, (3118019), (0, (ScreenHeight/2 - 30), 95, 110))
    pygame.draw.rect(screen, (3118019), (screenwidth-95, (ScreenHeight/2 - 30), 95, 110))

    pygame.display.flip()


timer = Timer(1,1)
pygame.time.set_timer(timer.timer_event, 0) #at the start the white timer decreases every 1000 ms (1 s)

while True:
    main()
