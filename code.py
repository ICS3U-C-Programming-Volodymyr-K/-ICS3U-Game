#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 05, 25, 2025
# This program is a game.



import ugame
import constants
import stage

#RST 1
def scene():
    #This function is a scene of game
    print("\n\n\n") #displays three blank lines
    print("Hello, Vlad!")
    #makes infinite loop
    while True:
        pass #placeholder for now
if __name__ == "__main__":
    scene()


#RST 7, menu scene
def menu_scene():
    
    #Takes an image from the bank RST 7
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    #adds the text on screen RST 7
    text = []
    text1 = stage.Text(width = 29, height = 12, font = None, palette = constants.RED_PALETTE, buffer=None)
    text1.move(20,10)
    text1.text("Sigma Production Presents")
    text.append(text1)
    # adds the text on screen RST 7
    text2 = stage.Text(width=29, height=12, font=None,
                       palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START!")
    text.append(text2)
    #Sets the background to image 0 RST 7
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y)
    #creates an fps ratio on which image will be displayed RST 7
    game = stage.Stage(ugame.display, constants.FPS)
    #sets the layers RST 7
    game.layers = text + [background]
# render block RST 7
    game.render_block()

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
    #RST 9/any other update abt adding aliens as a part cuz you need them for program
    alien = stage.Sprite(image_bank_sprites, 9, int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2), 16)

    #RST 9 which creates lasers and controls their amount.
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        single_laser = stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        lasers.append(single_laser)

    #5 is an image taken from our file while 75 and 66 are the x and y coordinates to set the sprite
    game = stage.Stage(ugame.display, 60)
    # Arrays create a nice flow for image to display
    game.layers = [background] + [ship] + lasers + [alien]
    # Render block
    game.render_block()
    # Place holder for now
    while True:
        pass #remove for the use 

        # Keys MAY NOT WORK AND CAUSE ERROR 06-04-2025, RST 4
        keys = ugame.button.get_pressed()
        #Sets specific parameter to be execute by a button pressed by the user or key
        if keys & ugame.K_X:
            pass
        #RST 9, update for shooting for A button , refer to RST 9 video 
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else: 
               a_button = constants.button_state["button_up"]
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

                #RST 9 video 
        if a_button == constants.button_state["button_just_pressed"]:
            #Fires a laser and plays a sound if A button is pressed RST 9
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break
        #RST 9 video each frame moves a shot laser 
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
 # redraw Sprites
        game.render_sprites(lasers + [ship] + [alien])
        # makes sure the ship is always on screen
        game.tick()
        # This makes sure the ship renders at 60 Hz per frames

if __name__ == "__main__":
    game_scene()
