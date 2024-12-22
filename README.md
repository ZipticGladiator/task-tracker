# Task Time Tracker

A simple GUI-based task time tracker application built with Python and Tkinter. This application allows users to track the time spent on various tasks, display task summaries, and visualize task durations using bar charts.

## Features
- Start and stop task tracking.
- Display a list of tracked tasks with their total time.
- Save task data to a JSON file.
- Generate bar charts to compare task durations.

## Requirements
- Python 3.6+
- Required Python packages:
  - `tkinter` (included with Python)
  - `matplotlib`

## Installation
### Install Dependencies
1. Install Python 3.6 or higher from [python.org](https://www.python.org/).
2. Install the required packages:
   ```bash
   pip install matplotlib
   ```

### Optional (Homebrew on macOS)
If using Homebrew:
```bash
brew install python
pip3 install matplotlib
```

## Usage
1. Clone or download this repository.
2. Run the application:
   ```bash
   python task_tracker.py
   ```
3. Interact with the GUI to:
   - Enter task names.
   - Start and stop task tracking.
   - View tasks and their durations.
   - Export data to `tasks.json`.
   - View a bar chart comparing task times.

## Files
- `task_tracker.py`: The main Python script.
- `tasks.json`: Stores saved task data.

## Screenshots
- **Main Interface**: Add, start, and stop tasks.
- **Chart Visualization**: Compare task durations using a bar chart.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the application.

