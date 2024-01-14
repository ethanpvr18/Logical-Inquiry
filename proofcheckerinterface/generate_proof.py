# Imports
from .Table import Table
from .utilities import contains

# TODO:
#   -> Order of Operations
#   -> Parentheses
#   -> In Rules
#   -> PA

def generate_proof(statement):
    # Variables
    current_line_number = 1
    generated_table = Table()

    # STEP 1 | Identify Assumptions
    assumptions = []
    # Identify left side of the statement
    altered_statement = statement[0:statement.index('|-')-1]
    # Remove spaces from statement
    altered_statement.replace(' ', '')

    # Split statement into assumptions
    while contains(',', altered_statement):
        # Split statement by commas
        assumptions.append(altered_statement[0:altered_statement.index(',')])
        # Remove recently added assumption from statement
        altered_statement = altered_statement[altered_statement.index(',')+1:]
    if contains(',', altered_statement) == False:
        # Add final assumption
        assumptions.append(altered_statement)

    # Add Line for Assumptions
    for assumption in assumptions:
        # Remove spaces
        assumption = assumption.replace(' ', '')
        # Add Line
        generated_table.add_line(current_line_number, current_line_number, assumption, 'A')
        # Go to next assumption
        current_line_number += 1

    # STEP 2 | Apply Rules
    # ->
    arrow_symbol = '->'
    arrow_out_rule = '->O'
    for i in range(generated_table.get_length()):
        primary_line = generated_table.get_line(i)
        if contains(arrow_symbol, primary_line.get_formula()):
            for j in range(generated_table.get_length()):
                secondary_line = generated_table.get_line(j)
                if (contains(arrow_symbol, secondary_line.get_formula()) != True) & (primary_line.get_line_number() != secondary_line.get_line_number()):
                    primary_formula = primary_line.get_formula()
                    letter_one = primary_formula[primary_formula.index(arrow_symbol)-1]
                    letter_two = primary_formula[primary_formula.index(arrow_symbol)+len(arrow_symbol)]
                    assumption_dependence = str(primary_line.get_line_number()) + ', ' + str(secondary_line.get_line_number())
                    justification = str(arrow_out_rule) + ', ' + assumption_dependence
                    generated_table.add_line(assumption_dependence, current_line_number, letter_two, justification)
                    current_line_number += 1

    # &
    and_symbol = '&'
    and_out_rule = '&O'
    for i in range(generated_table.get_length()):
        primary_line = generated_table.get_line(i)
        if contains(and_symbol, primary_line.get_formula()):
            primary_formula = primary_line.get_formula()
            letter_one = primary_formula[primary_formula.index(and_symbol)-1]
            letter_two = primary_formula[primary_formula.index(and_symbol)+len(and_symbol)]
            assumption_dependence = str(primary_line.get_line_number())
            justification = str(and_out_rule) + ', ' + assumption_dependence
            generated_table.add_line(assumption_dependence, current_line_number, letter_one, justification)
            current_line_number += 1
            generated_table.add_line(assumption_dependence, current_line_number, letter_two, justification)
            current_line_number += 1

    # ~
    not_symbol = '~'
    not_out_rule = '~O'
    for i in range(generated_table.get_length()):
        primary_line = generated_table.get_line(i)
        if contains(not_symbol, primary_line.get_formula()):
            primary_formula = primary_line.get_formula()
            letter_one = primary_formula[primary_formula.index(not_symbol)+len(not_symbol)]
            assumption_dependence = str(primary_line.get_line_number())
            justification = str(not_out_rule) + ', ' + assumption_dependence
            generated_table.add_line(assumption_dependence, current_line_number, letter_one, justification)
            current_line_number += 1

    # <-->
    iff_symbol = '<-->'
    iff_out_rule = '<-->O'
    for i in range(generated_table.get_length()):
        primary_line = generated_table.get_line(i)
        if contains(iff_symbol, primary_line.get_formula()):
            primary_formula = primary_line.get_formula()
            letter_one = primary_formula[primary_formula.index(iff_symbol)-1]
            letter_two = primary_formula[primary_formula.index(iff_symbol)+len(iff_symbol)]
            assumption_dependence = str(primary_line.get_line_number())
            justification = str(iff_out_rule) + ', ' + assumption_dependence
            generated_table.add_line(assumption_dependence, current_line_number, letter_one+'->'+letter_two, justification)
            current_line_number += 1
            generated_table.add_line(assumption_dependence, current_line_number, letter_two+'->'+letter_one, justification)
            current_line_number += 1
                    

    # v
    or_symbol = 'v'
    or_out_rule = 'vO'

    for i in range(generated_table.get_length()):
        primary_line = generated_table.get_line(i)
        if contains(or_symbol, primary_line.get_formula()):
            primary_formula = primary_line.get_formula()
            letter_one = primary_formula[primary_formula.index(or_symbol)-1]
            letter_two = primary_formula[primary_formula.index(or_symbol)+len(or_symbol)]
            assumption_dependence = str(primary_line.get_line_number())
            justification = str(or_out_rule) + ', ' + assumption_dependence
            generated_table.add_line(assumption_dependence, current_line_number, letter_one, justification)
            current_line_number += 1
            generated_table.add_line(assumption_dependence, current_line_number, letter_two, justification)
            current_line_number += 1
    
    return generated_table

def print_proof_table(proof_table):
    for line in range(proof_table.get_length()):
        primary_line = proof_table.get_line(line)
        print(str(primary_line.get_assumption_dependence()) + '     ' + str(primary_line.get_line_number()) + '     ' + str(primary_line.get_formula()) + '     ' + str(primary_line.get_justification()) + '\n')

def to_array(proof_table):
    lines = []
    for line in range(proof_table.get_length()):
        primary_line = proof_table.get_line(line)
        line = [str(primary_line.get_assumption_dependence()), str(primary_line.get_line_number()), str(primary_line.get_formula()), str(primary_line.get_justification())]
        lines.append(line)
    return lines


# STEP 1 | Generate Proof From Statement
# generated_proof = generate_proof('AvB,C&D,F<-->G,~X |- A')

# STEP 2 | Create User Table

# TODO:
#   -> Create User Table

# STEP 3 | Compare Tables

# TODO:
#   -> Compare Tables

# STEP 4 | Export Results / Web Interface

# TODO:
#   -> Web Interface
#   -> Align Table

# print_proof_table(generated_proof)
