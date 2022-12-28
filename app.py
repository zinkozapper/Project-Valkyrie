#This is the app class where everything will come together.
#We will most likely be using pygame for the UI components.
#Please tell the other person when you start working on something so we don't have merge issues in GitHub.

import pygame
import pygame_gui
from tkinter import filedialog, Text
from pathlib import Path
import random
import linecache

localPath = Path(__file__).absolute().parent

def makeGen(reader): #Is used by rawGenCount
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024*1024)

def rawGenCount(filename): #Determines # of lines in file
    f = open(filename, 'rb')
    f_gen = makeGen(f.raw.read)
    return sum( buf.count(b'\n') for buf in f_gen ) 
    
    
def genWord(length = 'Custom', wordList = localPath/'wordlist_long.txt'): #Generates a word of long, medium, or short length
    
    if (length=='long'):
        wordList = localPath/'wordlist_long.txt'     
    if(length=='medium'):
        wordList = localPath/'wordlist_medium.txt'
    elif(length=='short'):
        wordList = localPath/'wordlist_short.txt'
    elif(length=='Custom'):
        pass
     
    rnum = random.randrange(1,rawGenCount(wordList))
    return linecache.getline(str(wordList),rnum).rstrip('\n') # grabs word from line and removes \n

def multiGenWord(wc,length): # returns a list of words
    rels = []
    for i in range (wc):
        rels.append([genWord(length)])
    return[rels]






def main():
    pygame.init() #starts py game

    X = 800
    Y = 600

    wordlistLocation = ""


    pygame.display.set_caption('Project Valkyrie')
    pygame.font.init()
    window_surface = pygame.display.set_mode((X, Y))


    #Background
    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#050000'))
    #Text
    font = pygame.font.SysFont('Comic Sans MS', 32)
    text = font.render('Banana', True, pygame.Color('#050000'), pygame.Color('#21A5E3'))
    textRect = text.get_rect()
    textRect.center = (200, 200)

    #Manager
    manager = pygame_gui.UIManager((800, 600))
    #Buttons
    choose_list_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((15, 550), (250, 35)),
                                                text='Select Custom Word List',
                                                manager=manager)
                                                                                        
    generate_button_one = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((75, 282), (200, 35)),
                                                text='Generate short word',
                                                manager=manager)   
    generate_button_two = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 282), (200, 35)),
                                                text='Generate medium word',
                                                manager=manager)
    generate_button_three = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((525, 282), (200, 35)),
                                                text='Generate long word',
                                                manager=manager)
    generate_button_four = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((188, 332), (200, 35)),
                                                text='Generate 3 words',
                                                manager=manager)
    generate_button_five = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((413, 332), (200, 35)),
                                                text='Generate 5 words',
                                                manager=manager)
    generate_Custom = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((290, 550), (200, 35)),
                                                text='Generate from Custom',
                                                manager=manager)

    #Text
    title_text = pygame_gui.elements.UITextBox(relative_rect= pygame.Rect((275,15),(250, 35)),
                                                html_text='Welcome to Project Valkyrie',
                                                manager=manager)
    subtitle_text = pygame_gui.elements.UITextBox(relative_rect= pygame.Rect((250,55),(300, 35)),
                                                html_text='An english essay prompt generator',
                                                manager=manager)
    wordOutput = pygame_gui.elements.UITextBox(relative_rect= pygame.Rect((200,130),(400, 35)),
                                                html_text='',
                                                manager=manager)
    #title_text.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_IN)   
    #wordOutput.set_active_effect(pygame_gui.TEXT_EFFECT_TILT)                                       


    generate_Custom.visible=False

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60)/1000.0
        window_surface.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            
            #UI Button clicks
            if event.type == pygame_gui.UI_BUTTON_PRESSED: 
                #File selector button
                if event.ui_element == choose_list_button:
                    selectedFileForReading = filedialog.askopenfilename(initialdir="~", 
                    title = "Select File",
                    filetypes = (("Text Files","*.txt"),
                    ("all files", "*.*")))
                    generate_Custom.visible=True
                    
                #Genertate Buttons
                if event.ui_element == generate_button_one:
                    wordOutput.set_text(genWord('short'))
                if event.ui_element == generate_button_two:
                    wordOutput.set_text(genWord('medium'))
                if event.ui_element == generate_button_three:
                    wordOutput.set_text(genWord('long'))
                if event.ui_element == generate_button_four:
                    textStr = genWord('medium') + " " + genWord('short') + " " + genWord('long')
                    wordOutput.set_text(textStr) 
                if event.ui_element == generate_button_five:
                    textStr = genWord('medium') + " " + genWord('short') + " " + genWord('long') + " " + genWord('short') + " " + genWord('long')
                    wordOutput.set_text(textStr) 
                    
                #Custom generate button    
                if event.ui_element == generate_Custom:
                    if not '.txt' in selectedFileForReading:
                        wordOutput.set_text("Please select valid .txt file!") 
                    else:
                        wordOutput.set_text(genWord('Custom', selectedFileForReading))

                
                

            manager.process_events(event)

        manager.update(time_delta)

        manager.draw_ui(window_surface)

        pygame.display.update()


if __name__ == '__main__':
    main()