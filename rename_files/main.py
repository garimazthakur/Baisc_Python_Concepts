import os
from pathlib import Path
from datetime import datetime

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)



# # using os
# path1 =   os.path.dirname(os.path.abspath(__file__))
# path11 =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path111 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# print(f"path1 is : {path1}")
# print(f"path11 is : {path11}")
# print(f"path111 is : {path111}")


# print("***********************************************")
# print("***********************************************")

# # using pathlib
# path2=    Path(__file__).resolve().parent
# path22=   Path(__file__).resolve().parent.parent
# path222 = Path(__file__).resolve().parent.parent.parent

# print(f"path2 is : {path2}")
# print(f"path22 is : {path22}")
# print(f"path222 is : {path222}")
# print("***********************************************")


# path =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(os.listdir(path))
# path_resume = r'path/resume/'
# print(path_resume)
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2")

# dir = os.path.dirname(os.path.dirname(__file__)) 
# dirname1 = os.path.basename(dir) 
# dirname2 = os.path.split(dir)
# dirname3 = os.path.split(dir)[1]




# print("***********************************************")

# print(dir)
# print(dirname1)
# print(dirname2)    
# print(dirname3)
import datetime
dir = os.path.dirname(os.path.dirname(__file__)) 
name = dir + "/resume"
filename= os.listdir(name)

# Method1
# files= []
# for file in filename:
#     extension = file.split(".")  # filename
#     # new_name=str(datetime.datetime.now()).split(".")[0].replace(" ", "_")
#     name = str(datetime.datetime.now()).split(".")
#     new1 = name[0].replace(" ", "_")
#     # print(new1)
#     new2 = name[1]
#     new = " ".join([new1, new2]).replace(" ", "_")
#     new_name = str(new) + "." + str(extension[-1])  # doubt
#     # print(new_name)
#     files.append(new_name)
# print(files)


# output:
# ['2022-05-05_13:22:07_321864.pdf', '2022-05-05_13:22:07_321890.pdf', '2022-05-05_13:22:07_321896.pdf', '2022-05-05_13:22:07_321900.pdf', '2022-05-05_13:22:07_321903.pdf', '2022-05-05_13:22:07_321907.pdf']

# Method2

files= []
for file in filename:
    extension = file.split(".")[-1]  # filename
    # new_name=str(datetime.datetime.now()).split(".")[0].replace(" ", "_")
    new_name = str(datetime.datetime.now()).split(".")[0].replace(" ", "_")
    new_name = new_name + "." + extension 
    # print(new_name)
    files.append(new_name)
print(files)

# output
# ['2022-05-05_13:26:53.pdf', '2022-05-05_13:26:53.pdf', '2022-05-05_13:26:53.pdf', '2022-05-05_13:26:53.pdf', '2022-05-05_13:26:53.pdf', '2022-05-05_13:26:53.pdf']
