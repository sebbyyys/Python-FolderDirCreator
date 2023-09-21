import os
import os.path
import time

illegal = '<>:"/\|?* '
yesInputs = ["yes", "Yes", "y", "Y"," yes","yes "]
name = "yes"


while name in yesInputs:
    name = ""
    name = input("\nWould you like to use the program? Yes or no/exit? ")
    if name in yesInputs:
        ###root_path = 'E:\FolderMaker\Folders'
        root_path = input("\nPlease copy and paste in the filepath of where you want to make folders: ")
        folders = input("\nPlease input each folder name followed by a semicolon. (1;2;3;4 is a valid input): ")
            
        # checks if the directory path specified is a correct one
        check = os.path.isdir(root_path)
        emptyString = ""

        # error checking all of following code
        try:
            if check == False:
                raise(LookupError)
        # checks if any characters in the folder input are illegal (cant be added to folder name)
            for x in folders:
                if x not in illegal:
                    emptyString += x
                else:
        # if characters are illegal then make the emptyString variable blank and  raise an error which will stop program carrying on
                    emptyString = ""
                    raise(MemoryError)

        # checks to see if the emptyString variable is empty, if it is it returns error so no single folders are made
            if emptyString == "":
                raise(MemoryError)
        # otherwise takes the string splits it between colons and makes it into a list, joins the path and list together and makes a directory for each item in the list
            else:
                finalList = emptyString.split(";")
                for items in finalList:
                    path = os.path.join(root_path, items)
                    os.mkdir(path)
                listnames = ''
                for x in finalList:
                    listnames += ' ' + x
                print(f"\nSuccessfully created folders{listnames[0:-1]}and {listnames[-1:]}")
                time.sleep(5) 
                
        except MemoryError:
            print("\nIllegal character detected \n""\n""None of the following characters are allowed: \n""\n"""' < > : " / \ | ? * '"")
            time.sleep(5)
        except LookupError:
            print("\nWrong Filepath. Please input the correct filepath ")
            time.sleep(5)
        except FileExistsError:
            print("\nOne of those files already exists please make sure they are all unique or rename it to something else ")
            time.sleep(5)
    else:
        break