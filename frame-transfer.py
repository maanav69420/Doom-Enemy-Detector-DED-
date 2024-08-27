import os
import random 
from pathlib import Path

# ||=============[ this program should take a image from dir and transfer it to a new dir]=============||

# ||=======[ function to extract dir name from the path ]=======||
def extract_dir_name(current_root , dest):
    dir_name =os.path.basename(current_root)
    if not os.path.exist(dest + "/" + dir_name):
        os.makedir(dest + "/" + dir_name)
    
    return dir_name

# ||=======[ function to randomly choose a the file from unique list and transerfing it to the ]=======||
def random_choice(percent , get_item):
    file_dict = {file_name : 0
                 for file_name in get_item
                 if os.path.isfile(os.path.join(roots[counter] , file_name))}
    
    taken = (percent * len(get_item))//100
    pick = 0
    random.seed(10)
    
    while pick < taken:
         random_file = random.choice(get_item)
         if file_dict.get(random_file) > 1:
              file_dict[random_file] += 1
              continue
         else:
              file_dict[random_file] += 1
              pick += 1
    return file_dict
    
main = r'enemies'  
dest = "{main}/selective-dataset"

if not os.path.exist(dest):
        os.makedir(dest)

roots = [root for root,_,_ in os.walk(main)]
roots.pop(0)
counter = 0

# ||=======[ while loop must traverse the roots list ]=======||
while counter < len(roots):
        
    dir_name = extract_dir_name(roots[counter] , dest)

    src_list_dir , dest_list_dir = set(os.listdir(dir_name)), set(os.listdir(dest + "/" + dir_name))
    intersection = src_list_dir and dest_list_dir
    get_item = src_list_dir - intersection 

    percent = int(input(f"how much percent of images from {roots[counter]} |===> "))
    
    file_dict = random_choice(percent , get_item)
    file_dict = {key:value for key, value in file_dict.items() if value != 0} 
    file_dict = list(file_dict.keys()) # the list contain only those files whose key value is equal or greater than 1
    
    #||==================[if the percent is less than 50, increment the value, if pick the files whose value is 1]==================||
    #||==================[if the duplicacy occur (value == 1), do not increment the value and pick]==================|| 
    if percent <= 50:
        for i in range(len(file_dict)):
            print("File "+ file_dict[i] + "is transfered to {dir_name} of {main}")
            source , destination = Path("{main}/{dir_name}/{filr_dict[i]}") , Path("{dest}/{dir_name}/{file_dict[i]}")
            source.rename(destination)
    
    #||==================[if the percent is more than 50, create two pointers left and right]==================||
    #||==================[after left and right finish the traversal, mid must be transfered]==================|| 
    else:
         left , right = 0, len(file_dict)-1
         mid = abs(left - right)//2
         directions = [left, right]
         while (int(directions[0]) < mid) and (int(directions[1]) > mid):
              for point in range(len(directions)):
                  print("File "+ file_dict[directions[point]] + "is transfered to {dir_name} of {main}")
                  Path("{main}/{dir_name}/{file_dict[directions[point]}").rename(Path("{dest}/{dir_name}/{file_dict[directions[point]}")) 
              
              directions[0] += 1
              directions[1] -= 1
         
         print("File "+ file_dict[mid] + "is transfered to {dir_name} of {main}")
         Path("{main}/{dir_name}/{file_dict[mid]}").rename(Path("{dest}/{dir_name}/{file_dict[mid]}")) 
          
    counter += 1
         