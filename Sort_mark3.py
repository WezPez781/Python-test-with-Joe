import os
import time
import shutil

# the basic path
# this puts us in like the user profile 
Path = os.environ["USERPROFILE"] # = C:\Users\sudhesh
#Path for the desktop
desktop = os.path.join(Path,"desktop")
#desktop list
res_desktop = os.listdir(desktop)


#folder maker
for x in res_desktop:
    if "." in x.lower():
        file_type = x.split(".")[1]
        print ("file_type:",file_type)
        #check for folder file type
        file_path = os.path.join(desktop,x)
        folder_type = os.path.join(desktop, file_type)
        
        source = file_path
        destination = folder_type
        dest = shutil.move(source, destination, copy_function = shutil.copytree) 
        
        print ("file path ######",file_path)
        print ("folder_type #####",folder_type)
        
        if not os.path.exists(folder_type):
            os.makedirs(folder_type, exist_ok = True)
            print ("folder made :",folder_type)


