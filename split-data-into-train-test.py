import xml.etree.ElementTree as ET
import os
import cv2
import argparse
import shutil
import random
parser = argparse.ArgumentParser()
parser.add_argument('--file_name', help = 'give name of the dataset file', required = True)
parser.add_argument('--train_name', help = 'give name of the train file', required = True)
parser.add_argument('--test_name', help = 'give name of the test file', required = True)

def split(file_name, train_name, test_name):
    train = open(train_name, 'w')
    test = open(test_name, 'w')
    with open(file_name, 'r') as f:
        read_data = f.read()
        items = read_data.split('\n')
        random.shuffle(items)
        div = int(len(items) * 0.8)
        train_file = items[:div]
        test_file = items[div:]
        for i in train_file:
            train.write(f'{i}\n')
        for i in test_file:
            test.write(f'{i}\n')
        print(len(items), div, len(train_file), len(test_file))

if __name__ == "__main__":
    #Converts PASCAL-VOC to YOLO format
    args = parser.parse_args()

    print(args.file_name, args.train_name, args.test_name)
    split(args.file_name, args.train_name, args.test_name)
