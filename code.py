# Created By: Volodymyr Kryzhanovskyi
# Date: 05, 25, 2025
# This program is a game.




import ugame
import constants
import stage
import time
import random




def splash_scene():
    # RST 8 basically creates a splash scene
    # RST 8 controls the soun and access the library and plays it
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    # Gets the images from bank
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    # Grids the image and displays it
    background = stage.Grid(image_bank_mt_background,
                            constants.SCREEN_X, constants.SCREEN_Y)
    # used this program to split the image into tile:


    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png


    background.tile(2, 2, 0)  # blank white


    background.tile(3, 2, 1)


    background.tile(4, 2, 2)


    background.tile(5, 2, 3)


    background.tile(6, 2, 4)


    background.tile(7, 2, 0)  # blank white


    background.tile(2, 3, 0)  # blank white


    background.tile(3, 3, 5)


    background.tile(4, 3, 6)


    background.tile(5, 3, 7)


    background.tile(6, 3, 8)


    background.tile(7, 3, 0)  # blank white


    background.tile(2, 4, 0)  # blank white


    background.tile(3, 4, 9)


    background.tile(4, 4, 10)


    background.tile(5, 4, 11)


    background.tile(6, 4, 12)


    background.tile(7, 4, 0)  # blank white


    background.tile(2, 5, 0)  # blank white


    background.tile(3, 5, 0)


    background.tile(4, 5, 13)


    background.tile(5, 5, 14)


    background.tile(6, 5, 0)


    background.tile(7, 5, 0)  # blank white


    # Controls fps
    game = stage.Stage(ugame.display, constants.FPS)
    # Displays background as a layer
    game.layers = [background]
    game.render_block()
    # Displays the splash scene for two seconds and then switches onto main screen
    while True:
        time.sleep(2.0)
        menu_scene()
# RST 7, menu scene




def menu_scene():
    # Takes an image from the bank RST 7
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    # adds the text on screen RST 7
    text = []
    text1 = stage.Text(width=29, height=12, font=None,
                       palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("Sigma Production Presents")
    text.append(text1)
    # adds the text on screen RST 7
    text2 = stage.Text(width=29, height=12, font=None,
                       palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START!")
    text.append(text2)
    # Sets the background to image 0 RST 7
    background = stage.Grid(image_bank_mt_background,
                            constants.SCREEN_X, constants.SCREEN_Y)
    # creates an fps ratio on which image will be displayed RST 7
    game = stage.Stage(ugame.display, constants.FPS)
    # sets the layers RST 7
    game.layers = text + [background]
# render block RST 7
    game.render_block()


    while True:
        keys = ugame.buttons.get_pressed()


        if keys & ugame.K_START != 0:
            game_scene()


        game.tick()




def game_scene():
    # Basically game function
    def show_alien():
        # This function is responsible for adding alien on a screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(
                    0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break
    # Access the image from the files with the use of bank
    image_bank_background = stage.Bank.from_bmp16(
        "space_aliens_background.bmp")
    # Access to sprite from space_aliens.bmp
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")


    # RST 6 - sets button values from constant for future reference
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    pew_sound = open("pew.wav", 'rb')
    # Prepares the sound RST 6, WATCH THE VIDEO AND PLAY WITH BUTTONS FOR PARTIAL
    sound = ugame.audio
    sound.stop()
    sound.mute(True)
    # Sizes the image and participates in display of image due to grid
    background = stage.Grid(image_bank_background, 10, 8)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)


    # RST 5, basically performs calculation for Y coordinate while leaving the sprite and X alone.
    ship = stage.Sprite(image_bank_sprites, 5, 75,
                        constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    # RST 9/any other update abt adding aliens as a part cuz you need them for program
    aliens = []
    # Creates aliens and regulates their amount with for loop and appends them to aliens on top
    for alien_number in range(constants.TOTAL_NUMBER_OF_ENEMY):
        single_alien = stage.Sprite(
            image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        aliens.append(single_alien)
    show_alien()


    # RST 9 which creates lasers and controls their amount.
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        single_laser = stage.Sprite(
            image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        lasers.append(single_laser)


    # 5 is an image taken from our file while 75 and 66 are the x and y coordinates to set the sprite
    game = stage.Stage(ugame.display, 60)
    # Arrays create a nice flow for image to display
    game.layers = [ship] + aliens + lasers + [background]
    # Render block
    game.render_block()
    # Place holder for now
    while True:


        # Keys MAY NOT WORK AND CAUSE ERROR 06-04-2025, RST 4
        keys = ugame.buttons.get_pressed()
        # Sets specific parameter to be execute by a button pressed by the user or key
        if keys & ugame.K_X:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
               a_button = constants.button_state["button_up"]
        # RST 9, update for shooting for A button , refer to RST 9 video
        if keys & ugame.K_O != 0:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:  # RST 05 boundaries were added as in K_LEFT
            if ship.x <= constants.SCREEN_X:
                ship.move(ship.x + 1, ship.y - 1)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_LEFT:  # RST 05 changes applied in terms of boundary
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP:  # RST 05 EXPERIMENTAL MOVEMENT IN TERMS OF BOUNDARIES AND SIGNS FOR SHIP.Y +/- 1 CHANGED
            if ship.y <= constants.SCREEN_Y:
                ship.move(ship.x, ship.y + 1)
            else:
                ship.move(ship.x, 0)
        if keys & ugame.K_DOWN:  # RST 05 EXPERIMENTAL MOVEMENT IN TERMS OF BOUNDARIES AND SIGNS FOR SHIP.Y +/- 1 CHANGED
            if ship.y <= 0:
                ship.move(ship.x, ship.y - 1)
             else:
                ship.move(ship.x, 0)


                # RST 9 video
        if a_button == constants.button_state["button_just_pressed"]:
            # Fires a laser and plays a sound if A button is pressed RST 9
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break
        # RST 9 video each frame moves a shot laser
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(
                    lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        # RST 10 basically puts aliens into random places in pybadge and controls their amount on pybadge
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(
                    aliens[alien_number].x, aliens[alien_number].y + constants.ENEMY_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien()
 # redraw Sprites
        game.render_sprites(lasers + [ship] + aliens)
        # makes sure the ship is always on screen
        game.tick()
        # This makes sure the ship renders at 60 Hz per frames




if __name__ == "__main__":
    splash_scene()
