from PIL import Image
import ascii

characters = "_.,-=+:;cba!?0123456789$W#@ÑÑ"  # Karakterleri değiştirebilrisiniz / Az yoğundan çok yoğuna doğru gitmeli
dp = Image.open("/Users/hasankilinc/Desktop/ASCII ART/Images/applepix.png")  # açmak istediğiniz resimi çekin
k = 64  # Fotoğrafın boyutu / k= 64 ise 64x64

dataset = ascii.pixelCounter(dp, k)

pixelValue = ascii.avarageLight(dataset, characters)

i = 0
while i < len(dataset):
    for pix in dataset:
        if i % k != 0:
            print(ascii.characterAppoint(characters, pixelValue, pix), end=" ")
        elif i % k == 0:
            print("")
        i += 1