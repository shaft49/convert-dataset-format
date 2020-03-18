import xml.etree.ElementTree as ET
import os
import cv2
import argparse
import shutil
parser = argparse.ArgumentParser()
parser.add_argument('--images', help = 'give folder path of the images', required = True)
parser.add_argument('--labels', help = 'give folder path of the pascal-voc labels', required = True)
parser.add_argument('--output', help = 'give name of the folder where the  converted yolo labels will be saved', required = True)
parser.add_argument('--image_path', help = 'give the prefix of the image path', required = True)
def convert_labels(filepath, imagename, img_dir, dir_name):
    tree = ET.parse(filepath)
    root = tree.getroot()
    objs = root.findall('./object/bndbox')

    width = float(root.find('./size/width').text)
    height = float(root.find('./size/height').text)
    nid_type = root.find('./object/name').text
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    text_file = os.path.join(dir_name, f'{imagename}.txt')
    img_file = os.path.join(img_dir, f'{imagename}.png')
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
            class_label = 0
            if nid_type == 'old_nid':
                class_label = 1
            f.write(f'{class_label} {x} {y} {w} {h}\n')
        except ZeroDivisionError:
	        print(f'Division by zero: width -> {width}, height -> {height}, path -> {text_file}')

def main(images, labels, output, image_path):
    ano_dir = labels
    img_dir = images
    filename_list = os.listdir(ano_dir)
    path_text = 'path.txt'
    f = open(path_text, 'w')
    for filename in filename_list:
        filepath = os.path.join(ano_dir, filename)
        img_file = image_path + filename.split('.')[0] + '.png'
        f.write(f'{img_file}\n')
        convert_labels(filepath, filename.split('.')[0], img_dir, output)
    f.close()


if __name__ == "__main__":
    #Converts PASCAL-VOC to YOLO format
    args = parser.parse_args()
    if os.path.exists(args.output):
        shutil.rmtree(args.output)
    print(args.images, args.labels, args.output)
    main(args.images, args.labels, args.output, args.image_path)
