# convert-dataset-format
# PASCAL-VOC to YOL0
python pascal-voc-to-yolo.py --images [image_folder_path] --labels [pascal-voc labelled folder] --output [output folder] --image_path [image path prefix]

# SCUT-HEAD to YOLO
SCUT-HEAD uses PASCAL-VOC format, so PASCAL-VOC to YOLO scripts will work here.

# SPLIT DATASET

python split-data-into-train-test.py --filename [original dataset path file] --train_name [train file path] --test_name [test file path]

It splits the dataset into training and testing. First it randomly shuffle the dataset and puts 80% into training set and 20% into testing set.


# NUAA-FACE-LIVENESS Dataset

    USAGE: python3 nuaa_train_test_split.py -d ClientFace -t client_train_face.txt -o train/real
    python3 nuaa_train_test_split.py -d ImposterFace -t imposter_train_face.txt -o train/fake
    python3 nuaa_train_test_split.py -d ClientFace -t client_test_face.txt -o test/real
    python3 nuaa_train_test_split.py -d ImposterFace -t imposter_test_face.txt -o test/fake