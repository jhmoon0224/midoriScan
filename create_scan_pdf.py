
from PIL import Image
import os
import img2pdf
import argparse
import sys

class ImageNameConvert:
    def change_name(self, scan_path, image_prefix):

        os.chdir(scan_path)
        files  = filter(os.path.isfile, os.listdir(scan_path))

        i = 0
        for f in files:
            rename_file = "{0}{1:04}.png".format(image_prefix, i)
            print("source {}, rename{}\n".format(f, rename_file))
            os.rename(f, rename_file)
            i = i+1

class NoteImgaeToPdfConvert(object):

    def __init__(self, scan_path, image_prefix, image_num):
        self.scan_path = scan_path;
        self.image_file_name_prefix = image_prefix;
        self.images_num = image_num;
        self.image_postfix_start=1

        os.chdir(self.scan_path )

    def split_and_save_image(self, orig_image_file_name, left_image_file_name, right_image_file_name):
        print("Input image:{} left:{} right:{}".format(orig_image_file_name,left_image_file_name, right_image_file_name))
        
        orig_image = Image.open(orig_image_file_name)

        width, height = orig_image.size

        left_page_image = Image.new('RGBA', (width, int(height/2)))
        right_page_image = Image.new('RGBA', (width, int(height/2)))
        left_page_image = orig_image.crop((0,0, width/2, height) )
        right_page_image = orig_image.crop((width/2, 0, width, height))
        left_page_image.save(left_image_file_name)
        right_page_image.save(right_image_file_name)

    def split(self):
        front_left_postfix=self.images_num
        front_right_postfix=self.images_num+1
        back_left_postfix=self.images_num+2
        back_right_postfix=self.images_num-1


        for i in range(1, self.images_num, 2):
            print("\n==============")
            front_scan_image_name = "{0}{1:04}.png".format(self.image_file_name_prefix ,i)
            back_scan_image_name =  "{0}{1:04}.png".format(self.image_file_name_prefix ,i+1)

            print("[2 file] {0}, {1}".format(front_scan_image_name, back_scan_image_name))

            self.split_and_save_image(front_scan_image_name,
                'new_{0}{1:04}.jpg'.format(self.image_file_name_prefix, front_left_postfix),
                'new_{0}{1:04}.jpg'.format(self.image_file_name_prefix, front_right_postfix))
            self.split_and_save_image(back_scan_image_name,
                'new_{0}{1:04}.jpg'.format(self.image_file_name_prefix, back_left_postfix),
                'new_{0}{1:04}.jpg'.format(self.image_file_name_prefix, back_right_postfix))


            front_left_postfix-=2
            front_right_postfix+=2
            back_left_postfix+=2
            back_right_postfix-=2
     
    def export_pdf(self, pdf_file_name):
        files = os.listdir(self.scan_path)

        image_files = [ f for f in files if f.endswith('.jpg')]
    
        pdf_file = open(pdf_file_name, "wb")
        pdf_file.write(img2pdf.convert(image_files))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("please configure image path ")
    
    print("len({})".format(len(sys.argv)))
    input_path = sys.argv[1]
    input_prefix = sys.argv[2]

    print("path({}), prefix({}".format(input_path, input_prefix))

    #input_path = 'D:\\Scan\\2020\\TravelersNote_2020_Collection_1'', 32)
    #input_prefix = ,'TraverlersNote_2020_collection_log_1_'
    #input_image_new = 32
    pdf_convert = NoteImgaeToPdfConvert(input_path, input_prefix, 32)
    pdf_convert = NoteImgaeToPdfConvert('D:\\Scan\\2020\\TravelersNote_2020_Collection_1','TraverlersNote_2020_collection_log_1_', 32)
 # 
 #   pdf_convert.split()
    pdf_convert.export_pdf('D:\\Scan\\2020\\TravelersNote_2020_Collection_1\\a.pdf')
