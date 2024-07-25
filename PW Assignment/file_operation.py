# 15. Write a Python module named file_operations.py with functions for reading, writing, and appending
# data to a file

# Create a new file 
def create_file(file_name):
    f =open(file_name,"x")
    return "file_created"

# read file
def read_file(file_name):
    with open(file_name,"r") as f :
        print(f.read())
        

# write file       
def  write_file(file_name,write_content):
    with open(file_name,"w") as f :
        f.write(write_content)
        f.close()

# appeand file        
def  appeand_file(file_name,write_content):
    with open(file_name,"a") as f :
        f.write(write_content)
        f.close()       
