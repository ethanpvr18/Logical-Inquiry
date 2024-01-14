# Imports
from .Line import Line

class Table:

    # Constructor
    def __init__(self):
        self.table = []
        self.length = 0

    # Getters
    def get_line(self, index):
        return self.table[index]
    
    def get_length(self):
        return self.length

    # Setters
    def update_line(self, index, assumption_dependence, line_number, formula, justification):
        self.table[index] = Line(assumption_dependence, line_number, formula, justification)

    def add_line(self, assumption_dependence, line_number, formula, justification):
        new_line = Line(assumption_dependence, line_number, formula, justification)
        self.table.append(new_line)
        self.length += 1