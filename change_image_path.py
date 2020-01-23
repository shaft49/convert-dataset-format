
def change_path(filename):
    f = open(filename, 'r')
    f1 = open('output.txt', 'w+')
    lines = f.readlines()
    for text in lines:
        demo_text = text.rstrip('\n')
        new_path = 'custom_data/images/' + demo_text + '.jpg\n'
        f1.write(new_path)
    f.close()
    f1.close()

if __name__ == "__main__":
    filename = 'test.txt'
    change_path(filename)