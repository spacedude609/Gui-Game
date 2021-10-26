from guizero import App, Text, PushButton, ButtonGroup
from sys import exit
from time import sleep
from winsound import *
# winsound is used is for playing the .wav file included with the program


def e():
    """Kills the app and script"""
    app.destroy()
    exit(["END"])


def BEPIS():
    """ Function that runs when you press the big green button """
    q1 = app.question("?", "?", "Type Something...")
    if q1 == "" or q1 == "Type Something...":
        app.warn("WARNING!", "You didn't type anything!, Face the consequences...")
        app.error("", "")
        app.error("", "There was a problem displaying this popup. Please try again.")
        app.error("Error", "There was a problem displaying the title of the previous popup. Please try again.")
        e()
    elif q1 == "butt jimm":
        PlaySound('Uh_Oh.wav', SND_FILENAME)
        app.error("eqdhdueehd4gdt3r45retw3e73de63et36ete36te63et3hhudwudhw",
                  "ERR_BUTT_JIMMgedygdetdtefdtedtedftefdtefdtefdtefdtefdetdfetdyehdyegvfrgfyrhHDDHDYDGEYDGEYDECMFMVVNFHCGETFDEFDTEDTDFEDHEFURHGURHFURHFURHFRUFURHFRKKYHJYIHJYIHJIYJHIYJHYIHJIJHAFAGAGAGAGAGGAGAHDHRFUHYGEYGDEYGEDYGEDYGEDYGEDhshshgfgfr")
        e()
    elif q1 == "yup":
        # next stage
        app.info("Congrats!", "You did it!")
        Yee = Text(app, text="Huh, guess you're right...", size=10, font="Comic Sans MS", color="black")
        White.destroy()
        bepis.destroy()
        Yee.destroy()
        BONER()


def BONER():
    """Progresses to the nest game stage"""
    bonerc = ButtonGroup(app, options=[["What", "W"], ["Am", "A"], ["I", "I"], ["Doing?", "D"]], selected="W")
    what = app.question("Where am I?", "Who am I?", initial_value="What am I?")
    if what == "Why?":
        # The story path splits here. If you say Why you must say no next.
        # Saying yes does nothing. Or you can say anything else and you can get ending 1
        dec = app.yesno("Question...", "Am I decent?")
        if dec == False:
            app.info("Congrats", "Data sent succesfully!")
            app.error("ERROR", "An unknown error occured")
            app.info("Goodbye", "Shutting down...")
            app.destroy()
        elif dec:
            Text(app, text="Why thank you!", font="Comic Sans MS", size="20")
            bonerc.destroy()
        else:
            Whyy = app.question("?", "Then what am I?", "Worthless")
            if Whyy == "Worth":
                Text(app, text="Whee", font="Times New Roman", size=30)
                Text(app, text="Ow my balls")
                Text(app, text="Why tank you!", size=10)


app = App(title="What the heck is this?", width=6, height=9, layout='auto')
bepis = PushButton(app, command=BEPIS, text="Well this isn't right")
bepis.bg = "green"
White = Text(app, text="This button should be white!", size=10, font="Arial", color="black")
bye = PushButton(app, e, text="Quit", align="right")
bye.bg = "red"
name = app.question("Name:", "What is your name?")
app.set_full_screen()
app.info("IMPORTANT!", "Press Esc. to exit full screen")
app.display()
