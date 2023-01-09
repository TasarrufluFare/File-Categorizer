#Github Tasarruflu Fare
import os


def categorize_files(path):
    try:
        extension_set = set()
        files_categorized = {}

        for filename in os.listdir(path):
            filename_without_ext = os.path.splitext(filename)[0]
            extension = os.path.splitext(filename)[1]

            if extension != '':
                extension_set.add(extension)
                files_categorized.update({filename_without_ext: extension})

        for file_name in files_categorized:
            file_ext = files_categorized[file_name].replace(".", "")
            new_file_path = path + "\\" + "Categorized Files" + "\\" + file_ext + " files"
            try:
                os.makedirs(new_file_path)
            except FileExistsError:
                pass
            try:
                src = path + "\\" + file_name + "." + file_ext
                dest = new_file_path + "\\" + file_name + "." + file_ext

                files_exists_counter = 0
                error_flag = False
                while os.path.exists(dest):
                    files_exists_counter = files_exists_counter + 1
                    dest = new_file_path + "\\" + file_name + f" ({files_exists_counter})" + "." + file_ext
                    if files_exists_counter == 25:
                        error_flag = True
                        break

                if error_flag == False:
                    os.replace(src, dest)
                elif error_flag == True:
                    print("An error occurred while selecting the destination for categorized file!!!")

            except Exception as error:
                print(error)
        print("Files Succesfully Categorized!!")

    except Exception as e:
        print(e)


while True:

    print("To Exit Type Quit")
    path_usr = input("Enter the directory path where you need to categorize: ")

    if path_usr.startswith("C:\Windows"):
        print("What da hack are you doing!?!??!?!?")
        time.sleep(1)
        exit()

    if path_usr == "Quit" or path_usr == "quit":
        exit()

    while os.path.exists(path_usr) == False:
        if path_usr == "Quit" or path_usr == "quit":
            exit()
        print("Path you given does not exists!")
        path_usr = input("Enter the directory path where you need to categorize: ")

    print("Do you really want to Categorize Files in this path?  - it may cause errors if the path is wrong!! ")
    confirm = input("Y / n \t (Default=n): ")

    if confirm == "Y" or confirm == "y":
        categorize_files(path_usr)
    else:
        print("Operation Cancelled!")



