from PIL import Image, ImageFilter # This lib changes img files to fix size and output fit

img = Image.open(".\pokedex\Astro.jpg")

img.thumbnail((400, 400))
img.save('thumbnail.png', 'png')

'''Changing of images outlook'''
re_img = Image.open('charmander.jpg')
# Blur the input image using the filter ImageFilter.BLUR
img_converter = re_img.filter(filter=ImageFilter.BLUR)
# Save your filtering img

img_converter.save('Blur.png', 'png')
print('Successful converted')
                    
# or to any filter form

real_img = Image.open('bulbasaur.jpg')
img_convert = real_img.filter(filter=ImageFilter.SMOOTH)
# Save your filtering img

img_convert.save('Smooth.bmp', 'bmp')
print('Conversion succussful')
