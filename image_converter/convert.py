from PIL import Image

data = []

img = Image.open('taco.bmp')
pixels = list(img.getdata())
for x in range(0, img.width):
    for y in range(0, img.height):
        i = y * img.width + x
        val = pixels[i][0]
        data.append( val < 128 )

encoded = []
while len(data) >= 8:
    b = data[:8]
    data = data[8:]
    b = sum(int(x)*2**i for i, x in enumerate(b))
    encoded.append(b)

assert len(data) == 0

print 'char img_data[%d] = {%s};' % (len(encoded), ', '.join(hex(x) for x in encoded), )
