from time import sleep

def getUserInput(option):
    try:
        result = int(input(f"{option}:\t"))
        upperBoundCheck = result > 60 if option == "Minutes" else result >= 60
        lowerBoundCheck = result < 0
        if (upperBoundCheck or lowerBoundCheck):
            throw(ValueError)
    except:
        print("Please insert a valid numeric value [0-60].")
        return getUserInput(option)
    return result

def timer(mins, secs):
    minutes = int (mins)
    seconds = int (secs)

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
        minutes, seconds = getUserInput("Minutes"), getUserInput("Seconds")
        print("\n\tTimer is Starting...\n")
        timer(minutes, seconds)
        running = whatnow()

if __name__ == "__main__":
    main()