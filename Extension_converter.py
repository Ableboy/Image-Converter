# changing jpeg to png file
import sys # call from command line (cml)
import os # calling using cml
from PIL import Image # This module or package keeps design attractive.

# grap first and second argument
img_name = sys.argv[1]
convert_img = sys.argv[2]
# check if \new exists, if not create it
if not os.path.exists(convert_img):
    os.makedirs(convert_img)
# loop over the imgs
for filename in os.listdir(img_name):
    # convert imgs to png
    change_img = Image.open(f"{img_name}{filename}")
    # still having .jpg as extension but to remove, use splitext and access the real filename by [0]
    clean_img = os.path.splitext(filename)[0]
    # save all to new folder
    change_img.thumbnail((400, 400)) # resize to compress
    change_img.save(f"{convert_img}{clean_img}.png", "png") # "png" is an extension needed.
    print("all done!")

		

