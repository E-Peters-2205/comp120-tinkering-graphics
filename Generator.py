import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
white = (255, 255, 255)
red = (200, 0, 0)
black = (0, 0, 0)
font = pygame.font.Font("freesansbold.ttf", 20)
materials = ["Soil", "Bark", "Foliage", "Stone"]
m = 0
conditions = ["Default", "Dry", "Wet", "Scorched"]
c = 0


def button(text, x_pos, y_pos, x, y, colour, colour_hover):
    global m
    global c
    pygame.draw.rect(screen, colour, (x_pos, y_pos, x, y))
    if (x_pos < mouse[0] < (x + x_pos)) and (y_pos < mouse[1] < (y + y_pos)):
        pygame.draw.rect(screen, colour_hover, (x_pos, y_pos, x, y))
        if click[0] == 1:
            if text == "Material":
                if (m + 1) >= len(materials):
                    m = 0
                else:
                    m = m + 1
            if text == "Condition":
                if (c + 1) >= len(conditions):
                    c = 0
                else:
                    c = c + 1
    buttonText = font.render(text, True, white)
    textRect = buttonText.get_rect()
    textRect.center = (x_pos + (x / 2), (y_pos + (y / 2)))
    screen.blit(buttonText, textRect)


def tile_image(x_pos, y_pos, x, y):
    if materials[m] == "Soil":
        tile = pygame.image.load("Soil.jpg")
        tile = pygame.transform.scale(tile, (x, y))
        if conditions[c] == "Default":
            screen.blit(tile, (x_pos, y_pos))
        elif conditions[c] == "Dry":
            px_array = pygame.PixelArray(tile)
            counter1 = x_pos
            counter2 = y_pos
            while counter1 < (x + x_pos) or counter2 < (y + y_pos):
                while counter1 < (x + x_pos):
                    px_array[counter1, counter2] = px_array[counter1, counter2] / 2
                    counter1 = counter1 + 1
                if counter2 < (y + y_pos):
                    counter1 = x_pos
                    counter2 = counter2 + 1


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.fill(white)
        button("Material", 200, 200, 200, 60, black, red)
        mText = font.render(materials[m], True, black)
        mRect = mText.get_rect()
        mRect.center = (300, 310)
        screen.blit(mText, mRect)
        button("Condition", 200, 360, 200, 60, black, red)
        cText = font.render(conditions[c], True, black)
        cRect = cText.get_rect()
        cRect.center = (300, 480)
        screen.blit(cText, cRect)
        tile_image(600, 300, 200, 200)
        pygame.display.flip()