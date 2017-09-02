import os
from PIL import ImageColor
from PIL import Image


scan_path="C:\Users\jhmoon\scan_1"
image_file_name_prefix='tr_2016_04_'
#images_num=4
images_num=32



os.chdir(scan_path)

front_left_postfix=images_num
front_right_postfix=images_num+1
back_left_postfix=images_num+2
back_right_postfix=images_num-1


def split_and_save_image(orig_image_file_name, left_image_file_name, right_image_file_name):
    print "org image %s" % orig_image_file_name
    print("left {0} right{1}".format(left_image_file_name, right_image_file_name))
    orig_image = Image.open(orig_image_file_name)

    width, height = orig_image.size

    left_page_image = Image.new('RGBA', (width, height/2))
    right_page_image = Image.new('RGBA', (width, height/2))
    left_page_image = orig_image.crop((0,0, width/2, height) )
    right_page_image = orig_image.crop((width/2, 0, width, height))
    left_page_image.save(left_image_file_name)
    right_page_image.save(right_image_file_name)


for i in range(1, images_num, 2):
    print("\n==============");
    front_scan_image_name = "{0}{1:04}.png".format(image_file_name_prefix ,i)
    back_scan_image_name =  "{0}{1:04}.png".format(image_file_name_prefix ,i+1)

    print("[2 file] {0}, {1}".format(front_scan_image_name, back_scan_image_name))

    split_and_save_image(front_scan_image_name,
        'new_{0}{1:04}.jpg'.format(image_file_name_prefix, front_left_postfix),
        'new_{0}{1:04}.jpg'.format(image_file_name_prefix, front_right_postfix))
    split_and_save_image(back_scan_image_name,
        'new_{0}{1:04}.jpg'.format(image_file_name_prefix, back_left_postfix),
        'new_{0}{1:04}.jpg'.format(image_file_name_prefix, back_right_postfix))


    front_left_postfix-=2
    front_right_postfix+=2
    back_left_postfix+=2
    back_right_postfix-=2



    #print(back_scan_image_name)
