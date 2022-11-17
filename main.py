# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author(s):
# Date:
# Description:

import cmpt120imageProjHelper
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()

# list of system options
# ***TO-DO: populate it to provide more functionalities***
system = [
            "Q: Quit",
            "O: Open Image",
            "S: Save Current Image",
            "R: Reload Original Image",
         ]
loop=True


# list of basic operation options
# ***TO-DO: populate it to provide more functionalities***
basic = [
          "1: Apply Red",
          "2: Apply Green",
          "3: Apply Blue",
          "4: Apply Sepia",
          "5: Apply Warm",
          "6: Apply Cold",
          "7: Switch to Advanced Functions",
         ]


# list of advanced operation options
# ***TO-DO: populate it to provide more functionalities***
advanced = [    "1: Rotate counter clockwise",
                "2: Rotate clockwise",
                "3: Double Image",
                "4: Half Image",
                "5: Locate Fish",
                "6: Switch to Basic Functions",
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")

    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")

    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
    Input:  state - a dictionary containing the state values of the application
            img - the 2d array of RGB values to be operated on
    Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()

    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)

        #quit from program
        if userInput == "Q": # this case actually won't happen, it's here as an example
            print("Log: Quitting...")
        
        #open UI to select image
        elif userInput =="O":
          tkinter.Tk().withdraw()
          openFileName= tkinter.filedialog.askopenfilename()

          #save openFilename to dictionary
          appStateValues["lastOpenFilename"]=openFileName

          img=cmpt120imageProjHelper.getImage(openFileName)
          cmpt120imageProjHelper.showInterface(img, "Stock Image", generateMenu(state))

        #save image with a selected filename
        elif userInput =="S":
          tkinter.Tk().withdraw()
          saveFileName = tkinter.filedialog.asksaveasfilename()

          #save image based off of what the user saves image as
          cmpt120imageProjHelper.saveImage(img,saveFileName+".jpg")
          
          cmpt120imageProjHelper.showInterface(img,saveFileName+".jpg",generateMenu(state))

        #reset image
        elif userInput =="R":
          #loads image from dictionary
          img=cmpt120imageProjHelper.getImage(appStateValues["lastOpenFilename"])
          cmpt120imageProjHelper.showInterface(img, "Stock Image", generateMenu(state))

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)

        #user is in basic functions
        if state["mode"] == "basic":

            #apply red filter
            if userInput =="1":
                redimg = cmpt120imageManip.applyRed(img)
                cmpt120imageProjHelper.showInterface(redimg, "Apply Red Filter", generateMenu(state))

            #apply green filter
            elif userInput=="2":
                greenimg = cmpt120imageManip.applyGreen(img)
                cmpt120imageProjHelper.showInterface(greenimg, "Apply Green Filter", generateMenu(state))

            #apply blue filter
            elif userInput=="3":
                bluimg = cmpt120imageManip.applyBlue(img)
                cmpt120imageProjHelper.showInterface(bluimg, "Apply Blue Filter", generateMenu(state))

            #apply sepia filter
            elif userInput=="4":
                sepiaimg = cmpt120imageManip.applySepia(img)
                cmpt120imageProjHelper.showInterface(sepiaimg, "Apply Sepia Filter", generateMenu(state))

            #apply warm filter
            elif userInput=="5":
                warmimg = cmpt120imageManip.applyWarm(img)
                cmpt120imageProjHelper.showInterface(warmimg, "Apply Warm Filter", generateMenu(state))

            #apply cold filter
            elif userInput=="6":
                coldimg = cmpt120imageManip.applyCold(img)
                cmpt120imageProjHelper.showInterface(coldimg, "Apply Cold Filter", generateMenu(state))
            
            #switch to advanced functions
            elif userInput == "7":
                print("Log: Performing " + basic[int(userInput)-1])
                state["mode"]="advanced"
                cmpt120imageProjHelper.showInterface(img,"Stock Image", generateMenu(state))

        #user is in advanced functions
        if state["mode"]=="advanced": 

            #rotate clockwise
            if userInput =="1":
              clockwiseimg = cmpt120imageManip.rotateImageLeft(img)
              cmpt120imageProjHelper.showInterface(clockwiseimg, "Rotated Clockwise", generateMenu(state))   

            #rotate counter-clockwise
            elif userInput =="2" :
              countclockwiseimg = cmpt120imageManip.rotateImageRight(img)
              cmpt120imageProjHelper.showInterface(countclockwiseimg, "Rotated Counter-Clockise" ,generateMenu(state))

            #double image
            elif userInput =="3":
              bigimg = cmpt120imageManip.zoomImage(img)
              cmpt120imageProjHelper.showInterface(bigimg, "Image Double" ,generateMenu(state))

            #half image
            elif userInput =="4":
              smallimg= cmpt120imageManip.halfImage(img)
              cmpt120imageProjHelper.showInterface(smallimg, "Image Halved", generateMenu(state))

            #find fish {ONLY WHEN fish.jpg IS SELECTED}
            elif userInput =="5":
              fish = cmpt120imageManip.fishBox(img)
              cmpt120imageProjHelper.showInterface(fish, "Loacate Fish", generateMenu(state))

            #switch to basic function
            elif userInput =="6":
              print("Log: Performing " + basic[int(userInput)-1])
              state["mode"]="basic"
              cmpt120imageProjHelper.showInterface(img,"Stock Image", generateMenu(state))

    else: # unrecognized user input
        print("Log: Unrecognized user input: " + userInput)
    return img



# *** DO NOT change any of the code below this point ***

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProjHelper.getBlackImage(300, 200) # create a default 300 x 200 black image
cmpt120imageProjHelper.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False          

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")

