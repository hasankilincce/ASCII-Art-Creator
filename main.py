from PIL import Image
import ascii

# You can change the characters and characters number, it has been optional
characters = " .'`^/,:;I!l>i<~+_?-][}{1)(|\/tfjrxnucvzXYJCQ0OZmwqpbdkhao*#MW8%B@$"

# import the photo you want
image_path = input("Please enter the name of the image: ")

# You should change this according to your own information "/Users/hasankilinc/Desktop/ASCII ART/Images/"
dp = Image.open("/Users/hasankilinc/Desktop/ASCII ART/Images/"+image_path)



# k is size of the photo, also you can change this other than your size of the photo | k = 64x64
k = 64

# Resize and pull the value of pixels | you can find the function code at ascii.py
dataset = ascii.pixelCounter(dp, k)
brightness = ascii.calculate_brightness(dp)

if brightness >= 0.5:
    characters = characters[::-1]

# Convert pixels value to character | if we want to process it quickly we have to create it
pixelValue = ascii.avarageLight(dataset, characters)

# Output loop
for i, pix in enumerate(dataset):
    if i % k != 0:
        print(ascii.characterAppoint(characters,  pixelValue, pix), end=" ")
    else:
        print("")