from PIL import Image
fin = r'pigeon.PNG'
fout = r'pigeon.ico'
img = Image.open(fin)
img.save(fout)
