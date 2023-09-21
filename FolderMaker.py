import os
import os.path
import time

illegal = '<>:"/\|?*'

    #root_path = 'E:\FolderMaker\Folders'
root_path = input("Please copy and paste in the filepath of where you want to make folders: ")
folders = input("Please input each folder name followed by a semicolon:")
    

check = os.path.isdir(root_path)
emptyString = ""

try:
    if check == False:
        raise(TypeError)
    for x in folders:
        if x not in illegal:
            emptyString += x
        else:
            emptyString = ""
            raise(NameError)
       
    if emptyString == "":
        raise(NameError)
    else:
        finalList = emptyString.split(";")
        for items in finalList:
            path = os.path.join(root_path, items)
            os.mkdir(path)
        listnames = ''
        for x in finalList:
            listnames += ' ' + x
        print(f"Successfully created folders{listnames[0:-1]}and {listnames[-1:]}")
        time.sleep(5)  
        
except NameError:
    print("Illegal character detected \n""\n""None of the following characters are allowed: \n""\n"""' < > : " / \ | ? * '"")
    time.sleep(5)
except TypeError:
    print("Wrong Filepath. Please input the correct filepath")
    time.sleep(5)
except FileExistsError:
    print("One of those files already exists please make sure they are all unique or rename it to something else")
    time.sleep(5)


    
