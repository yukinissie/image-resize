from PIL import Image

file_name = 'hoge.png'

# Filters
# - NEAREST
# - BOX
# - BILINEAR
# - HAMMING
# - BICUBIC
# - LANCZOS

def resize():
  img = Image.open(file_name)
  img_resize = img.resize((int(img.width), int(img.height)), Image.LANCZOS)
  img_resize.save('none_resize_' + file_name)
  img_resize = img.resize((int(img.width // 8), int(img.height // 8)), Image.LANCZOS)
  img_resize.save('resize_lanczos_2_' + file_name)
  img_resize = img.resize((int(img.width // 16), int(img.height // 16)), Image.LANCZOS)
  img_resize.save('resize_lanczos_3_' + file_name)
  img_resize = img.resize((int(img.width // 32), int(img.height // 32)), Image.LANCZOS)
  img_resize.save('resize_lanczos_4_' + file_name)
  img_resize = img.resize((int(img.width // 64), int(img.height // 64)), Image.LANCZOS)
  img_resize.save('resize_lanczos_5_' + file_name)
  img_resize = img.resize((int(img.width // 128), int(img.height // 128)), Image.LANCZOS)
  img_resize.save('resize_lanczos_6_' + file_name)

def reColourDepth():
  img = Image.open('none_resize_' + file_name)
  level1 = img.resize((int(img.width), int(img.height)), Image.NEAREST)
  level1.save('level1_' + file_name)
  img = Image.open('resize_lanczos_2_' + file_name)
  level2 = img.resize((int(img.width * 8), int(img.height * 8)), Image.NEAREST)
  level2.save('level2_' + file_name)
  img = Image.open('resize_lanczos_3_' + file_name)
  level3 = img.resize((int(img.width * 16), int(img.height * 16)), Image.NEAREST)
  level3.save('level3_' + file_name)
  img = Image.open('resize_lanczos_4_' + file_name)
  level4 = img.resize((int(img.width * 32), int(img.height * 32)), Image.NEAREST)
  level4.save('level4_' + file_name)
  img = Image.open('resize_lanczos_5_' + file_name)
  level5 = img.resize((int(img.width * 64), int(img.height * 64)), Image.NEAREST)
  level5.save('level5_' + file_name)
  img = Image.open('resize_lanczos_6_' + file_name)
  level6 = img.resize((int(img.width * 128), int(img.height * 128)), Image.NEAREST)
  level6.save('level6_' + file_name)

resize()
reColourDepth()