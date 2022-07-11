import pygame
pygame.init()
screenwidth = 1000
ScreenHeight = 800
screen = pygame.display.set_mode((screenwidth, ScreenHeight))
characters = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '<--', 'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', 'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'Enter', 'Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Shift', 'Ctrs', 'Fn', 'Windows', 'Alt', 'Space', 'Alt', 'Ctrl', '<-', 'up', 'down', '->']
key_colours = []
for i in range(64):
    key_colours.append((100,100,100))

def makingKeyboard(width, height, x, y):
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    key_width = width/15
    key_height = height/5
    print(key_width)
    print(key_height)
    #making first row of keys
    for i in range(13):
        row1.append(pygame.Rect((x+i*key_width), y, key_width, key_height))
    row1.append(pygame.Rect((x+13*key_width), y, (2*key_width), key_height))
    #making second row of keys
    row2.append(pygame.Rect(x, (y+key_height), (1.5*key_width), key_height))
    for i in range(1,13):
        row2.append(pygame.Rect((x+i*key_width+key_width/2), (y+key_height), key_width, key_height))
    row2.append(pygame.Rect((x+13*key_width+key_width/2), (y+key_height), (1.5*key_width), key_height))
    #making third row
    row3.append(pygame.Rect(x, (y+2*key_height), (2*key_width), key_height))
    for i in range(2,13):
        row3.append(pygame.Rect((x+i*key_width), (y+2*key_height), key_width, key_height))
    row3.append(pygame.Rect((x+13*key_width), (y+2*key_height), (2*key_width), key_height))
    #making fourth row
    row4.append(pygame.Rect(x, (y+3*key_height), (2.5*key_width), key_height))
    for i in range(2,12):
        row4.append(pygame.Rect((x+i*key_width+key_width/2), (y+3*key_height), key_width, key_height))
    row4.append(pygame.Rect((x+12*key_width+key_width/2), (y+3*key_height), (2.5*key_width), key_height))
    #making fifth row
    for i in range(4):
        row4.append(pygame.Rect((x+i*key_width), (y+4*key_height), key_width, key_height))
    row4.append(pygame.Rect((x+4*key_width), (y+4*key_height), (key_width*6), key_height))
    for i in range(10,13):
        row4.append(pygame.Rect((x+i*key_width), (y+4*key_height), key_width, key_height))
    for i in range(2):
        row4.append(pygame.Rect((x+13*key_width), (y+(8+i)*(key_height/2)), key_width, (key_height/2)))
    row4.append(pygame.Rect((x+14*key_width), (y+4*key_height), key_width, key_height))

    all_keys = row1, row2, row3, row4, row5
    all_keys = list(all_keys)

    #displaying the rows
    inx = 0
    for i in range(len(all_keys)):
        for j in all_keys[i]:
            pygame.draw.rect(screen, key_colours[inx], j)
            pygame.draw.rect(screen, (255,255,255), j, 2)
            inx += 1
    return all_keys

def writingText2(text, rect, rect_colour, text_colour, size): #function for writing text. returns the width and height of text input
    textFont = pygame.font.SysFont('calibri', size)
    pygame.draw.rect(screen, rect_colour, (rect), 2)
    textDisplay = textFont.render(str(text), True, text_colour)
    textRect = textDisplay.get_rect()
    textRect.center = ((rect[0] + rect[2]/2), (rect[1] + rect[3]/2))
    screen.blit(textDisplay, textRect)

def main_keyboard():

    all_keys = makingKeyboard(1200,400,100,500)
    overall_index = 0
    for j in range(len(all_keys)):
        for i in range(len(all_keys[j])):
            writingText2(characters[overall_index], all_keys[j][i], (255,255,255), (255,255,255), 20)
            overall_index += 1

def highlighting_key(key, list1, list2):
    for i in range(list1):
        if key == list1[i]:
            list2[i]

'''
while True:
    main_keyboard()
'''
