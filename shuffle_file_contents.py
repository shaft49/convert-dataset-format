import random
import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('--filename', required = True)
class Shuffle:

    def shuffle_file_elements(self, filepath):
        with open(filepath, 'r') as f:
            read_data = f.read()
            items = read_data.split('\n')
            random.shuffle(items)
        os.remove(filepath)
        with open(filepath, 'w') as output:
            for line in items:
                output.write(line)
                output.write('\n')

if __name__ == "__main__":
    args = parser.parse_args()
    shuffle_obj = Shuffle()
    shuffle_obj.shuffle_file_elements(args.filename)