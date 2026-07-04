import sys
from .timer import PomodoroTimer

def display_time(time_string: str, state: str) -> None:
    """This is the callback function. It dictates HOW the time is shown."""
    # \r keeps the print statement on the same terminal line
    sys.stdout.write(f"\r[{state}] Remaining: {time_string}")
    sys.stdout.flush()
    
    if "FINISHED" in state:
        print(f"\nTime's up! Next phase: {state.split('_')[1]}")

def main() -> None:
    print("Welcome to your Pomodoro Timer!")
    # Initialize with 1 minute work / 1 minute break just for quick testing
    # example_timer = PomodoroTimer(work_mins=1, break_mins=1)
    timer = PomodoroTimer()
    
    try:
        timer.start(tick_callback=display_time)
    except KeyboardInterrupt:
        timer.stop()
        print("\nTimer stopped early. Goodbye!")

if __name__ == "__main__":
    main()
