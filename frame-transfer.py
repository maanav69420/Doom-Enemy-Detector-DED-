import os
import cv2 as cv
import random 
from pathlib import Path

# ||=======[ this program should take a image from dir and transfer it to a new dir]=======||
main = r'enemies'
dest = "enemies/selective-dataset"

if not os.path.exist(dest):
        os.makedir(dest)

roots = [root for root,_,_ in os.walk(main)]
roots.pop(0)
counter = 0

# ||=======[ function to extract dir name from the path ]=======||
def extract_dir_name(current_root , dest):
    dir_name =os.path.basename(current_root)
    if not os.path.exist(dest + "/" + dir_name):
        os.makedir(dest + "/" + dir_name)
    
    return dir_name


# ||=======[ function to randomly choose a the file from unique list and transerfing it to the ]=======||
def random_choice(percent , unique_list, dir_name):
    file_dict = {file_name : 0
                 for file_name in unique_list
                 if os.path.isfile(os.path.join(roots[counter] , file_name))}
    
    taken = (percent * len(unique_list))//100
    pick = 0
    random.seed(10)

    while pick < taken:
         random_file = random.choice(unique_list)
         if file_dict.get(random_file) > 1:
              file_dict[random_file] += 1
              continue
         else:
              file_dict[random_file] += 1
              pick += 1

    for key , value in file_dict.items():
         if value == 1:
           Path('enemies/zombie/filename.png').rename( Path('enemies/imp/filename.png') )   

    #||==================[if the percent is less than 50, increment the value, if pick the files whose value is 1]==================||
    #||==================[if the duplicacy occur (value == 1), do not increment the value and pick]==================||
    
# ||=======[ while loop must traverse the roots list ]=======||
while counter < len(roots):
        
    dir_name = extract_dir_name(roots[counter] , dest)

    src_list_dir , dest_list_dir = set(os.listdir(dir_name)), set(os.listdir(dest + "/" + dir_name))
         
    unique_list = list((src_list_dir or dest_list_dir) - (src_list_dir & dest_list_dir))

    percent = int(input(f"how much percent of images from {roots[counter]} |===> "))
    random_choice(percent , unique_list)

    # print(file_dict)
    counter += 1



#while counter <= root:
#   current_root = root[counter]
#   list_dir = os.listdir(current_root)
#   file_dict = {file_name : 0
#   for file_name in list_dir
#   if os.path.isfile(os.path.join(current_root, file_name))
#}
# Path('enemies/zombie/filename.png').rename( Path('enemies/imp/filename.png') )

# random.seed(2)
# list = ['apple' , 'banana' , ' cherry']
# print(list)
# random.shuffle(list)
# print(list)
