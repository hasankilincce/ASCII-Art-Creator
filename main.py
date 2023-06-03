from PIL import Image
import pandas as pd

characters = "_.,-=+:;cba!?0123456789$W#@ÑÑ"  # Karakterleri değiştirebilrisiniz / Az yoğundan çok yoğuna doğru gitmeli
# Karakter sayısı farketmez (37/38. satır sayesinde)
dp = Image.open("/Users/hasankilinc/Desktop/ASCII ART/Images/applepix.png")  # açmak istediğiniz resimi çekin
k = 172  # Fotoğrafın boyutu / k= 64 ise 64x64


# Dinamik şekilde boyut ayarlamak ve kare yapmak için
def size(x):
    size = (x, x)
    return size


# Göresel düzenleme
dp_resize = dp.resize(size(k))
dp_gray = dp_resize.convert("L")

# Boş bir array oluştur
dataset = []

# Her pikselin değerini array'e append ediyoruz
for x in range(dp_gray.height):
    for y in range(dp_gray.width):
        pixel = dp_gray.getpixel((y, x))
        dataset.append(pixel)

# Görüntü bilgilerine göre ışık ayarı yapmak için pandas'dan yararlanacağız
df = pd.DataFrame(dataset)

# Max ve min değerleri alarak bunu eşit aralıklara böleceğiz
dp_pixel_max = df.max()
dp_pixel_min = df.min()

dp_pixel_max = int(dp_pixel_max)
dp_pixel_min = int(dp_pixel_min)

pixelValue = (dp_pixel_max - dp_pixel_min) / (len(characters))
pixelValue = round(pixelValue)  # Tam sayıya yuvarla


# piksel parlaklığına göre karakter ataması
# piksellerin max ve min ve mean değerlerine göre belli bir aralık algoritma fonksiyonu
# characters isimli stringteki karakter sayısına bölerek her karakterin aralığını belirliyoruz
# seçilen karakteri return ile çıktı alıyoruz.
def characterAppoint(pixels, i=0):
    while i <= len(characters) - 1:
        if pixelValue * i <= pixels < pixelValue * (i + 1):
            character = characters[i]
            i += 1
            return character

        else:
            i += 1


# Piksellerin her birini tek tek işleme almak

# i değişkenini atadık ve bunu while döngüsü ile bir sayaç haline getiriyoruz
# len(dataset) ile toplam piksel sayısını tespit ettikten sonra sayacın limitini piksel sayısına göre ayarlıyoruz
# for döngüsü ile her pikselin tek tek seçilmesini sağlıyoruz
# if i % k != 0 koşulu k^2 olan görüntünün bir satırının sırasını belirliyor
# elif koşulu sayesinde n. piksele gelindiğinde n/n den kalan 0 olur yani bir satırdaki piksel sayısı tamamlanmış olur
i = 0
while i < len(dataset):
    for pix in dataset:
        if i % k != 0:
            print(characterAppoint(pix), end=" ")
        elif i % k == 0:
            print("")
        i += 1
