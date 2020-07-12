import random
import pygame
import time

# globals
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
DICE_NUMBER = 2
FIRST_DICE = 1
SECOND_DICE = 1

# Defines colours (not built in)
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
purple = 197, 66, 244
bright_red = 255, 96, 96
bright_green = 96, 255, 96

target_score = 32

pygame.display.set_caption("Final Battle With Thanos!!!")
gameDisplay = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
clock = pygame.time.Clock()
already_rolled = False

# Import Images for Dice 1-6
dice_one = pygame.image.load("C:\\Users\\Gautam\\dice\\dice_one.png")
dice_two = pygame.image.load("C:\\Users\\Gautam\\dice\\dice_two.png")
dice_three = pygame.image.load("C:\\Users\\Gautam\\dice\\dice_three.png")
dice_four = pygame.image.load("C:\\Users\\Gautam\\dice\\dice_four.png")
dice_five = pygame.image.load("C:\\Users\\Gautam\\dice\\dice_five.png")
dice_six = pygame.image.load("C:\\Users\\Gautam\\dice\\dice_six.png")
thanos_picture = pygame.image.load("C:\\Users\\Gautam\\dice\\thanos.jpg")
thanos_picture = pygame.transform.scale(thanos_picture, (138, 212))
white_background = pygame.image.load("C:\\Users\\Gautam\\dice\\whitebackground.png")
white_background = pygame.transform.scale(white_background, (900,900))

health_full = pygame.image.load("C:\\Users\\Gautam\\dice\\health bar full.png")
health_1 = pygame.image.load("C:\\Users\\Gautam\\dice\\health bar 1.png")
health_2 = pygame.image.load("C:\\Users\\Gautam\\dice\\health bar 2.png")
health_3 = pygame.image.load("C:\\Users\\Gautam\\dice\\health bar 3.png")
health_4 = pygame.image.load("C:\\Users\\Gautam\\dice\\health bar 4.png")
health_5 = pygame.image.load("C:\\Users\\Gautam\\dice\\health bar 5.png")
health_6 = pygame.image.load("C:\\Users\\Gautam\\dice\\health bar 6.png")


health_full = pygame.transform.scale(health_full, (100,75))
health_1 = pygame.transform.scale(health_1, (100,75))
health_2 = pygame.transform.scale(health_2, (100,75))
health_3 = pygame.transform.scale(health_3, (100,75))
health_4 = pygame.transform.scale(health_4, (100,75))
health_5 = pygame.transform.scale(health_5, (100,75))
health_6 = pygame.transform.scale(health_6, (100,75))

thanos_health_full = pygame.image.load("C:\\Users\\Gautam\\dice\\thanos health full.png")
thanos_health_1 = pygame.image.load("C:\\Users\\Gautam\\dice\\thanos health 1.png")
thanos_health_2 = pygame.image.load("C:\\Users\\Gautam\\dice\\thanos health 2.png")
thanos_health_3 = pygame.image.load("C:\\Users\\Gautam\\dice\\thanos health 3.png")
thanos_health_4 = pygame.image.load("C:\\Users\\Gautam\\dice\\thanos health 4.png")
thanos_health_5 = pygame.image.load("C:\\Users\\Gautam\\dice\\thanos health 5.png")
thanos_health_6 = pygame.image.load("C:\\Users\\Gautam\\dice\\thanos health 6.png")

thanos_health_full = pygame.transform.scale(thanos_health_full, (100,75))
thanos_health_1 = pygame.transform.scale(thanos_health_1, (100,75))
thanos_health_2 = pygame.transform.scale(thanos_health_2, (100,75))
thanos_health_3 = pygame.transform.scale(thanos_health_3, (100,75))
thanos_health_4 = pygame.transform.scale(thanos_health_4, (100,75))
thanos_health_5 = pygame.transform.scale(thanos_health_5, (100,75))
thanos_health_6 = pygame.transform.scale(thanos_health_6, (100,75))


diceDict = {1: dice_one,
            2: dice_two,
            3: dice_three,
            4: dice_four,
            5: dice_five,
            6: dice_six}

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()




def roll_a_dice():
    thanos_health_bar_function()
    health_bar_function()
    dice = random.randrange(1, 6)
    return dice


def display_dice(first, second):
    display_first(first)
    display_second(second)


# determines which first dice is used
def display_first(first):
    gameDisplay.blit(diceDict[first], (SCREEN_WIDTH / 4, SCREEN_HEIGHT/5.3))


# determines which second dice is used
def display_second(second):
    gameDisplay.blit(diceDict[second], (SCREEN_WIDTH / 1.5, SCREEN_HEIGHT/5.3))




# tells the user how to roll
def produce_button_message(text):
    our_font = pygame.font.SysFont("monospace", 19)
    # render the text now
    produce_text = our_font.render(text, 1, purple)
    gameDisplay.blit(produce_text, (SCREEN_WIDTH / 3.7, SCREEN_HEIGHT / 3))


# produce the roll results (in text)
def produce_roll_message(text):
    our_font = pygame.font.SysFont("monospace", 19)
    # render the text now. 1 refers to aliasing.
    produce_text = our_font.render(text, 1, purple)
    gameDisplay.blit(produce_text, (SCREEN_WIDTH / 3.3, SCREEN_HEIGHT / 2))\

def player_1(text):
    our_font = pygame.font.SysFont("monospace", 19)
    # render the text now. 1 refers to aliasing.
    produce_text = our_font.render(text, 1, purple)
    gameDisplay.blit(produce_text, (SCREEN_WIDTH / 4.1, SCREEN_HEIGHT/8))

def cpu(text):
    our_font = pygame.font.SysFont("monospace", 19)
    produce_text = our_font.render(text, 1, purple)
    gameDisplay.blit(produce_text, (SCREEN_WIDTH / 1.5, SCREEN_HEIGHT/8))

def winner(text):
    our_font = pygame.font.SysFont("monospace", 25)
    produce_text = our_font.render(text, 1, purple)
    gameDisplay.blit(produce_text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
cpu_score = 0

pygame.mixer.music.load('C:\\Users\\Gautam\\dice\\Avengers.mp3')
end_thanos = pygame.mixer.Sound('C:\\Users\\Gautam\\dice\\End game.wav')


pygame.mixer.music.play(-1)


def thanos_health_bar_function():
    if your_score < 4:
        pygame.draw.rect(gameDisplay, white, [533, 25, 101, 76])
        gameDisplay.blit(thanos_health_full, (533, 30))
        pygame.display.update()
    elif your_score < 8:
        pygame.draw.rect(gameDisplay, white, [533, 25, 101, 76])
        gameDisplay.blit(thanos_health_1, (533, 30))
        pygame.display.update()
    elif your_score < 12:
        pygame.draw.rect(gameDisplay, white, [533, 25, 101, 76])
        gameDisplay.blit(thanos_health_2, (533, 30))
        pygame.display.update()
    elif your_score < 16:

        pygame.draw.rect(gameDisplay, white, [533, 25, 101, 76])
        gameDisplay.blit(thanos_health_3, (533, 30))
        pygame.display.update()
    elif your_score < 20:
        pygame.draw.rect(gameDisplay, white, [533, 25, 101, 76])
        gameDisplay.blit(thanos_health_4, (533, 30))
        pygame.display.update()
    elif your_score < 24:
        pygame.draw.rect(gameDisplay, white, [533, 25, 101, 76])
        gameDisplay.blit(thanos_health_5, (533, 30))
        pygame.display.update()
    elif your_score < 32:
        pygame.draw.rect(gameDisplay, white, [533, 25, 101, 76])
        gameDisplay.blit(thanos_health_6, (533, 30))
        pygame.display.update()

def two_in_a_row(text):
    our_font = pygame.font.SysFont("monospace", 18)
    produce_text = our_font.render(text, 1, purple)
    gameDisplay.blit(produce_text, (10, 500))

def health_bar_function():
    if cpu_score < 4:
        pygame.draw.rect(gameDisplay, white, [200, 25, 101, 76])
        gameDisplay.blit(health_full, (200, 30))
        pygame.display.update()
    elif cpu_score < 8:
        pygame.draw.rect(gameDisplay, white, [200, 25, 101, 76])
        gameDisplay.blit(health_1, (200, 30))
        pygame.display.update()
    elif cpu_score < 12:
        pygame.draw.rect(gameDisplay, white, [200, 25, 101, 76])
        gameDisplay.blit(health_2, (200, 30))
        pygame.display.update()
    elif cpu_score < 16:
        pygame.draw.rect(gameDisplay, white, [200, 25, 101, 76])
        gameDisplay.blit(health_3, (200, 30))
        pygame.display.update()
    elif cpu_score < 20:
        pygame.draw.rect(gameDisplay, white, [200, 25, 101, 76])
        gameDisplay.blit(health_4, (200, 30))
        pygame.display.update()
    elif cpu_score < 24:
        pygame.draw.rect(gameDisplay, white, [200, 25, 101, 76])
        gameDisplay.blit(health_5, (200, 30))
        pygame.display.update()
    elif cpu_score < 32:
        pygame.draw.rect(gameDisplay, white, [200, 25, 101, 76])
        gameDisplay.blit(health_6, (200, 30))
        pygame.display.update()


# our roll will display message with our roll converted to text form, alongside
def before_roll(who_is_next):
    gameDisplay.blit(thanos_picture, (650, 50))
    cpu("Thanos")
    player_1("Player 1")
    if (who_is_next == 0):
        produce_button_message("Please hit space to roll your dice")

    else:
        produce_button_message("Thanos is  rolling . . .")



def our_roll(your_score, cpu_score):
    # Completed roll Message. Cast int to str to output the message clearly
    text = "Your Score: " + str(your_score) + ", Thanos' Score: " + str(cpu_score) + "."
    produce_roll_message(text)
    health_bar_function()
    thanos_health_bar_function()



# We don't want our roll value output before the first roll occurs.
roll_occur = False
who_is_next = 0
your_score = 0
last_roll_thanos = 0
last_roll_player = 0


def button(msg,x,y,w,h,ic,ac,):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1:
            game_start(False, 0, 0, 0, 0, 0,FIRST_DICE, SECOND_DICE, False,)



    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)



def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT/ 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50, green, bright_green,)
        button("Quit", 550, 450, 100, 50, red, bright_red,)


        pygame.display.update()
        clock.tick(15)

start_now = 1
def game_start(already_rolled, who_is_next, last_roll_thanos,cpu_score,last_roll_player,your_score,FIRST_DICE,SECOND_DICE,roll_occur):
    while already_rolled == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                already_rolled = True
                break
            if who_is_next == 1:
                time.sleep(1.3)
                SECOND_DICE = roll_a_dice()
                if SECOND_DICE == last_roll_thanos:
                    cpu_score = cpu_score + SECOND_DICE + 3
                    two_in_a_row("Thanos rolled the same number in a row. He get 3 extra points")
                    pygame.display.update()
                    time.sleep(3)
                    pygame.draw.rect(gameDisplay, white, [76, 501, 800, 76])
                    pygame.display.update()
                else:
                    cpu_score = cpu_score + SECOND_DICE
                last_roll_thanos = SECOND_DICE
                who_is_next = 0
            if cpu_score >= target_score:
                gameDisplay.blit(white_background, (0, 0))
                winner("Thanos wins!!")
                pygame.mixer.music.stop()
                end_thanos.play()
                pygame.display.update()
                time.sleep(5)
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if (who_is_next == 0):
                        FIRST_DICE = roll_a_dice()
                        if FIRST_DICE == last_roll_player:
                            your_score = your_score + FIRST_DICE + 3
                            two_in_a_row("You rolled the same number in a row. You get 3 extra points")
                            pygame.display.update()
                            time.sleep(3)
                            pygame.draw.rect(gameDisplay, white, [76, 501, 800, 76])
                            pygame.display.update()
                        else:
                            your_score = your_score + FIRST_DICE
                        last_roll_player = FIRST_DICE
                        who_is_next = 1
                    if your_score >= target_score:
                        gameDisplay.blit(white_background, (0, 0))
                        winner("You win!!")
                        pygame.mixer.music.stop()
                        pygame.display.update()
                        time.sleep(2)
                        pygame.quit()

                roll_occur = True

            gameDisplay.fill(white)

            before_roll(who_is_next)

            display_dice(FIRST_DICE, SECOND_DICE)


            if (roll_occur):
                our_roll(your_score, cpu_score)

            pygame.display.update()

            clock.tick(30)

game_intro()


