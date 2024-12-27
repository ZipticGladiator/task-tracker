import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import json
import matplotlib.pyplot as plt

class TaskTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Time Tracker")

        # Load tasks from a JSON file or initialize an empty dictionary if the file doesn't exist
        self.tasks = self.load_tasks()

        self.current_task = None
        self.start_time = None
        self.paused_time = None

        # UI Elements
        # Label to prompt the user to input a task name
        self.task_name_label = tk.Label(root, text="Task Name:")
        self.task_name_label.pack(pady=5)

        # Text entry for the user to input a task name
        self.task_name_entry = tk.Entry(root, width=30)
        self.task_name_entry.pack(pady=5)

        # Button to start tracking a task
        self.start_button = tk.Button(root, text="Start Task", command=self.start_task)
        self.start_button.pack(pady=5)

        # Button to pause tracking a task
        self.pause_button = tk.Button(root, text="Pause Task", command=self.pause_task)
        self.pause_button.pack(pady=5)

        # Button to stop tracking a task
        self.stop_button = tk.Button(root, text="Stop Task", command=self.stop_task)
        self.stop_button.pack(pady=5)

        # Button to refresh and display the list of tasks
        self.show_button = tk.Button(root, text="Show Tasks", command=self.show_tasks)
        self.show_button.pack(pady=5)

        # Listbox to display tasks and their time information
        self.task_list = tk.Listbox(root, width=50, height=15)
        self.task_list.pack(pady=10)

        # Button to export task data to a JSON file
        self.export_button = tk.Button(root, text="Export to JSON", command=self.export_tasks)
        self.export_button.pack(pady=5)

        # Button to display a chart of task times
        self.chart_button = tk.Button(root, text="Show Task Chart", command=self.show_chart)
        self.chart_button.pack(pady=5)

        # Label to display the elapsed time
        self.elapsed_time_label = tk.Label(root, text="Elapsed Time: 0s")
        self.elapsed_time_label.pack(pady=5)

        # Start the update loop for the elapsed time
        self.update_elapsed_time()

        # Update the task list initially
        self.update_task_list()

    def load_tasks(self):
        # Load tasks from "tasks.json", or return an empty dictionary if the file doesn't exist
        try:
            with open("tasks.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_tasks(self):
        # Save tasks to "tasks.json"
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f, indent=4)

    def start_task(self):
        task_name = self.task_name_entry.get().strip()

        # Validate input
        if not task_name:
            messagebox.showwarning("Input Error", "Task name cannot be empty!")
            return

        # Check if the task is already running
        if self.current_task and self.paused_time:
            # Resume the paused task
            self.start_time += time.time() - self.paused_time
            self.paused_time = None
        else:
            # Start a new task
            self.current_task = task_name
            self.start_time = time.time()
        self.task_name_entry.delete(0, tk.END)
        messagebox.showinfo("Task Started", f"Started task '{task_name}'.")
        self.update_task_list()

    def pause_task(self):
        if self.current_task and not self.paused_time:
            self.paused_time = time.time()
            messagebox.showinfo("Task Paused", f"Paused task '{self.current_task}'.")
        elif not self.current_task:
            messagebox.showwarning("No Task Running", "No task is currently running to pause.")

    def stop_task(self):
        if self.current_task:
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            if self.current_task in self.tasks:
                self.tasks[self.current_task]['total_time'] += elapsed_time
            else:
                self.tasks[self.current_task] = {'total_time': elapsed_time}
            messagebox.showinfo("Task Stopped", f"Stopped task '{self.current_task}'.")
            self.current_task = None
            self.start_time = None
            self.paused_time = None
            self.update_task_list()
        else:
            messagebox.showwarning("No Task Running", "No task is currently running to stop.")

    def show_tasks(self):
        # Refresh the task list in the UI
        self.update_task_list()

    def update_task_list(self):
        # Clear the current task list and display updated task data
        self.task_list.delete(0, tk.END)
        for task_name, info in self.tasks.items():
            total_time = info.get('total_time', 0)
            running = ' (Running)' if task_name == self.current_task and not self.paused_time else ''
            self.task_list.insert(tk.END, f"{task_name}: {total_time:.2f} seconds{running}")

    def export_tasks(self):
        # Save tasks to the JSON file and notify the user
        self.save_tasks()
        messagebox.showinfo("Export Successful", "Tasks exported to tasks.json.")

    def show_chart(self):
        # Generate a bar chart to compare task times
        task_names = list(self.tasks.keys())
        task_times = [info['total_time'] for info in self.tasks.values()]

        if not task_names:
            messagebox.showinfo("No Data", "No tasks available to display in the chart.")
            return

        plt.figure(figsize=(10, 6))
        plt.bar(task_names, task_times, color="skyblue")
        plt.xlabel("Tasks")
        plt.ylabel("Total Time (seconds)")
        plt.title("Task Time Comparison")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    def update_elapsed_time(self):
        if self.current_task and not self.paused_time:
            elapsed_time = int(time.time() - self.start_time)
            self.elapsed_time_label.config(text=f"Elapsed Time: {elapsed_time}s")
        self.root.after(1000, self.update_elapsed_time)

if __name__ == "__main__":
    # Initialize the main application window
    root = tk.Tk()
    app = TaskTrackerApp(root)
    root.mainloop()
