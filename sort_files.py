
#adapted from https://digitalcollections.wp.txstate.edu/2018/04/04/using-python-to-create-directories-and-move-files/
#added terminal entry



import os
import shutil
import sys

dir = str(sys.argv[1]) + "/"

for file in os.listdir(dir):
    # get the first 6 letters, which is row and column
    # the index number and extension
    dir_name = file[0:6]
    print(f'dir_name: {dir_name}')

    dir_path = dir + dir_name
    print(f'dir_path: {dir_path}')

    # check if directory exists or not yet
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    if os.path.exists(dir_path):
        file_path = dir + file
        print(f'file_path: {file_path}')

        # move files into created directory
        shutil.move(file_path, dir_path)


#Get list
# countries = f500['country']
# countries_counts = countries.value_counts()
# f = list(countries_counts.index)
# print(len(f))"
