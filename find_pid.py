import os


def main():
    """
    finds a process id
    """
    path = r'/proc'
    name = input("Please enter a precess name: ")
    process_lst = os.listdir(path)
    for proc_num in process_lst:
        try:
            f = open("/proc/" + proc_num + "/status", 'r')
            if name in f.read():
                print("The pid of " + name + " is: " + proc_num)
            f.close()
        except NotADirectoryError:
            pass
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    main()