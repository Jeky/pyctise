#
# Functions in Python are also objects, which means you can pass them around or save them into some containers.
#
import sys


def run():
    print("It is running")


def walk():
    print("It is walking")


def stop():
    print("It stopped")


def exit():
    print("Exit!")
    sys.exit(0)


def help():
    print("[r] to run")
    print("[w] to walk")
    print("[s] to stop")
    print("[e] to exit")
    print("[h] to get help")


def main():
    func_dict = {
        'r' : run,
        'w' : walk,
        's' : stop,
        'e' : exit,
        'h' : help
    }

    while True: # infinite loop
        key = input('INPUT:')
        if key not in func_dict:
            print('Cannot find command [{}]'.format(key))
            help()
        else:
            func_dict[key]()

if __name__ == '__main__':
    main()