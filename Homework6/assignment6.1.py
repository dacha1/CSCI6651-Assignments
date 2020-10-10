import os

os.chdir(os.path.join(os.getcwd(), "Homework1"))
print("Current working directory is:{}".format(os.getcwd()))
print("Directory Listing:{}".format(os.listdir()))
print("File/directory exists:" + str(os.path.exists("Assignment1.py")))

