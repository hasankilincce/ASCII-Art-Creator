def pixelCounter(image, size=32):
    image_resize = image.resize((size, size)).convert("L")
    dataset = [image_resize.getpixel((y, x)) for x in range(size) for y in range(size)]
    return dataset

def avarageLight(data, characters):
    pixel_max = max(data)
    pixel_min = min(data)

    pixelValue = (pixel_max - pixel_min) // len(characters)

    return pixelValue

def characterAppoint(characters, pixelValue, pixels):
    i = 0
    while i <= len(characters) - 1:
        if pixelValue * i <= pixels < pixelValue * (i + 1):
            return characters[i]
        i += 1
    return characters[-1]

def calculate_brightness(image):
    grayscale = image.convert('L')
    histogram = grayscale.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else brightness / scale