import json
import os

class History:
    def __init__(self, max_size=100, auto_save=True, base_dir="."):
        # Initialize the history object with max size, save option, and directory.
        self.history = []
        self.max_size = max_size
        self.auto_save = auto_save
        self.base_dir = base_dir
        self.history_file = os.path.join(base_dir, "history.json")
        self.load_history()

    def add(self, entry):
        # Add a new entry to history, removing the oldest if the limit is reached.
        if len(self.history) >= self.max_size:
            self.history.pop(0)
        self.history.append(entry)
        if self.auto_save:
            self.save_history()

    def save_history(self):
        # Save the history to a file.
        with open(self.history_file, 'w') as file:
            json.dump(self.history, file)

    def load_history(self):
        # Load the history from the file, if it exists.
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as file:
                self.history = json.load(file)

    def clear_history(self):
        # Clear the history and save the empty history list.
        self.history = []
        self.save_history()
