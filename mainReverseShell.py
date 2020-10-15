from mss import mss


def screen():
    with mss() as sct :
        sct.shot()

screen()
