import time
from collections.abc import Callable

class PomodoroTimer:
    def __init__(self, work_mins: int=25, break_mins: int=5) -> None:
        self.work_seconds:int = work_mins * 60
        self.break_seconds:int = break_mins * 60
        self.is_running:bool = False
        self.current_state:str = "WORK"  # Can be "WORK" or "BREAK"

    def start(self, tick_callback: Callable[[str, str], None]) -> None:
        """Starts the timer loop. Requires a callback function to handle the time display."""
        self.is_running:bool = True
        remaining = self.work_seconds if self.current_state == "WORK" else self.break_seconds

        while remaining > 0 and self.is_running:
            mins, secs = divmod(remaining, 60)
            # Send the formatted time string back to the interface
            tick_callback(f"{mins:02d}:{secs:02d}", self.current_state)
            time.sleep(1)
            remaining -= 1

        if self.is_running:
            self.is_running = False
            self.switch_state()
            tick_callback("00:00", f"FINISHED_{self.current_state}")

    def stop(self) -> None:
        self.is_running = False

    def switch_state(self) -> None:
        self.current_state = "BREAK" if self.current_state == "WORK" else "WORK"
