import tkinter as t
from PIL import Image
from resizeimage import resizeimage


def crop_image():
    # Load the original image:
    img = Image.open("/home/raja/Pictures/101_logo_Screenshot from 2017-08-13 17-15-08.png")
    img.show();

    #100px * 100px, starting at the top-left corner...
    img2 = img.crop((0, 0, 100, 100))
    img2.save("/home/raja/Pictures/img2.png")
    width = img.size[0]
    height = img.size[1]
    img3 = img.crop(
        (
            width - 100,
            height - 100,
            width,
            height
        )
    )
    img3.save("/home/raja/Pictures/img3.png")

    #100px * 150px, starting in the center....
    half_the_width = int(img.size[0] / 2)
    half_the_height = int(img.size[1] / 2)
    print(half_the_width, half_the_height);
    img4 = img.crop(
        (
            half_the_width - 50,
            half_the_height - 75,
            half_the_width + 50,
            half_the_height + 75
        )
    )
    img4.save("/home/raja/Pictures/img4.png");

    #Pad the image to a square
    longer_side = max(img.size)
    horizontal_padding = int((longer_side - img.size[0]) / 2);
    vertical_padding = int((longer_side - img.size[1]) / 2);
    img5 = img.crop(
        (
            -horizontal_padding,
            -vertical_padding,
            img.size[0] + horizontal_padding,
            img.size[1] + vertical_padding
        )
    )
    img5.save("/home/raja/Pictures/img5.png")

def resize_image():
    fd_img = open('/home/raja/Pictures/101_logo_Screenshot from 2017-08-13 17-15-08.png', 'r+b')
    img = Image.open(fd_img)
    img = resizeimage.resize_cover(img, [200, 200])
    img.save('/home/raja/Pictures/101_logo_Screenshot from 2017-08-13 17-15-08-cover.png', img.format)
    fd_img.close()


##root = t.Tk();
##image = t.PhotoImage(file = '/home/raja/Pictures/img5.png');
##l = t.Label(root, image = image).grid(row = 0, column = 1);
##root.mainloop();

#crop_image();

resize_image();
