import os

os.chdir('/content')
current_directory = os.getcwd()

os.mkdir('/content/my_folder')
os.chdir('/content/my_folder')
print(current_directory)
for i in range(1,11):
    file = open(f'file_number_{i}.py', 'w')
    file.close()
os.listdir('/content/my_folder')
