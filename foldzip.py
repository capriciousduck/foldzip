import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--folder", "-f", type=str, help = "Type the folder name")
args = vars(ap.parse_args())

# directory = os.getcwd()
folder_name = args["folder"]
# for folder in os.listdir(directory):
#     if os.path.isdir(folder):
#         os.system("detox {}".format(folder))
cwd = os.getcwd()

if folder_name in os.listdir(cwd) and os.path.isdir(folder_name):

    os.system("mkdir {}-FOLDZIP".format(folder_name))
    os.system("sudo zip -r -0 {}.zip {}".format(folder_name,folder_name))
    os.system("sudo mv {} {}-FOLDZIP/".format(folder_name,folder_name))
    os.system("sudo mv {}.zip {}-FOLDZIP/".format(folder_name,folder_name))
    
else:

    print("Folder doesn't exist!")
