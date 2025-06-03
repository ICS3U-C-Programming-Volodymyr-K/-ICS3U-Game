#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 05, 25, 2025
# This program is a game.



import ugame

import stage


def scene():
    #This function is a scene of game
    print("\n\n\n") #displays three blank lines
    print("Hello, Vlad!")
    #makes infinite loop
    while True:
        pass #placeholder for now
if __name__ == "__main__":
    scene()

def game_scene():
    # Access the image from the files with the use of bank
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    #Access to sprite from space_aliens.bmp
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Sizes the image and participates in display of image due to grid
    background = stage.Grid(image_bank_background, 10, 8)
    # Sets the background and displays it on frame rate of 60
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)
    #5 is an image taken from our file while 75 and 66 are the x and y coordinates to set the sprite
    game = stage.Stage(ugame.display, 60)
    # Arrays create a nice flow for image to display
    game.layers = [background]
    # Render block
    game.render_block()
    # Place holder for now
    while True:
        pass


if __name__ == "__main__":
    game_scene()
