import os
def demo_os():
    current_dir = os.getcwd()
    print(f"{current_dir = }")
    new_dir =  os.path.join(current_dir, 'demo_dir')
    # print(f"{new_dir = }")
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        print(f"\n Directory 'demo_dir' created at '{new_dir}'")
    else:
        print(f"\nDirectory 'demo_dir' already exists at '{new_dir}'")

    # List all files and folders in the curent directory
    print("\nFiles and folder:")
    # for item in os.listdir(current_dir):
    #     print(item)

    for index, item in enumerate(os.listdir(current_dir)):
        print(f"\t{index} - {item}")


    new_file_path = os.path.join(new_dir, 'demo_file.txt')
    # file = open(new_file_path, 'w')
    # file.write("This is demo")
    # # file.flush()
    # file.close()

    with open(new_file_path, 'w') as file:
        file.write("This is demo")
        file.writelines(["Str1", "Str2", "Str3"])
        file.writelines(["\nStr4", "\nStr5", "\nStr6"])
    print("\nFile 'demo_file.txt' has been created")

    with open(new_file_path, "r") as file:
        # str1 = file.read(10)
        # str1 = file.readline(512)
        str1 = file.readlines(512)
        print(f"\n File data:\n{str1}")
        # str1 = file.readline(512)
        # print(f"\n File data:\n{str1}")

    if os.path.exists(new_file_path):
        os.remove(new_file_path)
        print("\n'demo_file.txt' has been removed")
    else:
        print("\n'demo_file.txt' doesn't exist")

    os.rmdir(new_dir)
    print("\nFolder 'demo_dir' has been removed")


demo_os()