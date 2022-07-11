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
size = 50
colour = (0)
minutes = 0
seconds = 10


class Timer:

    def __init__(self, minutes, seconds, adder): #starts the timer
        self.timer_seconds = seconds
        self.timer_minutes = minutes
        self.timer = str(self.timer_minutes) + ':' + str(self.timer_seconds)
        self.timer_event = pygame.USEREVENT + adder
        pygame.time.set_timer(self.timer_event, 0)

    def decreasing_timer(self): #so that when it gets to zero seconds the number of minutes goes down
        if self.timer_seconds == -1 and self.timer_minutes != 0:
            self.timer_seconds = 59
            self.timer_minutes -= 1
        self.timer = str(self.timer_minutes) + ':' + str(self.timer_seconds)
        if self.timer_minutes == 0 and self.timer_seconds <= 0:
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


    pygame.draw.rect(screen, rect_colour, (x,y, width, height))
    textDisplay = textFont.render(str(text), True, text_colour)
    textRect = textDisplay.get_rect()
    textRect.center = ((x + width/2), (y + height/2))
    screen.blit(textDisplay, textRect)

    return textFont


def finding_width(text,size):
    textFont = pygame.font.SysFont('calibri', size)
    textsize = textFont.size(text)
    width = textsize[0]
    return width


def checking_letter(event, letter, characters):
    new_colour = 0
    try:
        pressed_key = chr(event)
        for j in range(64):
            keyboard.key_colours[j] = ((100,100,100))
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


def finding_speed(minutes): #returns the number of word and number of letters per minute
        minutes += seconds/60
        lpm = index/minutes
        lpm = int(lpm)

        num_words = 0
        for i in range(index):
            if letters_on_screen[i] == ' ':
                num_words += 1

        return lpm, num_words


def end_screen_slow(lpm, num_words):
        x_coordinate = screenwidth/2 - 300
        y_coordinate = ScreenHeight/2 - 200
        screen.fill((110,100,100))
        pygame.draw.rect(screen, (colour), (x_coordinate,y_coordinate,600,400))
        writingText('Letters per minute:', x_coordinate, y_coordinate, 600, 200, (colour), (255,255,255), 70)
        writingText(str(lpm), x_coordinate, (y_coordinate+200), 600, 200, (colour), (255,255,255), 70)
        writingText(str(num_words), x_coordinate, (y_coordinate+400), 600, 200, (colour), (255,255,255), 70)
        pygame.draw.rect(screen, (200,0,0), (x_coordinate,y_coordinate,600,400),3)


global x
x = starting_point
total_width = 0

def main():
    global letters_on_screen
    global index
    global x
    global total_width
    global timer
    screen.fill(colour)
    typed_letter = 0
    correct_key = False
    main_keyboard()

    if timer.timer == 'stop':
        speed = finding_speed(minutes)
        print(timer.timer_seconds)
        if speed[1] > 0:
            end_screen_slow(speed[0], speed[1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN and timer.timer_seconds < -3:
                timer = Timer(minutes,seconds,1)
            elif event.type == timer.timer_event:
                timer.timer_seconds -= 1

    else:
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
            if event.type == pygame.QUIT:
                exit()
            elif event.type == timer.timer_event:
                timer.timer_seconds -= 1

            elif event.type == pygame.KEYDOWN:
                correct_key = checking_letter(event.key, current_letter, keyboard.characters)

        if index != 0:
            letter_colours[(index-1)] = (101,100,100)

        if correct_key == True:
            if index == 0:
                pygame.time.set_timer(timer.timer_event, 1000)
            index += 1
        elif correct_key == 'back':
            if index > 0:
                letter_colours[index-1] = white
                index -= 1


        timer.decreasing_timer()
        writingText(('time: '+timer.timer), 120, 120, 240, 90, (colour), (255,255,255), 50)
        pygame.draw.rect(screen, (200,0,0), (120,120,240,90),3)



        letter_width = []
        for i in range(len(letters_on_screen)):
            letter_width.append(finding_width(letters_on_screen[i],size))
            if letter_colours[i] != (255,255,255): #so that for every letter that has already been typed, its colours won't be white so all the eltters will move by its width to the left.
                total_width += letter_width[i]




        x -= total_width #so that all the letters move to the left by the width of all the letters that have already been typed
        letters_as_text = []
        line = 0
        for i in range(len(letters_on_screen)): #displays the letters on the screen indivusually
            if i == index:
                line = pygame.Rect(starting_point, (ScreenHeight/2), 2, 50)
            if x < 900:
                letters_as_text.append(writingText(letters_on_screen[i], x, (ScreenHeight/2), letter_width[i], size, rect_colours[i], letter_colours[i], 50))
                x += letter_width[i]
            if line != 0:
                pygame.draw.rect(screen, (200,0,0), line)
        x = starting_point #x is the coordinate of the first letter in the sequence
        total_width = 0



        pygame.draw.rect(screen, (colour), (0, (ScreenHeight/2 - 30), 95, 110))
        pygame.draw.rect(screen, (colour), (screenwidth-95, (ScreenHeight/2 - 30), 95, 110))
        pygame.draw.rect(screen, (200,0,0), (95, (ScreenHeight/2 - 30), (screenwidth-190), 110), 3)




    pygame.display.flip()


timer = Timer(minutes,seconds,1)

while True:
    main()
