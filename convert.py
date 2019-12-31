import xml.etree.ElementTree as ET
import os

def convert_labels(filepath, imagename):
    tree = ET.parse(filepath)
    root = tree.getroot()
    objs = root.findall('./object/bndbox')

    if not os.path.exists('Annotations'):
        os.mkdir('Annotations')
    text_file = os.path.join('Annotations', f'{imagename}.txt')
    f = open(text_file, 'w')
    for obj in objs:
        coord = {}
        for child in obj:
            coord[child.tag] = child.text
        xmin = float(coord['xmin']); xmax = float(coord['xmax']); ymin = float(coord['ymin']); ymax = float(coord['ymax'])
        #If you want a normalized version then divide x by original image heigh, and y by original image width
        x = (xmin + xmax)/2.0
        y = (ymin + ymax)/2.0
        w = xmax - xmin
        h = ymax - ymin
        f.write(f'0 {x} {y} {w} {h}\n')

def main():
    ano_dir = '../Head Detection/SCUT_HEAD_Part_A/Annotations'
    filename_list = os.listdir(ano_dir)
    cnt = 0
    for filename in filename_list:
        filepath = os.path.join(ano_dir, filename)
        convert_labels(filepath, filename.split('.')[0])

if __name__ == "__main__":
    #Converts SCUT Head Detection Dataset to YOLO format
    main()