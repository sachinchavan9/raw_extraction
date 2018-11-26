# -*- coding: utf-8 -*-
import os
from tqdm import tqdm
from pytesseract import image_to_string
from datetime import datetime

now = datetime.now()

file_name = "RAW_EXTRACTION_{}.txt".format(now.strftime("%d-%b-%Y-%I-%M-%S"))

raw_list = list()


def raw_extraction():
    image_dir_path = raw_input("Image directory path: ")
    output_dir_path = raw_input("Output dirctory path: ")
    images = os.listdir(image_dir_path)
    for files in tqdm(images):
        image = os.path.join(image_dir_path, files)
        raw_list.append(image_to_string(image))
    print("please wait while file {} is writing".format(file_name))
    with open(os.path.join(output_dir_path, file_name), 'w') as f:
        f.write("\n".join(raw_list).encode('utf-8'))
    f.close()
    print("done")
    return None


if __name__ == "__main__":
    raw_extraction()
