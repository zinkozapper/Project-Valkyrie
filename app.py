#This is the app class where everything will come together.
#We will most likely be using pygame for the UI components.
#Please tell the other person when you start working on something so we don't have merge issues in GitHub.

#import Generator # imports other py files from the same 
import pygame
import pygame_gui
from tkinter import filedialog, Text



pygame.init() #starts py game

X = 800
Y = 600


pygame.display.set_caption('Project Valkyrie')
pygame.font.init()
window_surface = pygame.display.set_mode((X, Y))


#Background
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#568123'))
#Text
font = pygame.font.SysFont('Comic Sans MS', 32)
text = font.render('Banana', True, pygame.Color('#987ADC'), pygame.Color('#21A5E3'))
textRect = text.get_rect()
textRect.center = (200, 200)

#Manager
manager = pygame_gui.UIManager((800, 600))
#Buttons
choose_list_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 150), (100, 50)),
                                             text='Open File',
                                             manager=manager)                                                                                       
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='Say Hello',
                                             manager=manager)
generate_button_one = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 375), (150, 35)),
                                             text='Generate option 1',
                                             manager=manager)   
generate_button_two = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((550, 475), (100, 50)),
                                             text='Generate option 2',
                                             manager=manager)
generate_button_three = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 150), (100, 50)),
                                             text='Generate option 3',
                                             manager=manager)
#Text
text_display_one = pygame_gui.elements.UITextBox(relative_rect= pygame.Rect((350,150),(250, 35)),
                                             html_text='hi, this is some test text',
                                             manager=manager)
text_display_one.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_IN)                                          



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
            if event.ui_element == hello_button:
                print('Hello World!')
            if event.ui_element == choose_list_button:
                selectedFileForReading = filedialog.askopenfilename(initialdir="~", 
                title = "Select File",
                filetypes = (("Text Files","*.txt"),
                ("all files", "*.*")))
             

        manager.process_events(event)

    manager.update(time_delta)

    manager.draw_ui(window_surface)

    pygame.display.update()
