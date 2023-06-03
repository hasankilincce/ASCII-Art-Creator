import pandas as pd

def pixelCounter(image, size = 32):
    image_resize = image.resize((size, size))
    image_gray = image_resize.convert("L")

    dataset = []

    for x in range(image_gray.height):
        for y in range(image_gray.width):
            pixel = image_gray.getpixel((y, x))
            dataset.append(pixel)

    return dataset

def avarageLight(data, characters):
    df = pd.DataFrame(data)

    # Max ve min değerleri alarak bunu eşit aralıklara böleceğiz
    dp_pixel_max = df.max()
    dp_pixel_min = df.min()

    dp_pixel_max = int(dp_pixel_max)
    dp_pixel_min = int(dp_pixel_min)

    pixelValue = (dp_pixel_max - dp_pixel_min) / (len(characters))
    pixelValue = round(pixelValue)  # Tam sayıya yuvarla

    return pixelValue

def characterAppoint(characters, pixelValue, pixels):
    i = 0
    while i <= len(characters) - 1:
        if pixelValue * i <= pixels < pixelValue * (i + 1):
            character = characters[i]
            i += 1
            return character

        else:
            i += 1