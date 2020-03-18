# convert-dataset-format
# PASCAL-VOC to YOL0
python pascal-voc-to-yolo.py --images [image_folder_path] --labels [pascal-voc labelled folder] --output [output folder] --image_path [image path prefix]

#SCUT-HEAD to YOLO
SCUT-HEAD uses PASCAL-VOC format, so PASCAL-VOC to YOLO scripts will work here.

#SPLIT DATASET

python split-data-into-train-test.py --filename [original dataset path file] --train_name [train file path] --test_name [test file path]

It splits the dataset into training and testing. First it randomly shuffle the dataset and puts 80% into training set and 20% into testing set.
