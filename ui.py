import os
import time

_system = os.system
def _portable_system(command):
    if command == "cls" and os.name != "nt":
        # If on web or Mac/Linux, use ANSI escape code to clear
        print("\033[H\033[J", end="")
        return 0
    return _system(command)
os.system = _portable_system

#used ai for type_print function , and for msvcrt
def clear():
    os.system('cls')


try:
    import msvcrt
except ImportError:
    msvcrt = None 
    
def type_print(text, delay = 0.03):
    for i, letter in enumerate(text):
        if msvcrt is not None and msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\r':
                print(text[i:], end="", flush=True)
                break
        print(letter, end="", flush=True)
        time.sleep(delay)
    print()
    while msvcrt is not None and msvcrt.kbhit():
        key = msvcrt.getch()


def input_type(text, delay=0.03):
    for i, letter in enumerate(text):
        if msvcrt is not None and msvcrt.kbhit(): 
            key = msvcrt.getch()

            if key == b'\r':
                print(text[i:], end="", flush=True)
                break

        print(letter, end="", flush=True)
        time.sleep(delay)
    try:
        import js  # type: ignore
        # Use the browser's native pop-up box
        res = js.prompt("")
        return res if res is not None else ""
    except ImportError:
        # Use normal terminal input if playing locally
        return input()

