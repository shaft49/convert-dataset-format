import random

class Shuffle:

    def shuffle_file_elements(self, filepath, output_file_path):
        with open(filepath, 'r') as f:
            read_data = f.read()
            items = read_data.split('\n')
            random.shuffle(items)
        with open(output_file_path, 'w') as output:
            for line in items:
                output.write(line)
                output.write('\n')

if __name__ == "__main__":
    shuffle_obj = Shuffle()
    shuffle_obj.shuffle_file_elements('train_v0_3.txt', 'output_train_v0_3.txt')