CODE_TO_COLOUR = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff", "Amber": "#ffbf00",
                  "Amethyst": "#9966cc", "Aqua": "#00ffff", "Ash Grey": "#b2beb5", "Blue Green": "#0d98ba",
                  "BlueViolet": "#8a2be2", "DeepPink1": "#ff1493"}

print(CODE_TO_COLOUR)

colour_code = input("Enter colour: ")
while colour_code != "":
    if colour_code in CODE_TO_COLOUR:
        print(colour_code, "is", CODE_TO_COLOUR[colour_code])
    else:
        print("Invalid colour")
    colour_code = input("Enter colour: ")
