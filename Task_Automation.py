import os
import fileinput

def find_replace(directory, find_text, replace_text):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.txt'):  
                file_path = os.path.join(root, file_name)
                with fileinput.FileInput(file_path, inplace=True) as file:
                    for line in file:
                        print(line.replace(find_text, replace_text), end='')


path = input('Enter the directory path(Without quotes): ')
text_to_find = input('Enter the text to find: ')
text_to_replace = input('Enter the text to replace: ')

find_replace(path, text_to_find, text_to_replace)