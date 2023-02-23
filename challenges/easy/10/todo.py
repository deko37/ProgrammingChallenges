import time

class ToDo:
    def __init__(self, have_to_do: str):
        self.to_do = have_to_do
        self.time = time.time()
        self.checked = False

    def __repr__(self):
        return f"[{'✓' if self.checked else 'X'}] {self.to_do} ({time.ctime(self.time)})"

    def check(self):
        self.checked = True
