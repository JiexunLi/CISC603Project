import os


def main():
    while True:
        input_string = input()
        if input_string == "ls":
            dirs = os.listdir(os.getcwd())
            for dir in dirs:
                print(dir)
        elif input_string == "pwd":
            print(os.getcwd())
        else:
            print("invalid input!")


if __name__ == '__main__':
    main()