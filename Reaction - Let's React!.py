#Dhruvi Patel
#The Ultimate Chemistry Study Guide: Reaction? Let's React!

"""
The purpose of this program is to
provide advanced chemistry lessons
alongside review through the practice
questions given.
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 95, 0)
YELLOW = (255, 255, 0)
TURQUOISE = (77, 255, 195)
pygame.init()

# Set the width and height of the screen [width, height]
size = (1000, 750)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Chemistry Study Guide")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Introduction Screen (user will be able to go to back to menu from ever other screen, but not this screen).
screen_number = 0

#Images for Chapter 1 - Unit 1 - Isotopes
isotopes = pygame.image.load("Isotopes.jpg").convert()
isotope_example1 = pygame.image.load("Isotope - Example 1.jpg").convert()
isotope_example2 = pygame.image.load("Isotope - Example 2.jpg").convert()

#Images for Chapter 2 - Unit 1 - Trends
periodic_trends = pygame.image.load("Periodic Trends.jpg").convert()
ar_ie = pygame.image.load("Atomic Radius & Ionization Energy.jpg").convert()
ea_en = pygame.image.load("Electron Affinity & Electronegativity.jpg").convert()

#Images for Chapter 1 - Unit 2 - Reactions: Synthesis & Decomposition
synthesis = pygame.image.load("Synthesis.jpg").convert()
decomposition = pygame.image.load("Decomposition.jpg").convert()

#Images for Chapter 2 - Unit 2 - Reactions: Single Displacement & Double Displacement
single_d = pygame.image.load("Single Displacement.jpg").convert()
double_d = pygame.image.load("Double Displacement.jpg").convert()

#Images for Chapter 1 - Unit 3 - Acids & Bases
acid_properties = pygame.image.load("Acids -  Properties.jpg").convert()
acid_definitions = pygame.image.load("Acids - Basic Definitions.jpg").convert()
acid_hydrogen = pygame.image.load("Acids - True Nature of Hydrogen.jpg").convert()
base_properties = pygame.image.load("Bases - Properties.jpg").convert()
base_definitions = pygame.image.load("Bases - Basic Definitions.jpg").convert()

#Images for Chapter 2 - Unit 3 - pH/pOH & Titration
pH = pygame.image.load("pH.jpg").convert()
pOH = pygame.image.load("pOH.jpg").convert()
pH_scale = pygame.image.load("pH Scale.jpg").convert()
titration_definitions = pygame.image.load("Titration - Basic Definitions.jpg").convert()


#These are the questions in Unit 1.
unit1_questions = ["1. Isotopes differ in _______, not atomic number. A: Mass. B: Volume. C: Density. D: Temperature.",
                   "2. Calculate the atomic weight of Mg.  Given: 24Mg - 78.80% (23.98504 u), 25Mg - 10.13% (24.98584 u), "
                   "and 26Mg - 11.17% (25.98259 u). A: 18.95u. B: 20.22u. C: 24.31. D:10.54u.",
                   "3. Atomic Mass is the _______. A: Superscript. B: Subscript. C: Element. D: None.",
                   "4. ENC stands for? A: Element Compound. B: Effective Nuclear Charge. C: Efficient Net Charge. D: None.",
                   "5. Sr has a higher Electron Affinity than S. A: True. B: False.",
                   "6. Sr has a lower Electronegativity than S. A: True. B: False.",
                   "7. First Ionization is the _______ required to remove an electron from an atom in its gaseous state. "
                   "A: Force. B: Number. C: Pressure. D: Energy."]

#These are the questions in Unit 2.
unit2_questions = ["1. Which of the following are types of reactions: A: Synthesis. B: Decomposition. C. Single Displacement. D: All.",
                   "2. What is this reaction: BaCO3  ---> BaO + CO2. A: Synthesis. B: Double Displacement. C: Decomposition. D: Combustion.",
                   "3. You can tell a chemical reaction because it always produces. A: Different Substance. B: State Change. C: Reactants. D: Water.",
                   "4. What is this reaction: Pb(NO3)2 + 2 KI ---> PbI2 + 2 KNO3. A: Decomposition. B: Double Displacement. C: Synthesis. D: Combustion.",
                   "5. What would NOT be expected in a double displacement reaction? A: Gas. B: Water. C: Precipitate. D: None.",
                   "6. What is the product of a Neutralization reaction? A: Water. B: Salt. C: Acid. D: Salt & Water.",
                   "7. What is this reaction: Mg + 2 HCl ---> MgCl2 + H2. A: Decomposition. B: Double Displacement. C: Single Displacement. D: Combustion."]

#These are the questions in Unit 3.
unit3_questions = ["1. What is strong acid? A: Al. B: C. C: HCl. D: None.",
                   "2. A strong base dissociates completely. A weak base dissociates partially. A: True. B: False.",
                   "3. -log(OH-) concentration is not the pOH equation. A: True. B: False.",
                   "4. What is -log(H+) concentration? A: pOH equation. B: Concentration. C: Hydrogen. D: pH equation.",
                   "5. What changes in color depending on the pH of the solution called? A: Liquid. B: Solution. C: Acid-Base Indicator. D: None.",
                   "6. In titration, where does a marked color change take place? A: Transition. B: End-Point. C: Equivalency Point. D: Dilution.",
                   "7. The amount of solute that is dissolved in a solution is? A: Concentration. B: Dilution. C: Saturation. D: Titration."]

# Draws a red rectangle on multiple screens.
def red_border():
    pygame.draw.rect(screen, RED, [50, 50, 900, 650], 6)

# Draws a blue rectangle on multiple screens.
def blue_border():
    pygame.draw.rect(screen, BLUE, [50, 50, 900, 650], 6)

#A menu rectangle is displayed.
def menu_button():
    pygame.draw.rect(screen, WHITE, [840, 60, 100, 50], 4)
    font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
    menu_back = font_menu_back.render("MENU", True, WHITE)
    screen.blit(menu_back, [849, 65])

#If user clicks the right box, "CORRECT" shows up.
def correct_box():
    pygame.draw.rect(screen, GREEN, [790, 640, 150, 50], 4)
    font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
    menu_back = font_menu_back.render("CORRECT", True, GREEN)
    screen.blit(menu_back, [798, 645])

#If user clicks the wrong box, "ANSWER: " shows up.
def answer_box():
    pygame.draw.rect(screen, TURQUOISE, [760, 640, 180, 50], 4)

#If the user wants to go to the next screen, a "NEXT" button is displayed.
def next():
    pygame.draw.rect(screen, WHITE, [60, 60, 100, 50], 4)
    font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
    menu_back = font_menu_back.render("NEXT", True, WHITE)
    screen.blit(menu_back, [74,65])

#Button for Unit 1 Test.
def unit1_chaptertest():
    pygame.draw.rect(screen, WHITE, [60, 60, 177, 50], 4)
    font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
    menu_back = font_menu_back.render("UNIT 1 TEST", True, WHITE)
    screen.blit(menu_back, [74,65])

#Button for Unit 2 Test.
def unit2_chaptertest():
    pygame.draw.rect(screen, WHITE, [60, 60, 177, 50], 4)
    font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
    menu_back = font_menu_back.render("UNIT 2 TEST", True, WHITE)
    screen.blit(menu_back, [74,65])

#Button for Unit 3 Test.
def unit3_chaptertest():
    pygame.draw.rect(screen, WHITE, [60, 60, 177, 50], 4)
    font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
    menu_back = font_menu_back.render("UNIT 3 TEST", True, WHITE)
    screen.blit(menu_back, [74,65])

#Text - tells the user to hold down the box to see the result (correct/incorrect).
def test_format():
    font_unit1 = pygame.font.SysFont('CenturyGothic', 30, True, False)
    unit1 = font_unit1.render("Please hold your answer to see if it is correct or incorrect.", True, BLUE)
    screen.blit(unit1, [100, 120])

#Draws two boxes after each Unit is chosen. User gets to choose Chapter in Unit.
def chapter_boxes():
    y_change = 0
    for i in range(2):
        y_change = y_change + 150
        pygame.draw.rect(screen, TURQUOISE, [300, 150 + y_change, 400, 125], 4)
        font_chapter_box = pygame.font.SysFont('CenturyGothic', 76, True, False)
        chapter_box = font_chapter_box.render("CHAPTER " + str(i + 1), True, WHITE)
        screen.blit(chapter_box, [305, 160 + y_change])
        font_chapters = pygame.font.SysFont('CenturyGothic', 135, True, False)
        chapters = font_chapters.render("...CHAPTERS...", True, TURQUOISE)
        screen.blit(chapters, [60, 85])

#Draws 4 boxes, with a letter each for multiple choice questions on the Unit tests.
def mcq_boxes():
    options = ["A", "B", "C", "D"]
    y_change_mcq = 0
    for i in range (len(options)):
        y_change_mcq = y_change_mcq + 125
        #Each rectangle corresponds to an answer or lette - A, B, C, D.
        pygame.draw.rect(screen, TURQUOISE, [100, 50 + y_change_mcq, 300, 100], 4)
        font_option_mcq = pygame.font.SysFont('CenturyGothic', 90, True, False)
        option_box = font_option_mcq.render(options[i], True, WHITE)
        screen.blit(option_box, [225, 40 + y_change_mcq])

#Rectangle 1: 100, 175, 300, 100 - A
#Rectangle 2: 100, 300, 300, 100 - B
#Rectangle 3: 100, 425, 300, 100 - C
#Rectangle 4: 100, 550, 300, 100 - D


#For Unit 1 Test, questions and screen numbers are correlated through a list.
#Each question is printed out 1 by one. This function is called at the screens it has itself.
def unit1_ques_ans():
    font = pygame.font.SysFont('CenturyGothic', 15, True, False)

    if screen_number == 15:
        #Answer - A
        q1_u1 = font.render(unit1_questions[0], True, WHITE)
        screen.blit(q1_u1, [100, 660])
        test_format()

    if screen_number == 16:
        #Answer - C
        font2 = pygame.font.SysFont('CenturyGothic', 10, True, False)
        q2_u1 = font2.render(unit1_questions[1], True, WHITE)
        screen.blit(q2_u1, [65, 660])
        test_format()

    if screen_number == 17:
        #Answer - A
        q3_u1 = font.render(unit1_questions[2], True, WHITE)
        screen.blit(q3_u1, [100, 660])
        test_format()

    if screen_number == 18:
        #Answer - B
        q4_u1 = font.render(unit1_questions[3], True, WHITE)
        screen.blit(q4_u1, [100, 660])
        test_format()

    if screen_number == 19:
        #Answer - B
        q5_u1 = font.render(unit1_questions[4], True, WHITE)
        screen.blit(q5_u1, [100, 660])
        test_format()

    if screen_number == 20:
        #Answer - A
        q6_u1 = font.render(unit1_questions[5], True, WHITE)
        screen.blit(q6_u1, [100, 660])
        test_format()

    if screen_number == 21:
        #Answer D
        font2 = pygame.font.SysFont('CenturyGothic', 12, True, False)
        q7_u1 = font2.render(unit1_questions[6], True, WHITE)
        screen.blit(q7_u1, [100, 660])
        test_format()


#For Unit 2 Test, questions and screen numbers are correlated through a list.
#Each question is printed out 1 by one. This function is called at the screens it has itself.
def unit2_ques_ans():
    font = pygame.font.SysFont('CenturyGothic', 12, True, False)

    if screen_number == 24:
        #Answer - D
        q1_u2 = font.render(unit2_questions[0], True, WHITE)
        screen.blit(q1_u2, [100, 660])
        test_format()

    if screen_number == 25:
        # Answer - C
        q2_u2 = font.render(unit2_questions[1], True, WHITE)
        screen.blit(q2_u2, [100, 660])
        test_format()

    if screen_number == 26:
        # Answer - A
        q3_u2 = font.render(unit2_questions[2], True, WHITE)
        screen.blit(q3_u2, [100, 660])
        test_format()

    if screen_number == 27:
        # Answer - B
        q4_u2 = font.render(unit2_questions[3], True, WHITE)
        screen.blit(q4_u2, [100, 660])
        test_format()

    if screen_number == 28:
        # Answer - D
        q5_u2 = font.render(unit2_questions[4], True, WHITE)
        screen.blit(q5_u2, [100, 660])
        test_format()

    if screen_number == 29:
        # Answer - D
        q6_u2 = font.render(unit2_questions[5], True, WHITE)
        screen.blit(q6_u2, [100, 660])
        test_format()

    if screen_number == 30:
        # Answer - C
        q7_u2 = font.render(unit2_questions[6], True, WHITE)
        screen.blit(q7_u2, [100, 660])
        test_format()


#For Unit 3 Test, questions and screen numbers are correlated through a list.
#Each question is printed out 1 by one. This function is called at the screens it has itself.
def unit3_ques_ans():
    font = pygame.font.SysFont('CenturyGothic', 14, True, False)

    if screen_number == 38:
        #Answer - C
        q1_u3 = font.render(unit3_questions[0], True, WHITE)
        screen.blit(q1_u3, [100, 660])
        test_format()

    if screen_number == 39:
        # Answer - A
        q2_u3 = font.render(unit3_questions[1], True, WHITE)
        screen.blit(q2_u3, [100, 660])
        test_format()

    if screen_number == 40:
        # Answer - B
        q3_u3 = font.render(unit3_questions[2], True, WHITE)
        screen.blit(q3_u3, [100, 660])
        test_format()

    if screen_number == 41:
        # Answer - D
        q4_u3 = font.render(unit3_questions[3], True, WHITE)
        screen.blit(q4_u3, [100, 660])
        test_format()

    if screen_number == 42:
        # Answer - C
        q5_u3 = font.render(unit3_questions[4], True, WHITE)
        screen.blit(q5_u3, [100, 660])
        test_format()

    if screen_number == 43:
        # Answer - B
        q6_u3 = font.render(unit3_questions[5], True, WHITE)
        screen.blit(q6_u3, [100, 660])
        test_format()

    if screen_number == 44:
        # Answer - A
        q7_u3 = font.render(unit3_questions[6], True, WHITE)
        screen.blit(q7_u3, [100, 660])
        test_format()

#This defines the appearance of Screen 0. Welcomes User.
def screen_0():
    screen.fill(BLACK)
    red_border()

    # Welcomes the user before getting to menu system.
    font_welcome = pygame.font.SysFont('CenturyGothic', 135, True, False)
    welcome = font_welcome.render("Reaction?", True, ORANGE)
    screen.blit(welcome, [175, 85])
    font_intro = pygame.font.SysFont('CenturyGothic', 85, True, False)
    intro = font_intro.render("Let's React!", True, YELLOW)
    screen.blit(intro, [265, 320])
    font_begin = pygame.font.SysFont('CenturyGothic', 40, True, False)
    begin = font_begin.render("Click Anywhere Inside The Box To Start.", True, RED)
    screen.blit(begin, [130, 550])


#This defines the appearance of Screen 1. Welcomes User to the Menu.
def screen_1():
    screen.fill(BLACK)
    red_border()

    font_menu = pygame.font.SysFont('CenturyGothic', 120, True, False)
    menu = font_menu.render("...MAIN MENU...", True, ORANGE)
    screen.blit(menu, [60, 85])

    # Draws and writes Unit # in the menu.
    pygame.draw.rect(screen, RED, [300, 250, 400, 125], 4)
    font_unit1 = pygame.font.SysFont('CenturyGothic', 100, True, False)
    unit1 = font_unit1.render("UNIT 1", True, RED)
    screen.blit(unit1, [360, 250])

    # Draws and writes Unit # in the menu.
    pygame.draw.rect(screen, ORANGE, [300, 400, 400, 125], 4)
    font_unit2 = pygame.font.SysFont('CenturyGothic', 100, True, False)
    unit2 = font_unit2.render("UNIT 2", True, ORANGE)
    screen.blit(unit2, [360, 400])

    # Draws and writes Unit # in the menu.
    pygame.draw.rect(screen, YELLOW, [300, 550, 400, 125], 4)
    font_unit3 = pygame.font.SysFont('CenturyGothic', 100, True, False)
    unit3 = font_unit3.render("UNIT 3", True, YELLOW)
    screen.blit(unit3, [360, 550])

#Screen that lets you choose between chapters in Unit 1.
def screen_2():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    chapter_boxes()

#Screen that lets you choose between chapters in Unit 2.
def screen_3():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    chapter_boxes()

#Screen that lets you choose between chapters in Unit 3.
def screen_4():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    chapter_boxes()

#Screen with first lesson in Chapter 1 Unit 1.
def screen_5():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    #1st pic
    screen.blit(isotopes, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 783, 495], 6)
    #To screen 11 (2nd pic), and to screen 12 (3rd pic).
    next()

#Screen with first lesson in Chapter 2 Unit 1.
def screen_6():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    #1st pic
    screen.blit(periodic_trends, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 785, 495], 6)
    #To screen 13 (2nd pic), and to screen 14 (3rd pic).
    next()

#Screen with first lesson in Chapter 1 Unit 2.
def screen_7():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    #1st pic
    screen.blit(synthesis, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 783, 488], 6)
    #To screen 22 (2nd pic). This is the last pic in this chapter.
    next()

#Screen with first lesson in Chapter 2 Unit 2.
def screen_8():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    #1st pic
    screen.blit(single_d, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 785, 492], 6)
    #To screen 23 (2nd pic). This is the last pic in this chapter.
    next()

#Screen with first lesson in Chapter 1 Unit 3.
def screen_9():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    #1st pic
    screen.blit(acid_properties, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 785, 490], 6)
    #To screen 31 (2nd pic), screen 32 (3rd pic), screen 33(4th pic), screen 34 (5th pic).
    next()

#Screen with first lesson in Chapter 2 Unit 3.
def screen_10():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    #1st pic
    screen.blit(pH, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 785, 490], 6)
    #To screen 35 (2nd pic), screen 36 (3rd pic), screen 37(4th pic).
    next()

#Second picture in Chapter 1 Unit 1.
def screen_11():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    screen.blit(isotope_example1, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 781, 490], 6)
    next()

#Third picture in Chapter 1 Unit 1.
def screen_12():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    screen.blit(isotope_example2, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 781, 492], 6)
    #Clicking next will take you to Chapter 2 lessons (Chapter 1 Unit 1 finishes).
    next()

#Second picture in Chapter 2 Unit 1.
def screen_13():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    screen.blit(ar_ie, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 779, 490], 6)
    next()

#Second picture in Chapter 2 Unit 1.
def screen_14():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    screen.blit(ea_en, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 781, 490], 6)
    #DIDNT ADD A NEXT SINCE THIS LEADS TO CHAPTER TEST
    unit1_chaptertest()

#Screen appearance.
def screen_15():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_16():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_17():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_18():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_19():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_20():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_21():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

def screen_22():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    screen.blit(decomposition, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 785, 490], 6)
    # Clicking next will take you to Chapter 2 lessons (Chapter 1 Unit 2 finishes).
    next()

def screen_23():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    screen.blit(double_d, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 781, 492], 6)
    #DIDNT ADD A NEXT SINCE THIS LEADS TO CHAPTER TEST
    unit2_chaptertest()

#Screen appearance.
def screen_24():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_25():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_26():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_27():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_28():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_29():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_30():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Lesson from Unit 3 - Chapter 1.
def screen_31():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    screen.blit(acid_definitions, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 785, 490], 6)
    next()

#Lesson from Unit 3 - Chapter 1.
def screen_32():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    screen.blit(acid_hydrogen, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 785, 492], 6)
    next()

#Lesson from Unit 3 - Chapter 1.
def screen_33():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    screen.blit(base_properties, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 785, 492], 6)
    next()

#Lesson from Unit 3 - Chapter 1.
def screen_34():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    screen.blit(base_definitions, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 785, 492], 6)
    # Clicking next will take you to Chapter 2 lessons (Chapter 1 Unit 2 finishes).
    next()

#Lesson from Unit 3 - Chapter 2.
def screen_35():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    screen.blit(pOH, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 782, 488], 6)
    next()

#Lesson from Unit 3 - Chapter 2.
def screen_36():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    screen.blit(pH_scale, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 785, 492], 6)
    next()

#Lesson from Unit 3 - Chapter 2.
def screen_37():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    screen.blit(titration_definitions, [110, 160])
    pygame.draw.rect(screen, TURQUOISE, [110, 160, 781, 488], 6)
    #DIDNT ADD A NEXT SINCE THIS LEADS TO CHAPTER TEST
    unit3_chaptertest()

#Screen appearance.
def screen_38():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_39():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_40():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_41():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_42():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#Screen appearance.
def screen_43():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()
    next()

#This is the last screen. From here user can go to menu again.
def screen_44():
    screen.fill(BLACK)
    blue_border()
    menu_button()
    mcq_boxes()

# -------- Main Program Loop -----------
while not done:
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    mouse_pressed = pygame.mouse.get_pressed()[0]
    if (mouseX > 840) and (mouseX < 840 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
        screen_number = 1
    if screen_number == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_0()

        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 50) and (mouseX < 50 + 900) and (mouseY > 50) and (mouseY < 50 + 650) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 1


    if screen_number == 1:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_1()

        #Checks if Unit 1 is clicked.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 300) and (mouseX < 300 + 400) and (mouseY > 250) and (mouseY < 250 + 125) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 2

        #Checks if Unit 2 is clicked.
        if (mouseX > 300) and (mouseX < 300 + 400) and (mouseY > 400) and (mouseY < 400 + 125) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 3

        #Checks if Unit 3 is clicked.
        if (mouseX > 300) and (mouseX < 300 + 400) and (mouseY > 550) and (mouseY < 550 + 125)and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 4


    #Unit 1 material starts from Screen 2.
    if screen_number == 2:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_2()

        #If Chapter 1 in Unit 1 is clicked, screen changes to 5.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 300) and (mouseX < 300 + 400) and (mouseY > 300) and (mouseY < 300 + 125) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 5

        #If Chapter 2 in Unit 1 is clicked, screen changes to 6.
        if (mouseX > 300) and (mouseX < 300 + 400) and (mouseY > 450) and (mouseY < 450 + 125) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 6


    #Unit 2 material starts from Screen 3.
    if screen_number == 3:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_3()

        #If Chapter 1 in Unit 2 is clicked, screen changes to 7.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 300) and (mouseX < 300 + 400) and (mouseY > 300) and (mouseY < 300 + 125) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 7

        #If Chapter 2 in Unit 2 is clicked, screen changes to 8.
        if (mouseX > 300) and (mouseX < 300 + 400) and (mouseY > 450) and (mouseY < 450 + 125) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 8


    #Unit 3 material starts from Screen 4.
    if screen_number == 4:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_4()

        #If Chapter 1 in Unit 3 is clicked, screen changes to 9.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 300) and (mouseX < 300 + 400) and (mouseY > 300) and (mouseY < 300 + 125) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 9

        #If Chapter 2 in Unit 3 is clicked, screen changes to 10.
        if (mouseX > 300) and (mouseX < 300 + 400) and (mouseY > 450) and (mouseY < 450 + 125) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 10


    #Chapter 1 in Unit 1 - Isotopes - goes to screen 11 for next pic.
    if screen_number == 5:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_5()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 11


    if screen_number == 6:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_6()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 13


    if screen_number == 7:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_7()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 22


    if screen_number == 8:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_8()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 23


    if screen_number == 9:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_9()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 31


    if screen_number == 10:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_10()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 35


    #Chapter 1 in Unit 1 - Isotopes Example 1 - goes to screen 12 for next pic.
    if screen_number == 11:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_11()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 12


    # Chapter 1 in Unit 1 - Isotopes Example 2(last pic in Chapter, so user can go back to Menu, or Chapter Test).
    if screen_number == 12:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_12()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 6


    if screen_number == 13:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_13()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 14


    if screen_number == 14:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_14()

        #Checks if user clicks Unit 1 Test.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 177) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 15


    # From Screen 15 - 21, it is the Unit 1 Test.
    if screen_number == 15:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_15()
        unit1_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 16

        # From Screen 38 - 44, it is the Unit 3 Test.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 175) and (mouseY < 175 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: A", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 16:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_16()
        unit1_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 17

        # From Screen 38 - 44, it is the Unit 3 Test.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 425) and (mouseY < 425 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: C", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 17:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_17()
        unit1_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 18

        # From Screen 38 - 44, it is the Unit 3 Test.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 175) and (mouseY < 175 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: A", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 18:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_18()
        unit1_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 19

        # From Screen 38 - 44, it is the Unit 3 Test.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 300) and (mouseY < 300 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: B", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 19:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_19()
        unit1_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 20

        # From Screen 38 - 44, it is the Unit 3 Test.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 300) and (mouseY < 300 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: B", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 20:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_20()
        unit1_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 21

        # From Screen 38 - 44, it is the Unit 3 Test.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 175) and (mouseY < 175 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: A", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 21:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_21()
        unit1_ques_ans()

        # Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 7

        # From Screen 38 - 44, it is the Unit 3 Test.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 550) and (mouseY < 550 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: D", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 22:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_22()

        # Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 8


    if screen_number == 23:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_23()

        #Checks if user clicks Unit 2 Test.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 177) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 24


    # From Screen 24 - 30, it is the Unit 2 Test.
    if screen_number == 24:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_24()
        unit2_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 25

        # Checks if the user clicked the right or wrong answer.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 550) and (mouseY < 550 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: D", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 25:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_25()
        unit2_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 26

        # Checks if the user clicked the right or wrong answer.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 425) and (mouseY < 425 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: C", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 26:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_26()
        unit2_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 27

        # Checks if the user clicked the right or wrong answer.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 175) and (mouseY < 175 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: A", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 27:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_27()
        unit2_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 28

        # Checks if the user clicked the right or wrong answer.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 300) and (mouseY < 300 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: B", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 28:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_28()
        unit2_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 29

        # Checks if the user clicked the right or wrong answer.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 550) and (mouseY < 550 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: D", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 29:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_29()
        unit2_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 30

        # Checks if the user clicked the right or wrong answer.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 550) and (mouseY < 550 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: D", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 30:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_30()
        unit2_ques_ans()

        # Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 9

        # Checks if the user clicked the right or wrong answer.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 425) and (mouseY < 425 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: C", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 31:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_31()

        # Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 32


    if screen_number == 32:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_32()

        # Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 33


    if screen_number == 33:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_33()

        # Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 34


    if screen_number == 34:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_34()

        # Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 10


    if screen_number == 35:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_35()

        # Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 36


    if screen_number == 36:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_36()

        # Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 37


    if screen_number == 37:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_37()

        #Checks if user clicks Unit 2 Test.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 177) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 38


    #From Screen 38 - 44, it is the Unit 3 Test.
    if screen_number == 38:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_38()
        unit3_ques_ans()

        # Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 39

        # Checks if the user clicked the right or wrong answer.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 425) and (mouseY < 425 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: C", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 39:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_39()
        unit3_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 40

        # Checks if the user clicked the right or wrong answer.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 175) and (mouseY < 175 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: A", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 40:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_40()
        unit3_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 41

        # Checks if the user clicked the right or wrong answer.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 300) and (mouseY < 300 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: B", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 41:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_41()
        unit3_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 42

        # Checks if the user clicked the right or wrong answer.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 550) and (mouseY < 550 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: D", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 42:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_42()
        unit3_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 43

        # Checks if the user clicked the right or wrong answer.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 425) and (mouseY < 425 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: C", True, WHITE)
            screen.blit(menu_back, [768, 645])


    if screen_number == 43:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_43()
        unit3_ques_ans()

        #Checks if user clicks next.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if (mouseX > 60) and (mouseX < 60 + 100) and (mouseY > 60) and (mouseY < 60 + 50) and mouse_pressed == 1:
            pygame.time.delay(300)
            screen_number = 44

        # Checks if the user clicked the right or wrong answer.
        elif(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 300) and (mouseY < 300 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: B", True, WHITE)
            screen.blit(menu_back, [768, 645])


    #This is the last screen.
    if screen_number == 44:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen_44()
        unit3_ques_ans()

        #Checks if the user clicked the right or wrong answer. Then the only place to navigate to is the Menu.
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if(mouseX > 100) and (mouseX < 100 + 300) and (mouseY > 175) and (mouseY < 175 + 100) and mouse_pressed == 1:
            correct_box()

        elif mouse_pressed  == 1:
            pygame.time.delay(300)
            answer_box()
            font_menu_back = pygame.font.SysFont('CenturyGothic', 30, True, False)
            menu_back = font_menu_back.render("ANSWER: A", True, WHITE)
            screen.blit(menu_back, [768, 645])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()