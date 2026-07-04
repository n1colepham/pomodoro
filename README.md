# 🍅 Cute Pomodoro Timer

A modern, customizable desktop Pomodoro timer built with Python 3.13. Designed to easily transition from a command-line utility to a desktop GUI, and eventually onto physical hardware.

## 🚀 Features & Roadmap
- [x] **Phase 1:** Decoupled core timer engine with a Command-Line Interface (CLI).
- [ ] **Phase 2:** Modern, cute Graphical User Interface (GUI) using CustomTkinter.
- [ ] **Phase 3:** Hardware integration using MicroPython/CircuitPython for a physical desktop device.

## 📁 Architecture
The project is built using a decoupled architecture, separating the core timer logic from the user interface:
- `src/timer.py`: The core countdown engine (independent of any UI).
- `src/cli.py`: The terminal-based interface wrapper.

## ⚙️ How to Run

### Prerequisites
- Python 3.13+

### Running the CLI Timer
Clone the repository, open your terminal in the project root directory, and execute the module:

```bash
python -m src.cli
```

*Press `Ctrl + C` in the terminal at any time to safely stop the timer.*
