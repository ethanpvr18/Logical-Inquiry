# def remove_spaces(statement):
#     return statement.replace(' ', '')

# def remove_commas(statement):
#     return statement.replace(',', '')

# def remove_rules(statement):
#     new_statement = ''
#     new_statement = statement.replace('<-I', '')
#     new_statement = statement.replace('&O', '')
#     new_statement = statement.replace('&I', '')
#     new_statement = statement.replace('<-O', '')

#     return new_statement

# def contains_connective(statement):
#     connectives = ['->','&','~','v','<->']
#     exists = False
#     for connective in connectives:
#         if statement.find(str(connective)) != -1:
#             exists = True
#             return exists
#         else:
#             exists = False
#     return exists
    
# def contains(string, target):
#     return string.find(target) != -1

# def find_key(dict, target):
#     for key, value in dict:
#         if key == target:
#             return str(value)
    
# def is_letter(string):
#     letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     return letters.find(string) != -1

# def find_solos(statement):
#     letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for index, character in enumerate(statement):
#         if index+1 < len(statement) and index - 1 >= 0:
#             if is_letter(statement[index]) and is_letter(statement[index-1]) and is_letter(statement[index+1]):
#                 statement[index]


    
# def split_statement(original_statement):
#     edited_statement = []
#     no_spaces = remove_spaces(original_statement)
#     if no_spaces.find('-|'):
#         no_spaces = no_spaces[0:no_spaces.index('-|')]
#     while contains_connective(no_spaces):
#         if no_spaces.find('<->') != -1:
#             statement = no_spaces[no_spaces.index('<->')-1:no_spaces.index('<->')+len('<->')+1]
#             no_spaces = no_spaces.replace(statement, '')
#             edited_statement.append(statement)
#         if no_spaces.find('->') != -1:
#             statement = no_spaces[no_spaces.index('->')-1:no_spaces.index('->')+len('->')+1]
#             no_spaces = no_spaces.replace(statement, '')
#             edited_statement.append(statement)
#         if no_spaces.find('&') != -1:
#             statement = no_spaces[no_spaces.index('&')-1:no_spaces.index('&')+len('&')+1]
#             no_spaces = no_spaces.replace(statement, '')
#             edited_statement.append(statement)
#         if no_spaces.find('~') != -1:
#             statement = no_spaces[no_spaces.index('~')-2:no_spaces.index('~')+len('~')+1]
#             no_spaces = no_spaces.replace(statement, '')
#             edited_statement.append(statement)
#         if no_spaces.find('v') != -1:
#             statement = no_spaces[no_spaces.index('v')-1:no_spaces.index('v')+len('v')+1]
#             no_spaces = no_spaces.replace(statement, '')
#             edited_statement.append(statement)
#         if len(no_spaces) == 1:
#             statement = no_spaces
#             no_spaces = ''
#             edited_statement.append(statement)
    
#     return edited_statement

# def add_line(proof_table, assumption_dependence, line_number, formula, justification):
#     proof_table[line_number] = {
#         'assumption_dependence' : assumption_dependence,
#         'line_number' : line_number,
#         'formula' : formula,
#         'justification' : justification
#     }
#     return proof_table

# def del_line(proof_table, target):
#     proof_table.pop(target)
#     return proof_table

# def identify_assumptions(proof_table, statement_list):
#     num = 0
#     for statement in statement_list:
#         num += 1
#         add_line(proof_table, str(num), str(num), statement, 'A')

# def search_for(proof_table, inputted_element_key, target, exact):
#     for line_key, line_value in proof_table.items():
#         for element_key, element_value in line_value.items():
#             if element_key == inputted_element_key:
#                 if exact == False:
#                     if contains(proof_table[line_key][element_key], target):
#                         return proof_table[line_key]
#                 else:
#                     if proof_table[line_key][element_key] == target:
#                         return proof_table[line_key]


# def transfrom_assumptions(proof_table, target):
#     dependence_line = search_for(proof_table, 'formula', str(target)+str('->'), False)
#     solo_line = search_for(proof_table, 'formula', str(target), True)
#     dependence_line_number = dependence_line['line_number']
#     solo_line_number = solo_line['line_number']
#     new_formula = dependence_line['formula'][dependence_line['formula'].index(str(target)+str('->'))+len(str(target)+str('->')):]    
#     add_line(proof_table, str(len(proof_table)+1), len(proof_table)+1, new_formula, str(dependence_line_number)+', '+str(solo_line_number)+' <-O')
#     return new_formula

# def iff_out(proof_table):
#     dependence_line = search_for(proof_table, 'formula', '<->', False)
#     dependence_line_number = dependence_line['line_number']
#     statement = dependence_line['formula']
#     if contains(statement, '<->'):
#         var_1 = statement[statement.index('<->')-1]
#         var_2 = statement[statement.index('<->')+len('<->')]
#         new_formula_1 = var_1 + '->' + var_2
#         new_formula_2 = var_2 + '->' + var_1
#         add_line(proof_table, str(len(proof_table)+1), len(proof_table)+1, new_formula_1, str(dependence_line_number)+' <->O')
#         add_line(proof_table, str(len(proof_table)+1), len(proof_table)+1, new_formula_2, str(dependence_line_number)+' <->O')

# def and_out(proof_table):
#     dependence_line = search_for(proof_table, 'formula', '&', False)
#     dependence_line_number = dependence_line['line_number']
#     statement = dependence_line['formula']
#     if contains(statement, '&'):
#         var_1 = statement[statement.index('&')-1]
#         var_2 = statement[statement.index('&')+len('&')]
#         add_line(proof_table, str(len(proof_table)+1), len(proof_table)+1, var_1, str(dependence_line_number)+' &O')
#         add_line(proof_table, str(len(proof_table)+1), len(proof_table)+1, var_2, str(dependence_line_number)+' &O')

# def wedge_out(proof_table):
#     dependence_line = search_for(proof_table, 'formula', 'v', False)
#     dependence_line_number = dependence_line['line_number']
#     statement = dependence_line['formula']
#     if contains(statement, 'v'):
#         var_1 = statement[statement.index('v')-1]
#         var_2 = statement[statement.index('v')+len('v')]
#         add_line(proof_table, str(len(proof_table)+1), len(proof_table)+1, var_1, str(dependence_line_number)+', '+' vO')
#         add_line(proof_table, str(len(proof_table)+1), len(proof_table)+1, var_2, str(dependence_line_number)+', '+' vO')



# def process(proof_table):
#     if search_for(proof_table, 'formula', '&', False) == True:
#         and_out(proof_table)
#     if search_for(proof_table, 'formula', '<->', False) == True:
#         iff_out(proof_table)
#     if search_for(proof_table, 'formula', 'v', False) == True:
#         wedge_out(proof_table)

#     assumptions = []
#     for line in proof_table:
#         if proof_table[line]['justification'] == 'A':
#             assumptions.append(proof_table[line])
    
#     assumptions_letters = []
#     for line in assumptions:
#         if len(line['formula']) == 1:
#             assumptions_letters.append(line['formula'])

#     for letter in assumptions_letters:
#         transfrom_assumptions(proof_table, str(letter))
#     # transfrom_assumptions(proof_table, 'B')

#     not_assumptions = []
#     for line in proof_table:
#         if proof_table[line]['justification'] != 'A':
#             not_assumptions.append(proof_table[line])
#             proof_table[line]['assumption_dependence'] = remove_rules(proof_table[line]['justification'])

# def setup(original_statement):
#     proof_table = {}
#     edited_statement = split_statement(original_statement)
#     identify_assumptions(proof_table, edited_statement)
#     process(proof_table)
#     return proof_table

# def print_proof_table(proof_table):
#     for line_key, line_value in proof_table.items():
#         for element_key, element_value in line_value.items():
#             print(str(element_value)  + '     ', end='')
#         print('\n')

# print_proof_table(setup('A->B B->C A -| C'))

# 'A->B B->C A -| C'

# add_line(dict, '1', '1', 'A->B', 'A')
# add_line(dict, '2', '2', 'B->C', 'A')
# add_line(dict, '3', '3', 'A', 'A')
# add_line(dict, '1,2', '4', 'B', '1,3,->O')
# add_line(dict, '1,2,3', '5', 'C', '2,4,->O')





