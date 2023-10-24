from time import sleep

def timer():
    minutes = 0
    seconds = 10

    while ((minutes >= 0 and seconds >= 0)):

        print(f"Time Remaining:\t{minutes:02d}:{seconds:02d}")

        sleep(1)

        seconds -= 1
        if (seconds < 0):
            seconds = 59
            minutes -= 1

def whatnow():
    answer = input("The timer has finished, do you want to start another session? (y/N)\n").lower()
    if (answer not in ["y", "n"]):
        return whatnow()
    return True if answer == "y" else False


def main():
    running = True
    while (running):
        timer()
        running = whatnow()

if __name__ == "__main__":
    main()