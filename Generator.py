# Written by Edward Peters

# Imports
import pygame

# Initialising Pygame and creating a surface
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))

# Colours
white = (255, 255, 255)
red = (200, 0, 0)
black = (0, 0, 0)

# General-purpose font
font = pygame.font.Font("freesansbold.ttf", 20)

# Arrays representing available materials and states, as well as integers to define which are currently selected
materials = ["Soil", "Bark", "Foliage", "Stone"]
material = 0
conditions = ["Default", "Hot", "Wet", "Scorched"]
condition = 0


# https://stackoverflow.com/a/11508164
# Ported from JavaScript notation
# Function to get the RGB values of a pixel and return them in an array
def getRGB(pixel):
    r = (pixel >> 16) & 255
    g = (pixel >> 8) & 255
    b = pixel & 255
    return [r, g, b]


# General function for displaying interactive buttons
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
    rectangleText = buttonText.get_rect()
    rectangleText.center = (x_pos + (x / 2), (y_pos + (y / 2)))
    screen.blit(buttonText, rectangleText)


# Function for displaying all variations of the 'Soil' tile
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


# Function for displaying all variations of the 'Stone' tile
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


# Function for displaying all variations of the 'Bark' tile
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


# Function for displaying all variations of the 'Foliage' tile
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


# Loop that keeps the surface running and constantly updating
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Variables to keep track of the state and position of the mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # What's to be displayed on the surface
        screen.fill(white)
        button("Material", 200, 200, 200, 60, black, red)
        materialText = font.render(materials[material], True, black)
        materialRectangle = materialText.get_rect()
        materialRectangle.center = (300, 310)
        screen.blit(materialText, materialRectangle)
        button("Condition", 200, 360, 200, 60, black, red)
        conditionText = font.render(conditions[condition], True, black)
        conditionRectangle = conditionText.get_rect()
        conditionRectangle.center = (300, 480)
        screen.blit(conditionText, conditionRectangle)
        if materials[material] == "Soil":
            tile_soil(500, 300, 200, 200)
        elif materials[material] == "Stone":
            tile_stone(500, 300, 200, 200)
        elif materials[material] == "Bark":
            tile_bark(500, 300, 200, 200)
        elif materials[material] == "Foliage":
            tile_foliage(500, 300, 200, 200)
        pygame.display.flip()
