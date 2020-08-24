import argparse
import os
import cv2
# USAGE: python3 nuaa_train_test_split.py -d ClientFace -t client_train_face.txt -o train/real
# python3 nuaa_train_test_split.py -d ImposterFace -t imposter_train_face.txt -o train/fake
# python3 nuaa_train_test_split.py -d ClientFace -t client_test_face.txt -o test/real
# python3 nuaa_train_test_split.py -d ImposterFace -t imposter_test_face.txt -o test/fake
class TrainTestSplitter:
    def __init__(self, dataset_path, txt_file, output):
        self.dataset_path = dataset_path
        self.txt_file = txt_file
        self.output_path = output

    def process(self):
        with open(self.txt_file, 'r') as f:
            data = f.read().split('\n')
            image_path = [d.split(' ')[0] for d in data]
            for path in image_path:
                path = path.replace('\\', '/')
                file_path = os.path.sep.join([self.dataset_path, path])
                try:
                    image_name = file_path.split('/')[-1]
                    saved_path = os.path.sep.join([self.output_path, image_name])

                    print(f"[INFO] Writing {saved_path}")
                    image = cv2.imread(file_path)
                    cv2.imwrite(saved_path, image)
                except Exception as e:
                    print(e) 

    def run(self):
        print(f"[INFO] Script is running: dataset = {self.dataset_path}, text file = {self.txt_file}, output = {self.output_path}")
        if not os.path.exists(self.output_path):
            print(f'[INFO] output folder created {self.output_path}')
            os.makedirs(self.output_path)
        
        self.process()
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--dataset", type = str, required = True, help = "Path to the dataset folder")
    ap.add_argument("-t", "--textfile", type = str, required = True, help = "Path to the text file containing image name")
    ap.add_argument("-o", "--output", type = str, required = True, help = "Path to the output folder")
    args = vars(ap.parse_args())

    splitter =  TrainTestSplitter(dataset_path = args["dataset"], txt_file = args["textfile"], output = args["output"])
    splitter.run()

    print('[INFO] End of script')