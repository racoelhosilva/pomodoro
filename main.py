import curses
from curses import wrapper
from time import sleep

def getUserInput(stdscr, option):
    try:
        curses.echo()
        yOutput = 2 * curses.LINES // 3
        xOutput = curses.COLS // 3 if option == "Minutes" else 2 * curses.COLS // 3 - 8
        stdscr.addstr(yOutput, xOutput,f"{option}: ")
        result = int(stdscr.getstr(2))

        upperBoundCheck = result > 60 if option == "Minutes" else result >= 60
        lowerBoundCheck = result < 0
        if (upperBoundCheck or lowerBoundCheck):
            throw(ValueError)
    except:
        stdscr.clear()
        errorText = "Please insert a valid numeric value [0-60]."
        stdscr.addstr((2 * curses.LINES // 3 + 4), ((curses.COLS // 2) - (len(errorText) // 2)), errorText)
        return getUserInput(stdscr, option)
    return result

def timer(stdscr, mins, secs):
    minutes = int (mins)
    seconds = int (secs)

    curses.curs_set(0)

    while ((minutes >= 0 and seconds >= 0)):
        stdscr.clear()
        timeOutput = f"Time Remaining:"
        stdscr.addstr((curses.LINES // 3 - 1), ((curses.COLS // 2) - (len(timeOutput) // 2)), timeOutput)
        stdscr.addstr((curses.LINES // 3), ((curses.COLS // 2) - 2),  f"{minutes:02d}:{seconds:02d}")
        stdscr.refresh()
        sleep(1)

        seconds -= 1
        if (seconds < 0):
            seconds = 59
            minutes -= 1

def whatnow(stdscr):
    try:
        curses.echo()
        prompt = "The timer has finished, do you want to start another session? (y/N)  "
        stdscr.addstr((2 * curses.LINES // 3 + 4), ((curses.COLS // 2) - (len(prompt) // 2)), prompt)
        answer = str(stdscr.getstr(1))[2].lower()
        if (answer not in ["y", "n"]):
            throw(ValueError)
    except:
        return whatnow(stdscr)
    return True if answer == "y" else False

def main(stdscr):
    running = True
    while (running):
        # Get Inputs
        stdscr.clear()
        minutes = getUserInput(stdscr, "Minutes")
        seconds = getUserInput(stdscr, "Seconds")

        # Start the Timers
        stdscr.clear()
        stdscr.refresh()
        timer(stdscr, minutes, seconds)

        # Prompt Next Timer
        curses.curs_set(1)
        running = whatnow(stdscr)

if __name__ == "__main__":
    curses.initscr()
    curses.start_color()
    curses.use_default_colors()
    curses.echo()
    wrapper(main)