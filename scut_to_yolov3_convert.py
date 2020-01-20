import xml.etree.ElementTree as ET
import os
import cv2

def convert_labels(filepath, imagename, img_dir):
    tree = ET.parse(filepath)
    root = tree.getroot()
    objs = root.findall('./object/bndbox')
    dir_name = 'Annotations_yolo'

    width = float(root.find('./size/width').text)
    height = float(root.find('./size/height').text)

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    text_file = os.path.join(dir_name, f'{imagename}.txt')
    img_file = os.path.join(img_dir, f'{imagename}.jpg')
    if width == 0 or height == 0:
        current_image = cv2.imread(img_file)
        height, width, _ = current_image.shape
    f = open(text_file, 'w')
    for obj in objs:
        coord = {}
        for child in obj:
            coord[child.tag] = child.text
        xmin = float(coord['xmin']); xmax = float(coord['xmax']); ymin = float(coord['ymin']); ymax = float(coord['ymax'])
        try:
            x = (xmin + xmax) / (2.0 * width)
            y = (ymin + ymax) / (2.0 * height)
            w = (xmax - xmin) / width
            h = (ymax - ymin) / height
            f.write(f'0 {x} {y} {w} {h}\n')
        except ZeroDivisionError:
	        print(f'Division by zero: width -> {width}, height -> {height}, path -> {text_file}')

def main():
    ano_dir = '../Head Detection/SCUT_HEAD_Part_B/Annotations'
    img_dir = '../Head Detection/SCUT_HEAD_Part_B/JPEGImages'
    filename_list = os.listdir(ano_dir)
    for filename in filename_list:
        filepath = os.path.join(ano_dir, filename)
        convert_labels(filepath, filename.split('.')[0], img_dir)

if __name__ == "__main__":
    #Converts SCUT Head Detection Dataset to YOLO format
    main()
