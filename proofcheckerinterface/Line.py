class Line:

    # Constructor
    def __init__(self, assumption_dependence, line_number, formula, justification):
        self.assumption_dependence = assumption_dependence
        self.line_number = line_number
        self.formula = formula
        self.justification = justification
        self.current = 0

    # Getters
    def get_assumption_dependence(self):
        return self.assumption_dependence

    def get_line_number(self):
        return self.line_number

    def get_formula(self):
        return self.formula

    def get_justification(self):
        return self.justification
    
    #Setters
    def set_assumption_dependence(self, input):
        self.assumption_dependence = input

    def set_line_number(self, input):
        self.line_number = input

    def set_formula(self, input):
        self.formula = input

    def set_justification(self, input):
        self.justification = input