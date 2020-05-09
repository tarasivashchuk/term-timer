import re
import sys
from time import time, sleep
from typing import List

hh_mm_ss_re = re.compile(r"^(\d+|(\d{1,2}:\d{2})|(\d{1,2}:\d{2}:\d{2}))$")  # seconds | mm:ss | hh:mm:ss


def main(args: List[str]):
    if len(args) == 0:
        chronometer()
    elif len(args) == 1 and hh_mm_ss_re.match(args[0]):
        timer(args[0])
    else:
        help()


def timer(arg: str):
    assert hh_mm_ss_re.match(arg)

    split = arg.split(":")
    seconds = 0
    for s in split:
        seconds *= 60
        seconds += int(s)
    print(_seconds_to_time_string(seconds), end="   \r")

    end_time = int(time()) + seconds
    while True:
        try:
            sleep(1)
        except KeyboardInterrupt:
            print()
            exit(1)

        remaining_seconds = end_time - int(time())
        if remaining_seconds <= 0:
            break
        print(f"{_seconds_to_time_string(remaining_seconds)}", end="   \r")

    print("Time is up! (Ctrl+C to exit)", end="")

    while True:
        try:
            print("\a", end="")
            sys.stdout.flush()
            sleep(2)
        except KeyboardInterrupt:
            print()
            exit(0)


def chronometer():
    start_time = int(time())
    print(f"{_seconds_to_time_string(0)}", end="   \r")
    while True:
        try:
            sleep(1)
        except KeyboardInterrupt:
            print()
            exit(1)

        elapsed_seconds = int(time()) - start_time
        print(f"{_seconds_to_time_string(elapsed_seconds)}", end="   \r")


def help():
    print("Usage: python src/main.py [[[HH:]MM:]SS]")
    print()
    print("Call it with no arguments to start the chronometer/stopwatch.")
    print("Provide a single integer set up a timer with that amount of seconds.")
    print("Provide 'MM:SS' set the timer for MM minutes and SS seconds.")
    print("Provide 'HH:MM:SS' set the timer for HH hours, MM minutes and SS seconds.")
    print("You may stop the program at any time with CTRL+C.")


def _seconds_to_time_string(seconds: int):
    secs = seconds % 60
    minutes = seconds // 60
    mins = minutes % 60
    hours = minutes // 60

    if hours == 0:
        return "%02d:%02d" % (mins, secs)
    return "%02d:%02d:%02d" % (hours, mins, secs)


main(sys.argv[1:])
