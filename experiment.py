import shutil
# set1 = set(["hello", "it's", "a", "me", "mario"])
# set2 = set(["hello", "mario", "it's", "chris patt"])

# # Correct set operations
# print("intersection: ", set1 & set2)
# print("union: ", set1 | set2)     
# print("difference: ", set1 - set2)

# intersection = set1 and set2
# print("set1 - intersection", set1 - intersection)
source = r'Doom-Enemy-Detector-DED-\enemies\Zombie.png'
dest = r'Doom-Enemy-Detector-DED-\enemies\zombie\Zombie_copy.png'

shutil.copy(source,dest)