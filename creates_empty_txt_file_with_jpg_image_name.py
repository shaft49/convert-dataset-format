#image are in the images folder
#created .txt file will be in the labels folder
import os

def main():
    dir_path = 'images'
    extensions = ['.jpg']
    dir_list = [file for file in os.listdir(dir_path)
                if any(file.endswith(ext) for ext in extensions)]
    #print(dir_list)
    output_dir = 'labels'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for image_name in dir_list:
        file_name = image_name.split('.')[0]
        #print(file_name)
        text_file_path = output_dir + "/" + file_name + ".txt"
        if not os.path.exists(text_file_path):
            f = open(text_file_path, 'w')
            f.close()


if __name__ == "__main__":
    main()