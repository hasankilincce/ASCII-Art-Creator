from PIL import Image
import ascii

characters = "_.,-=+:;cba!?0123456789$W#@ÑÑ"  # Karakterleri değiştirebilrisiniz / Az yoğundan çok yoğuna doğru gitmeli
# Karakter sayısı farketmez (37/38. satır sayesinde)
dp = Image.open("/Users/hasankilinc/Desktop/ASCII ART/Images/applepix.png")  # açmak istediğiniz resimi çekin
k = 64  # Fotoğrafın boyutu / k= 64 ise 64x64


# Dinamik şekilde boyut ayarlamak ve kare yapmak için

dataset = ascii.pixelCounter(dp, k)
# Görüntü bilgilerine göre ışık ayarı yapmak için pandas'dan yararlanacağız

pixelValue = ascii.avarageLight(dataset, characters)

# piksel parlaklığına göre karakter ataması
# piksellerin max ve min ve mean değerlerine göre belli bir aralık algoritma fonksiyonu
# characters isimli stringteki karakter sayısına bölerek her karakterin aralığını belirliyoruz
# seçilen karakteri return ile çıktı alıyoruz.
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
            print(ascii.characterAppoint(characters, pixelValue, pix), end=" ")
        elif i % k == 0:
            print("")
        i += 1