import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
white = (255, 255, 255)
red = (200, 0, 0)
black = (0, 0, 0)
font = pygame.font.Font("freesansbold.ttf", 20)
materials = ["Soil", "Bark", "Foliage", "Stone"]
material = 0
conditions = ["Default", "Hot", "Wet", "Scorched"]
condition = 0


# https://stackoverflow.com/a/11508164
# Ported from JavaScript notation
def getRGB(pixel):
    r = (pixel >> 16) & 255
    g = (pixel >> 8) & 255
    b = pixel & 255
    return [r, g, b]


def button(text, x_pos, y_pos, x, y, colour, colour_hover):
    global material
    global condition
    pygame.draw.rect(screen, colour, (x_pos, y_pos, x, y))
    if (x_pos < mouse[0] < (x + x_pos)) and (y_pos < mouse[1] < (y + y_pos)):
        pygame.draw.rect(screen, colour_hover, (x_pos, y_pos, x, y))
        if click[0] == 1:
            if text == "Material":
                if (material + 1) >= len(materials):
                    material = 0
                else:
                    material = material + 1
            if text == "Condition":
                if (condition + 1) >= len(conditions):
                    condition = 0
                else:
                    condition = condition + 1
    buttonText = font.render(text, True, white)
    textRect = buttonText.get_rect()
    textRect.center = (x_pos + (x / 2), (y_pos + (y / 2)))
    screen.blit(buttonText, textRect)


def tile_soil(x_pos, y_pos, x, y):
    tile = pygame.image.load("Soil.jpg")
    tile = pygame.transform.scale(tile, (x, y))
    if conditions[condition] == "Default":
        screen.blit(tile, (x_pos, y_pos))
    elif conditions[condition] == "Wet":
        px_array = pygame.PixelArray(tile)
        counter1 = 0
        counter2 = 0
        while counter1 < x or counter2 < y - 1:
            while counter1 < x:
                pixel = px_array[counter1, counter2]
                pixel = getRGB(pixel)
                pixel[0] = 255
                pixel = tuple(pixel)
                px_array[counter1, counter2] = pixel
                counter1 = counter1 + 1
            if counter2 < y - 1:
                counter1 = 0
                counter2 = counter2 + 1
        del px_array
        screen.blit(tile, (x_pos, y_pos))
    elif conditions[condition] == "Hot":
        px_array = pygame.PixelArray(tile)
        counter1 = 0
        counter2 = 0
        while counter1 < x or counter2 < y - 1:
            while counter1 < x:
                pixel = px_array[counter1, counter2]
                pixel = getRGB(pixel)
                pixel[2] = 255
                pixel = tuple(pixel)
                px_array[counter1, counter2] = pixel
                counter1 = counter1 + 1
            if counter2 < y - 1:
                counter1 = 0
                counter2 = counter2 + 1
        del px_array
        screen.blit(tile, (x_pos, y_pos))
    elif conditions[condition] == "Scorched":
        px_array = pygame.PixelArray(tile)
        counter1 = 0
        counter2 = 0
        while counter1 < x or counter2 < y - 1:
            while counter1 < x:
                pixel = px_array[counter1, counter2]
                pixel = getRGB(pixel)
                average = (pixel[0] + pixel[1] + pixel[2]) / 3
                pixel[0] = average
                pixel[1] = average
                pixel[2] = average
                pixel = tuple(pixel)
                px_array[counter1, counter2] = pixel
                counter1 = counter1 + 1
            if counter2 < y - 1:
                counter1 = 0
                counter2 = counter2 + 1
        del px_array
        screen.blit(tile, (x_pos, y_pos))


def tile_stone(x_pos, y_pos, x, y):
    tile = pygame.image.load("Stone.jpg")
    tile = pygame.transform.scale(tile, (x, y))
    if conditions[condition] == "Default":
        screen.blit(tile, (x_pos, y_pos))
    elif conditions[condition] == "Wet":
        px_array = pygame.PixelArray(tile)
        counter1 = 0
        counter2 = 0
        while counter1 < x or counter2 < y - 1:
            while counter1 < x:
                pixel = px_array[counter1, counter2]
                pixel = getRGB(pixel)
                pixel[0] = 255
                pixel = tuple(pixel)
                px_array[counter1, counter2] = pixel
                counter1 = counter1 + 1
            if counter2 < y - 1:
                counter1 = 0
                counter2 = counter2 + 1
        del px_array
        screen.blit(tile, (x_pos, y_pos))
    elif conditions[condition] == "Hot":
        px_array = pygame.PixelArray(tile)
        counter1 = 0
        counter2 = 0
        while counter1 < x or counter2 < y - 1:
            while counter1 < x:
                pixel = px_array[counter1, counter2]
                pixel = getRGB(pixel)
                pixel[2] = 255
                pixel = tuple(pixel)
                px_array[counter1, counter2] = pixel
                counter1 = counter1 + 1
            if counter2 < y - 1:
                counter1 = 0
                counter2 = counter2 + 1
        del px_array
        screen.blit(tile, (x_pos, y_pos))
    elif conditions[condition] == "Scorched":
        px_array = pygame.PixelArray(tile)
        counter1 = 0
        counter2 = 0
        while counter1 < x or counter2 < y - 1:
            while counter1 < x:
                pixel = px_array[counter1, counter2]
                pixel = getRGB(pixel)
                average = (pixel[0] + pixel[1] + pixel[2]) / 3
                pixel[0] = average
                pixel[1] = average
                pixel[2] = average
                pixel = tuple(pixel)
                px_array[counter1, counter2] = pixel
                counter1 = counter1 + 1
            if counter2 < y - 1:
                counter1 = 0
                counter2 = counter2 + 1
        del px_array
        screen.blit(tile, (x_pos, y_pos))


def tile_bark(x_pos, y_pos, x, y):
    tile = pygame.image.load("Bark.jpg")
    tile = pygame.transform.scale(tile, (x, y))
    if conditions[condition] == "Default":
        screen.blit(tile, (x_pos, y_pos))
    elif conditions[condition] == "Wet":
        px_array = pygame.PixelArray(tile)
        counter1 = 0
        counter2 = 0
        while counter1 < x or counter2 < y - 1:
            while counter1 < x:
                pixel = px_array[counter1, counter2]
                pixel = getRGB(pixel)
                pixel[0] = 255
                pixel = tuple(pixel)
                px_array[counter1, counter2] = pixel
                counter1 = counter1 + 1
            if counter2 < y - 1:
                counter1 = 0
                counter2 = counter2 + 1
        del px_array
        screen.blit(tile, (x_pos, y_pos))
    elif conditions[condition] == "Hot":
        px_array = pygame.PixelArray(tile)
        counter1 = 0
        counter2 = 0
        while counter1 < x or counter2 < y - 1:
            while counter1 < x:
                pixel = px_array[counter1, counter2]
                pixel = getRGB(pixel)
                pixel[2] = 255
                pixel = tuple(pixel)
                px_array[counter1, counter2] = pixel
                counter1 = counter1 + 1
            if counter2 < y - 1:
                counter1 = 0
                counter2 = counter2 + 1
        del px_array
        screen.blit(tile, (x_pos, y_pos))
    elif conditions[condition] == "Scorched":
        px_array = pygame.PixelArray(tile)
        counter1 = 0
        counter2 = 0
        while counter1 < x or counter2 < y - 1:
            while counter1 < x:
                pixel = px_array[counter1, counter2]
                pixel = getRGB(pixel)
                average = (pixel[0] + pixel[1] + pixel[2]) / 3
                pixel[0] = average
                pixel[1] = average
                pixel[2] = average
                pixel = tuple(pixel)
                px_array[counter1, counter2] = pixel
                counter1 = counter1 + 1
            if counter2 < y - 1:
                counter1 = 0
                counter2 = counter2 + 1
        del px_array
        screen.blit(tile, (x_pos, y_pos))


def tile_foliage(x_pos, y_pos, x, y):
    tile = pygame.image.load("Foliage.jpg")
    tile = pygame.transform.scale(tile, (x, y))
    if conditions[condition] == "Default":
        screen.blit(tile, (x_pos, y_pos))
    elif conditions[condition] == "Wet":
        px_array = pygame.PixelArray(tile)
        counter1 = 0
        counter2 = 0
        while counter1 < x or counter2 < y - 1:
            while counter1 < x:
                pixel = px_array[counter1, counter2]
                pixel = getRGB(pixel)
                pixel[0] = 255
                pixel = tuple(pixel)
                px_array[counter1, counter2] = pixel
                counter1 = counter1 + 1
            if counter2 < y - 1:
                counter1 = 0
                counter2 = counter2 + 1
        del px_array
        screen.blit(tile, (x_pos, y_pos))
    elif conditions[condition] == "Hot":
        px_array = pygame.PixelArray(tile)
        counter1 = 0
        counter2 = 0
        while counter1 < x or counter2 < y - 1:
            while counter1 < x:
                pixel = px_array[counter1, counter2]
                pixel = getRGB(pixel)
                pixel[2] = 255
                pixel = tuple(pixel)
                px_array[counter1, counter2] = pixel
                counter1 = counter1 + 1
            if counter2 < y - 1:
                counter1 = 0
                counter2 = counter2 + 1
        del px_array
        screen.blit(tile, (x_pos, y_pos))
    elif conditions[condition] == "Scorched":
        px_array = pygame.PixelArray(tile)
        counter1 = 0
        counter2 = 0
        while counter1 < x or counter2 < y - 1:
            while counter1 < x:
                pixel = px_array[counter1, counter2]
                pixel = getRGB(pixel)
                average = (pixel[0] + pixel[1] + pixel[2]) / 3
                pixel[0] = average
                pixel[1] = average
                pixel[2] = average
                pixel = tuple(pixel)
                px_array[counter1, counter2] = pixel
                counter1 = counter1 + 1
            if counter2 < y - 1:
                counter1 = 0
                counter2 = counter2 + 1
        del px_array
        screen.blit(tile, (x_pos, y_pos))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.fill(white)
        button("Material", 200, 200, 200, 60, black, red)
        mText = font.render(materials[material], True, black)
        mRect = mText.get_rect()
        mRect.center = (300, 310)
        screen.blit(mText, mRect)
        button("Condition", 200, 360, 200, 60, black, red)
        cText = font.render(conditions[condition], True, black)
        cRect = cText.get_rect()
        cRect.center = (300, 480)
        screen.blit(cText, cRect)
        if materials[material] == "Soil":
            tile_soil(500, 300, 200, 200)
        elif materials[material] == "Stone":
            tile_stone(500, 300, 200, 200)
        elif materials[material] == "Bark":
            tile_bark(500, 300, 200, 200)
        elif materials[material] == "Foliage":
            tile_foliage(500, 300, 200, 200)
        pygame.display.flip()
