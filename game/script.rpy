# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Characters
define ko = Character("Kota")
define le = Character("LEM")
define mi = Character("Milk")
define ce = Character("Celeste")
define cl = Character("Clementine")


# ------> Sprites

#Kota

#LEM

#Milk

#Celeste

#Clementine


# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    show kota happy
    ko "You've created a new Ren'Py game."

    show kota
    ko "Once you add a story, pictures, and music, you can release it to the world! Except don't because the shit i do is embarassing."
    show lem
    le "Yea for real."

    # This ends the game.

    return
