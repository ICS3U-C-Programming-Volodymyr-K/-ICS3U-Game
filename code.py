#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 05, 25, 2025
# This program is a game.



import ugame
import constants
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

    #RST 6 - sets button values from constant for future reference
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    pew_sound = open("pew.wav", 'rb')
    #Prepares the sound RST 6, WATCH THE VIDEO AND PLAY WITH BUTTONS FOR PARTIAL
    sound = ugame.audio
    sound.stop()
    sound.mute(True)
    # Sizes the image and participates in display of image due to grid
    background = stage.Grid(image_bank_background, 10, 8)
    # Sets the background and displays it on frame rate of 60

    #RST 5, basically performs calculation for Y coordinate while leaving the sprite and X alone. 
    ship = stage.Sprite(image_bank_sprites, 5, 75,
                        constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    

    #5 is an image taken from our file while 75 and 66 are the x and y coordinates to set the sprite
    game = stage.Stage(ugame.display, 60)
    # Arrays create a nice flow for image to display
    game.layers = [background]
    # Render block
    game.render_block()
    # Place holder for now
    while True:
        pass #remove for the use 

        # Keys MAY NOT WORK AND CAUSE ERROR 06-04-2025
        keys = ugame.button.get_pressed()
        #Sets specific parameter to be execute by a button pressed by the user or key
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT: #RST 05 boundaries were added as in K_LEFT
            if ship.x <= constants.SCREEN_X:
                ship.move(ship.x + 1, ship.y - 1)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_LEFT: #RST 05 changes applied in terms of boundary
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP: #RST 05 EXPERIMENTAL MOVEMENT IN TERMS OF BOUNDARIES AND SIGNS FOR SHIP.Y +/- 1 CHANGED
            if ship.y <= constants.SCREEN_Y:
                ship.move(ship.x, ship.y + 1)
            else: 
                ship.move(ship.x, 0)
        if keys & ugame.K_DOWN:  # RST 05 EXPERIMENTAL MOVEMENT IN TERMS OF BOUNDARIES AND SIGNS FOR SHIP.Y +/- 1 CHANGED
             if ship.y <= constants.SCREEN_Y:
                ship.move(ship.x, ship.y - 1)
             else: 
                ship.move(ship.x, 0)


if __name__ == "__main__":
    game_scene()
