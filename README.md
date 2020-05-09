# cli-timer-chronometer

## Features

* Command-line based chronometer, which prints the time elapsed since the program started.
* Command-line based timer, which prints the time remaining until the provided time mark.
* The timer will warn you when the time is up with the system-defined sound by printing `\a` on the standard output in 2 second intervals until you dismiss it.


## Usage

    python src/main.py [[[HH:]MM:]SS]

* Call it with no arguments to immediately start the chronometer/stopwatch.
* Provide a single integer set up a timer with that amount of seconds.
* Provide 'MM:SS' set the timer for MM minutes and SS seconds.
* Provide 'HH:MM:SS' set the timer for HH hours, MM minutes and SS seconds.
* **You may stop the program at any time with Ctrl+C.**

## Requirements

* [Python 3](https://www.python.org/downloads/).
* No PIP package dependencies.
* Tested on Windows, but should also work on Mac and Linux.

## Example usages

    python src/main.py         # start chronometer (stop it with Ctrl+C)
    python src/main.py 90      # set timer for 90 seconds
    python src/main.py 5:00    # set timer to 5 minutes
    python src/main.py 1:30:00 # set timer for a hour and a half
    python src/main.py 1:30    # set timer for a minute and a half
    
## Additional notes

* You may set up a command line alias so its easier to use this tool from anywhere. I have mine set up as `ck`, short for `clock`.
