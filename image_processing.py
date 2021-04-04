
#https://pillow.readthedocs.io/en/stable/
from PIL import Image, ImageFilter

img = Image.open('./pokedox/pikachu.jpg')

#to blur the image
blur_img = img.filter(ImageFilter.BLUR) 
blur_img.save("sharp.png", 'png')

#to blur the image
sharpen_img = img.filter(ImageFilter.SHARPEN)
sharpen_img.save("sharp.png", 'png')

#to grey the image
grey_img = img.convert('L')
grey_img.save('grey.png', 'png')
#grey_img.show() ---to show the image

#to roate the image
rotate_img = img.rotate(90) #90 degree rotate
rotate_img.save("rotated.png", 'png')
#rotate_img.show()

#to resize an image
resize_img = img.resize((1, 300)) #a tuple needs to be passed as an argument.
resize_img.save("resize.png", 'png')
resize_img.show()